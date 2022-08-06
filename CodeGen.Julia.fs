module Fable.Sedlex.CodeGen.Julia

open Fable.Sedlex.PrettyDoc
open Fable.Sedlex.Compiler
open Fable.Sedlex.Compiler.Automata

let codegen_julia (import_head: string) (cu: compiled_unit) =

    let mutable decision_funcs : Map<decision_tree, string> = Map.empty

    let mutable tbl_cnt = 0
    let new_tbl_name() =
        tbl_cnt <- tbl_cnt + 1
        sprintf "_sedlex_DT_table_%d" tbl_cnt

    let mutable dt_cnt = 0
    let new_dt_name() =
        dt_cnt <- dt_cnt + 1
        sprintf "_sedlex_decide_%d" dt_cnt

    let mutable rnd_cnt = 0
    let new_rnd_name() =
        rnd_cnt <- rnd_cnt + 1
        sprintf "_sedlex_rnd_%d" rnd_cnt

    let mutable tables : Map<int array, string> = Map.empty

    let mutable toplevels : Doc list = []

    let mutable later_toplevels : Doc list = []

    let push_toplevel doc =
        toplevels <- doc :: empty :: toplevels


    (* forward decl *)
    let push_later_toplevel doc =
        later_toplevels <- doc :: empty :: later_toplevels

    let st_func_name i =
        sprintf "_sedlex_st_%d" i

    let remember_table (table: int array) =
        match Map.tryFind table tables with
        | Some n -> n
        | None ->
            table
            |> Seq.map (string >> word)
            |> List.ofSeq
            |> seplist (word ", ")
            |> fun table_doc ->
            let n = new_tbl_name()
            push_later_toplevel <| word "const" + word n + word "=" + bracket table_doc
            tables <- Map.add table n tables
            n

    let rec _cg_decision_func tree: Doc =
            match tree with
            | Lte(i, yes, no) ->
                let yes_f = _cg_decision_func yes
                let no_f = _cg_decision_func no
                vsep [
                    word "if" + word "c" + word "<=" + word (string i);
                        yes_f >>> 4;
                    word "else";
                        no_f >>> 4;
                    word "end"
                ]
            | Return i -> word "return" + word (string i)
            | Table(offset, t) ->
                let tname = remember_table t
                word "return" + word tname * word "[" * word "c" + word "-" + pretty offset + word "+ 1" * word "]" + word "-" + pretty 1

    let cg_decision_func tree =
        match Map.tryFind tree decision_funcs with
        | Some name -> name
        | None ->
        let dtname = new_dt_name()
        let define =
            vsep [
                word "function" + word dtname * parens (word "c::Int32");
                _cg_decision_func tree >>> 4
                word "end"
            ]
        push_toplevel define
        decision_funcs <- Map.add tree dtname decision_funcs
        dtname

    let rec _cg_state_func (lang: lang): Doc =
        match lang with
        | Lang_backtrace -> word "result = sedlex_backtrack(lexerbuf)"
        | Lang_callst i ->
            word "result" + word "=" + word (st_func_name i) * parens (word "lexerbuf")
        | Lang_int i -> word "result" + word "=" + word "Int32" * parens(  pretty i )
        | Lang_mark(i, lang) ->
            vsep [
                word <| sprintf "sedlex_mark(lexerbuf, %d)" i;
                _cg_state_func lang;
            ]
        | Lang_match_i(dt, cases, default_case) ->
            let mutable names = []
            for each in cases do
                let body = _cg_state_func each
                let name = new_rnd_name()
                push_toplevel <|
                    vsep [
                        word "function" + word name * parens (word "lexerbuf::lexbuf");
                        vsep [
                            word "result = Int32(-1)"
                            body;
                            word "return result"
                        ] >>> 4
                        word "end"
                    ]
                names <- name :: names
            let names = List.rev names
            let func_table = new_rnd_name()
            push_later_toplevel <|
                word "const" + word func_table + word "=" + parens (seplist (word ", ") (List.map word names) * word ",")
            let default_body = _cg_state_func default_case
            let decision_func = (cg_decision_func dt)
            let test =  word decision_func * parens (word "sedlex_next_int(lexerbuf)")
            vsep [
                word "state_id" + word "="  + test;
                word "if" + word (sprintf "state_id >= 0");
                vsep [
                    word "result" + word "=" + word (sprintf "sedlex_call_state(%s, state_id, lexerbuf)" func_table)
                ] >>> 4;
                word "else";
                    default_body >>> 4;
                word "end";
            ]

    let cg_state_func i lang =
        vsep [
            word "function" + word (st_func_name i) * parens(word "lexerbuf::lexbuf")
            vsep [
                word "result = Int32(-1)" // not -1~MAXCODE could be fine
                _cg_state_func lang
                word "return result"
            ] >>> 4
            word "end"
        ]
        |> fun define ->
        push_toplevel define

    let compile_lexer() =
        let lex_code, error_msg = cu.lex_code
        let error_msg = "\"" + error_msg.Replace("\"", "\\\"") + "\""
        let initial_state_fun = st_func_name 0
        let token_ids = Array.toList <|
                            Array.map
                                (function | Discard -> word "nothing"
                                          | Tokenize (i: token_id) -> word "Int32" * parens(pretty i))
                                lex_code
        let construct_table = word "["  + seplist (word ", ") token_ids +  word "]" + word " # token_ids"
        
        let table_name = new_rnd_name()
        push_toplevel (word "const" + word table_name + word "=" + construct_table)

        vsep [
            empty;
            word "struct Token";
            vsep [
                word "token_id::Int32";
                word "lexeme::String";
                word "line::Int32"
                word "col::Int32"
                word "span::Int32"
                word "offset::Int32"
                word "file::String"
                word "Token(token_id, src, line, col, span, offset, file) = new(token_id, sedlex_lexeme(src), line, col, span, offset, file)"
            ] >>> 4
            word "end"
            empty;
            word "function" + word "lex" * parens(word "construct_token" * word ", " + word "lexerbuf::lexbuf")
            vsep [
                word "sedlex_start(lexerbuf)";
                word "case_id" + word "=" + word initial_state_fun * parens (word "lexerbuf")
                word "case_id < 0" + word "&&" + word "error" * parens  (seg error_msg);
                word "token_id"  + word "=" + word table_name * word "[" * word "case_id" + word "+ 1" * word "]"
                word "token_id == nothing" + word "&&" + word "return nothing";
                word "return" + word "construct_token" * parens ( seplist (word ", ") [
                    word "token_id";
                    word "lexerbuf";
                    word "lexerbuf.start_line";
                    word "lexerbuf.pos - lexerbuf.curr_bol";
                    word "lexerbuf.pos - lexerbuf.start_pos";
                    word "lexerbuf.start_pos"
                    word "lexerbuf.filename"
                ])
            ] >>> 4;
            word "end";
            empty;
            word "function lexall(construct_token, buf::lexbuf, is_eof #= Token -> Bool =#)";
            vsep [
                word "Channel() do coro"
                vsep [
                    word "while true";
                    vsep [
                        word "token = lex(construct_token, buf)";
                        word "token === nothing && continue";
                        word "is_eof(token) && break";
                        word "put!(coro, token)";
                    ] >>> 4
                    word "end"
                ] >>> 4
                word "end"
            ] >>> 4
            word "end";
        ]

    
    for kv in cu.states do
        cg_state_func kv.Key kv.Value

    for dt in cu.referenced_decision_trees do
        ignore(cg_decision_func dt)
    
    
    let middle_toplevels = compile_lexer()
    vsep <|
        [
            seg import_head
        ] @
        toplevels @
        [middle_toplevels] @
        later_toplevels

