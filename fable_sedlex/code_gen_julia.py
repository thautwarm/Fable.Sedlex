from __future__ import annotations
from typing import (Any, Callable, Optional, Tuple)
from .fable_modules.fable_library.array import (compare_with, map as map_2)
from .fable_modules.fable_library.list import (empty as empty_1, FSharpList, of_array_with_tail, of_seq, of_array, cons, reverse, map as map_1, singleton, append)
from .fable_modules.fable_library.map import (empty, try_find, add)
from .fable_modules.fable_library.seq import map
from .fable_modules.fable_library.string import (to_text, printf, replace)
from .fable_modules.fable_library.types import Array
from .fable_modules.fable_library.util import (compare, compare_primitives, int32_to_string, get_enumerator, ignore)
from .pretty_doc import (Doc, empty as empty_2, word, seplist, Doc_op_Addition_Z492644C0, bracket, Doc_op_Multiply_Z492644C0, pretty, vsep, Doc_op_RightShift_1E15AFA6, parens, seg)
from .sedlex import (compiled_unit, Automata_decision_tree, lang as lang_3, keep_token)

def codegen_julia(import_head: str, cu: compiled_unit) -> Doc:
    class ObjectExpr3:
        @property
        def Compare(self) -> Any:
            def arrow_2(x: Automata_decision_tree, y: Automata_decision_tree) -> int:
                return compare(x, y)

            return arrow_2

    decision_funcs : Any = empty(ObjectExpr3())
    tbl_cnt : int = 0
    def new_tbl_name(import_head: str=import_head, cu: compiled_unit=cu) -> str:
        nonlocal tbl_cnt
        tbl_cnt = (tbl_cnt + 1) or 0
        arg : int = tbl_cnt or 0
        return to_text(printf("_sedlex_DT_table_%d"))(arg)

    dt_cnt : int = 0
    def new_dt_name(import_head: str=import_head, cu: compiled_unit=cu) -> str:
        nonlocal dt_cnt
        dt_cnt = (dt_cnt + 1) or 0
        arg_1 : int = dt_cnt or 0
        return to_text(printf("_sedlex_decide_%d"))(arg_1)

    rnd_cnt : int = 0
    def new_rnd_name(import_head: str=import_head, cu: compiled_unit=cu) -> str:
        nonlocal rnd_cnt
        rnd_cnt = (rnd_cnt + 1) or 0
        arg_2 : int = rnd_cnt or 0
        return to_text(printf("_sedlex_rnd_%d"))(arg_2)

    class ObjectExpr11:
        @property
        def Compare(self) -> Any:
            def arrow_10(x_1: Array[int], y_1: Array[int]) -> int:
                def arrow_7(x_2: int, y_2: int) -> int:
                    return compare_primitives(x_2, y_2)

                return compare_with(arrow_7, x_1, y_1)

            return arrow_10

    tables : Any = empty(ObjectExpr11())
    toplevels : FSharpList[Doc] = empty_1()
    later_toplevels : FSharpList[Doc] = empty_1()
    def push_toplevel(doc: Doc, import_head: str=import_head, cu: compiled_unit=cu) -> None:
        nonlocal toplevels
        toplevels = of_array_with_tail([doc, empty_2], toplevels)

    def push_later_toplevel(doc_1: Doc, import_head: str=import_head, cu: compiled_unit=cu) -> None:
        nonlocal later_toplevels
        later_toplevels = of_array_with_tail([doc_1, empty_2], later_toplevels)

    def st_func_name(i: int, import_head: str=import_head, cu: compiled_unit=cu) -> str:
        return to_text(printf("_sedlex_st_%d"))(i)

    def remember_table(table: Array[int], import_head: str=import_head, cu: compiled_unit=cu) -> str:
        nonlocal tables
        match_value : Optional[str] = try_find(table, tables)
        if match_value is None:
            table_doc : Doc
            def mapping(arg_4: int, table: Array[int]=table) -> Doc:
                return word(int32_to_string(arg_4))

            lst : FSharpList[Doc] = of_seq(map(mapping, table))
            table_doc = seplist(word(", "), lst)
            n_1 : str = new_tbl_name()
            push_later_toplevel(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("const"), word(n_1)), word("=")), bracket(table_doc)))
            tables = add(table, n_1, tables)
            return n_1

        else: 
            return match_value


    def _cg_decision_func(tree: Automata_decision_tree, import_head: str=import_head, cu: compiled_unit=cu) -> Doc:
        if tree.tag == 2:
            return Doc_op_Addition_Z492644C0(word("return"), word(int32_to_string(tree.fields[0])))

        elif tree.tag == 1:
            tname : str = remember_table(tree.fields[1])
            return Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("return"), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word(tname), word("[")), word("c"))), word("-")), pretty(tree.fields[0])), Doc_op_Multiply_Z492644C0(word("+ 1"), word("]"))), word("-")), pretty(1))

        else: 
            yes_f : Doc = _cg_decision_func(tree.fields[1])
            no_f : Doc = _cg_decision_func(tree.fields[2])
            return vsep(of_array([Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("if"), word("c")), word("<=")), word(int32_to_string(tree.fields[0]))), Doc_op_RightShift_1E15AFA6(yes_f, 4), word("else"), Doc_op_RightShift_1E15AFA6(no_f, 4), word("end")]))


    def cg_decision_func(tree_1: Automata_decision_tree, import_head: str=import_head, cu: compiled_unit=cu) -> str:
        nonlocal decision_funcs
        match_value_1 : Optional[str] = try_find(tree_1, decision_funcs)
        if match_value_1 is None:
            dtname : str = new_dt_name()
            push_toplevel(vsep(of_array([Doc_op_Addition_Z492644C0(word("function"), Doc_op_Multiply_Z492644C0(word(dtname), parens(word("c::Int32")))), Doc_op_RightShift_1E15AFA6(_cg_decision_func(tree_1), 4), word("end")])))
            decision_funcs = add(tree_1, dtname, decision_funcs)
            return dtname

        else: 
            return match_value_1


    def _cg_state_func(lang: lang_3, import_head: str=import_head, cu: compiled_unit=cu) -> Doc:
        if lang.tag == 3:
            return Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("result"), word("=")), Doc_op_Multiply_Z492644C0(word(st_func_name(lang.fields[0])), parens(word("lexerbuf"))))

        elif lang.tag == 4:
            return Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("result"), word("=")), Doc_op_Multiply_Z492644C0(word("Int32"), parens(pretty(lang.fields[0]))))

        elif lang.tag == 2:
            return vsep(of_array([word(to_text(printf("sedlex_mark(lexerbuf, %d)"))(lang.fields[0])), _cg_state_func(lang.fields[1])]))

        elif lang.tag == 0:
            cases : Array[lang_3] = lang.fields[1]
            names : FSharpList[str] = empty_1()
            for idx in range(0, (len(cases) - 1) + 1, 1):
                body : Doc = _cg_state_func(cases[idx])
                name_1 : str = new_rnd_name()
                push_toplevel(vsep(of_array([Doc_op_Addition_Z492644C0(word("function"), Doc_op_Multiply_Z492644C0(word(name_1), parens(word("lexerbuf::lexbuf")))), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("result = Int32(-1)"), body, word("return result")])), 4), word("end")])))
                names = cons(name_1, names)
            names_1 : FSharpList[str] = reverse(names)
            func_table : str = new_rnd_name()
            def arrow_15(s_2: str, lang: lang_3=lang) -> Doc:
                return word(s_2)

            push_later_toplevel(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("const"), word(func_table)), word("=")), parens(Doc_op_Multiply_Z492644C0(seplist(word(", "), map_1(arrow_15, names_1)), word(",")))))
            default_body : Doc = _cg_state_func(lang.fields[2])
            test : Doc = Doc_op_Multiply_Z492644C0(word(cg_decision_func(lang.fields[0])), parens(word("sedlex_next_int(lexerbuf)")))
            return vsep(of_array([Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("state_id"), word("=")), test), Doc_op_Addition_Z492644C0(word("if"), word(to_text(printf("state_id >= 0")))), Doc_op_RightShift_1E15AFA6(vsep(singleton(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("result"), word("=")), word(to_text(printf("sedlex_call_state(%s, state_id, lexerbuf)"))(func_table))))), 4), word("else"), Doc_op_RightShift_1E15AFA6(default_body, 4), word("end")]))

        else: 
            return word("result = sedlex_backtrack(lexerbuf)")


    def cg_state_func(i_6: int, lang_2: lang_3, import_head: str=import_head, cu: compiled_unit=cu) -> None:
        push_toplevel(vsep(of_array([Doc_op_Addition_Z492644C0(word("function"), Doc_op_Multiply_Z492644C0(word(st_func_name(i_6)), parens(word("lexerbuf::lexbuf")))), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("result = Int32(-1)"), _cg_state_func(lang_2), word("return result")])), 4), word("end")])))

    def compile_lexer(import_head: str=import_head, cu: compiled_unit=cu) -> Doc:
        pattern_input : Tuple[Array[keep_token], str] = cu.lex_code
        error_msg_1 : str = ("\"" + replace(pattern_input[1], "\"", "\\\"")) + "\""
        initial_state_fun : str = st_func_name(0)
        def arrow_18(_arg: keep_token) -> Doc:
            return Doc_op_Multiply_Z492644C0(word("Int32"), parens(pretty(_arg.fields[0]))) if (_arg.tag == 1) else word("nothing")

        token_ids : FSharpList[Doc] = of_array(map_2(arrow_18, pattern_input[0], None))
        construct_table : Doc = Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("["), seplist(word(", "), token_ids)), word("]")), word(" # token_ids"))
        table_name : str = new_rnd_name()
        push_toplevel(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("const"), word(table_name)), word("=")), construct_table))
        return vsep(of_array([empty_2, word("struct Token"), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("token_id::Int32"), word("lexeme::String"), word("line::Int32"), word("col::Int32"), word("span::Int32"), word("offset::Int32"), word("file::String"), word("Token(token_id, src, line, col, span, offset, file) = new(token_id, sedlex_lexeme(src), line, col, span, offset, file)")])), 4), word("end"), empty_2, Doc_op_Addition_Z492644C0(word("function"), Doc_op_Multiply_Z492644C0(word("lex"), parens(Doc_op_Addition_Z492644C0(Doc_op_Multiply_Z492644C0(word("construct_token"), word(", ")), word("lexerbuf::lexbuf"))))), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("sedlex_start(lexerbuf)"), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("case_id"), word("=")), Doc_op_Multiply_Z492644C0(word(initial_state_fun), parens(word("lexerbuf")))), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("case_id < 0"), word("&&")), Doc_op_Multiply_Z492644C0(word("error"), parens(seg(error_msg_1)))), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("token_id"), word("=")), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word(table_name), word("[")), word("case_id"))), Doc_op_Multiply_Z492644C0(word("+ 1"), word("]"))), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("token_id == nothing"), word("&&")), word("return nothing")), Doc_op_Addition_Z492644C0(word("return"), Doc_op_Multiply_Z492644C0(word("construct_token"), parens(seplist(word(", "), of_array([word("token_id"), word("lexerbuf"), word("lexerbuf.start_line"), word("lexerbuf.pos - lexerbuf.curr_bol"), word("lexerbuf.pos - lexerbuf.start_pos"), word("lexerbuf.start_pos"), word("lexerbuf.filename")])))))])), 4), word("end"), empty_2, word("function lexall(construct_token, buf::lexbuf, is_eof #= Token -> Bool =#)"), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("Channel() do coro"), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("while true"), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("token = lex(construct_token, buf)"), word("token === nothing && continue"), word("is_eof(token) && break"), word("put!(coro, token)")])), 4), word("end")])), 4), word("end")])), 4), word("end")]))

    with get_enumerator(cu.states) as enumerator:
        while enumerator.System_Collections_IEnumerator_MoveNext():
            kv : Any = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
            cg_state_func(kv[0], kv[1])
    with get_enumerator(cu.referenced_decision_trees) as enumerator_1:
        while enumerator_1.System_Collections_IEnumerator_MoveNext():
            ignore(cg_decision_func(enumerator_1.System_Collections_Generic_IEnumerator_00601_get_Current()))
    middle_toplevels : Doc = compile_lexer()
    return vsep(append(singleton(seg(import_head)), append(toplevels, append(singleton(middle_toplevels), later_toplevels))))


