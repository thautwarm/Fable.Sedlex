module Main

open Fable.Sedlex.Compiler
open Fable.CodeGen

type MyToken = {
    s_tokenId: token_id;
    s_lexeme : string ;
    s_line: int;
    s_col: int;
    s_span: int;
    s_offset: int;
    s_file: string 
} with
    interface token with
        member this.col: int = this.s_col
        member this.file: string = this.s_file
        member this.lexeme: string = this.s_lexeme
        member this.line: int = this.s_line
        member this.offset: int = this.s_offset
        member this.span: int = this.s_span
        member __.tokenId = __.s_tokenId

let create_my_token (token_id, lexeme, line, col, span, offset, file): token =
    {  s_tokenId = token_id ;
       s_lexeme = lexeme;
       s_line = line;
       s_col = col;
       s_span = span;
       s_offset = offset;
       s_file = file }


[<EntryPoint>]
let main _ =
    let cu = build [|(pstring "123",  Lexer_tokenize 2 )|] "error msg"
    let parse = inline_thread cu create_my_token
    let buf = from_ustring "123"
    printfn "%A" <| parse buf
    
    let doc = 
        word "class" + vsep [
            word "def";
            vsep [
                word "123"
                word "var" + word "x" + word "=" + word "z" * word ";"
            ] >>> 3
        ] >>> 2

    printfn "%s" (showDoc doc)
    0
