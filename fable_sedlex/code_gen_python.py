from __future__ import annotations
from array import array as array_1
from typing import (Any, Optional, List, Tuple)
from fable_modules.fable_library.array import (compare_with, map as map_2)
from fable_modules.fable_library.list import (empty as empty_1, append, singleton, of_array_with_tail, of_seq, FSharpList, of_array, cons, reverse, map as map_1)
from fable_modules.fable_library.map import (empty, try_find, add)
from fable_modules.fable_library.reflection import (TypeInfo, class_type)
from fable_modules.fable_library.seq import map
from fable_modules.fable_library.string import (to_text, printf, replace)
from fable_modules.fable_library.util import (compare, compare_primitives, get_enumerator, ignore, int32_to_string)
from .code_gen import (Doc, vsep, empty as empty_2, word, seplist, Doc_op_Addition_Z7CFFAC00, bracket, Doc_op_Multiply_Z7CFFAC00, pretty, Doc_op_RightShift_2AAA0F3C, parens)
from .sedlex import (Automata_decision_tree, compiled_unit, lang as lang_2, keep_token)

def expr_7() -> TypeInfo:
    return class_type("Fable.Sedlex.CodeGen.Python.CodeGenerator", None, CodeGenerator)


class CodeGenerator:
    def __init__(self, cu: compiled_unit=None) -> None:
        self.cu = cu
        class ObjectExpr5:
            @property
            def Compare(self) -> Any:
                return lambda x, y: compare(x, y)
            
        self.decision_funcs = empty(ObjectExpr5())
        self.tbl_cnt = 0
        self.dt_cnt = 0
        self.rnd_cnt = 0
        class ObjectExpr6:
            @property
            def Compare(self) -> Any:
                return lambda x_1, y_1: compare_with(lambda x_2, y_2: compare_primitives(x_2, y_2), x_1, y_1)
            
        self.tables = empty(ObjectExpr6())
        self.toplevels = empty_1()
        self.later_toplevels = empty_1()
    

CodeGenerator_reflection = expr_7

def CodeGenerator__ctor_24D518AB(cu: compiled_unit) -> CodeGenerator:
    return CodeGenerator(cu)


def CodeGenerator__CodeGenDoc(__: CodeGenerator) -> Doc:
    with get_enumerator(__.cu.states) as enumerator:
        while enumerator.System_Collections_IEnumerator_MoveNext():
            kv : Any = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
            CodeGenerator__cg_state_func(__, kv[0], kv[1])
    with get_enumerator(__.cu.referenced_decision_trees) as enumerator_1:
        while enumerator_1.System_Collections_IEnumerator_MoveNext():
            ignore(CodeGenerator__cg_decision_func_71482736(__, enumerator_1.System_Collections_Generic_IEnumerator_00601_get_Current()))
    middle_toplevels : Doc = CodeGenerator__compile_lexer(__)
    return vsep(append(__.toplevels, append(singleton(middle_toplevels), __.later_toplevels)))


def CodeGenerator__new_tbl_name(this: CodeGenerator) -> str:
    this.tbl_cnt = (this.tbl_cnt + 1) or 0
    arg10 : int = this.tbl_cnt or 0
    return to_text(printf("_sedlex_DT_table_%d"))(arg10)


def CodeGenerator__new_dt_name(this: CodeGenerator) -> str:
    this.dt_cnt = (this.dt_cnt + 1) or 0
    arg10 : int = this.dt_cnt or 0
    return to_text(printf("_sedlex_decide_%d"))(arg10)


def CodeGenerator__new_rnd_name(this: CodeGenerator) -> str:
    this.rnd_cnt = (this.rnd_cnt + 1) or 0
    arg10 : int = this.rnd_cnt or 0
    return to_text(printf("_sedlex_rnd_%d"))(arg10)


def CodeGenerator__push_toplevel_417FD60(this: CodeGenerator, doc: Doc) -> None:
    this.toplevels = of_array_with_tail([doc, empty_2], this.toplevels)


def CodeGenerator__push_later_toplevel_417FD60(this: CodeGenerator, doc: Doc) -> None:
    this.later_toplevels = of_array_with_tail([doc, empty_2], this.later_toplevels)


def CodeGenerator__st_func_name_Z524259A4(this: CodeGenerator, i: int) -> str:
    return to_text(printf("_sedlex_st_%d"))(i)


def CodeGenerator__remember_table_13C0A23A(this: CodeGenerator, table: array_1) -> str:
    match_value : Optional[str] = try_find(table, this.tables)
    if match_value is None:
        table_doc = None
        lst : FSharpList[Doc] = of_seq(map(lambda arg, this=this, table=table: word(int32_to_string(arg)), table))
        table_doc = seplist(word(", "), lst)
        n_1 : str = CodeGenerator__new_tbl_name(this)
        CodeGenerator__push_later_toplevel_417FD60(this, Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word(n_1), word("=")), bracket(table_doc)))
        this.tables = add(table, n_1, this.tables)
        return n_1
    
    else: 
        return match_value
    


def CodeGenerator___cg_decision_func_71482736(this: CodeGenerator, tree: Automata_decision_tree) -> Doc:
    if tree.tag == 2:
        return Doc_op_Addition_Z7CFFAC00(word("return"), word(int32_to_string(tree.fields[0])))
    
    elif tree.tag == 1:
        tname : str = CodeGenerator__remember_table_13C0A23A(this, tree.fields[1])
        return Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("return"), Doc_op_Multiply_Z7CFFAC00(Doc_op_Multiply_Z7CFFAC00(word(tname), word("[")), word("c"))), word("-")), Doc_op_Multiply_Z7CFFAC00(pretty(tree.fields[0]), word("]"))), word("-")), pretty(1))
    
    else: 
        yes_f : Doc = CodeGenerator___cg_decision_func_71482736(this, tree.fields[1])
        no_f : Doc = CodeGenerator___cg_decision_func_71482736(this, tree.fields[2])
        return vsep(of_array([Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("if"), word("c")), word("\u003c=")), Doc_op_Multiply_Z7CFFAC00(word(int32_to_string(tree.fields[0])), word(":"))), Doc_op_RightShift_2AAA0F3C(yes_f, 4), word("else:"), Doc_op_RightShift_2AAA0F3C(no_f, 4)]))
    


def CodeGenerator__cg_decision_func_71482736(this: CodeGenerator, tree: Automata_decision_tree) -> str:
    match_value : Optional[str] = try_find(tree, this.decision_funcs)
    if match_value is None:
        dtname : str = CodeGenerator__new_dt_name(this)
        CodeGenerator__push_toplevel_417FD60(this, vsep(of_array([Doc_op_Addition_Z7CFFAC00(word("def"), Doc_op_Multiply_Z7CFFAC00(Doc_op_Multiply_Z7CFFAC00(word(dtname), parens(word("c: int"))), word(":"))), Doc_op_RightShift_2AAA0F3C(CodeGenerator___cg_decision_func_71482736(this, tree), 4)])))
        this.decision_funcs = add(tree, dtname, this.decision_funcs)
        return dtname
    
    else: 
        return match_value
    


def CodeGenerator___cg_state_func_Z11073E1D(this: CodeGenerator, lang: lang_2) -> Doc:
    if lang.tag == 3:
        return Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("result"), word("=")), Doc_op_Multiply_Z7CFFAC00(word(CodeGenerator__st_func_name_Z524259A4(this, lang.fields[0])), parens(word("lexerbuf"))))
    
    elif lang.tag == 4:
        return Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("result"), word("=")), pretty(lang.fields[0]))
    
    elif lang.tag == 2:
        return vsep(of_array([word(to_text(printf("mark(lexerbuf, %d)"))(lang.fields[0])), CodeGenerator___cg_state_func_Z11073E1D(this, lang.fields[1])]))
    
    elif lang.tag == 0:
        cases : List[lang_2] = lang.fields[1]
        names : FSharpList[str] = empty_1()
        for idx in range(0, (len(cases) - 1) + 1, 1):
            body : Doc = CodeGenerator___cg_state_func_Z11073E1D(this, cases[idx])
            name : str = CodeGenerator__new_rnd_name(this)
            CodeGenerator__push_toplevel_417FD60(this, vsep(of_array([Doc_op_Addition_Z7CFFAC00(word("def"), Doc_op_Multiply_Z7CFFAC00(Doc_op_Multiply_Z7CFFAC00(word(name), parens(word("lexerbuf: lexbuf"))), word(":"))), Doc_op_RightShift_2AAA0F3C(vsep(of_array([word("result = -1"), body, word("return result")])), 4)])))
            names = cons(name, names)
        names_1 : FSharpList[str] = reverse(names)
        func_table : str = CodeGenerator__new_rnd_name(this)
        def arrow_8(this=this, lang=lang) -> Doc:
            lst : FSharpList[Doc] = map_1(lambda s_1: word(s_1), names_1)
            return seplist(word(", "), lst)
        
        CodeGenerator__push_later_toplevel_417FD60(this, Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word(func_table), word("=")), bracket(arrow_8())))
        default_body : Doc = CodeGenerator___cg_state_func_Z11073E1D(this, lang.fields[2])
        test : Doc = Doc_op_Multiply_Z7CFFAC00(word(CodeGenerator__cg_decision_func_71482736(this, lang.fields[0])), parens(word("public_next_int(lexerbuf)")))
        return vsep(of_array([Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("state_id"), word("=")), test), Doc_op_Addition_Z7CFFAC00(word("if"), Doc_op_Multiply_Z7CFFAC00(word(to_text(printf("state_id \u003e= 0"))), word(":"))), Doc_op_RightShift_2AAA0F3C(vsep(singleton(Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("result"), word("=")), Doc_op_Multiply_Z7CFFAC00(word(to_text(printf("%s[state_id]"))(func_table)), parens(word("lexerbuf")))))), 4), word("else:"), Doc_op_RightShift_2AAA0F3C(default_body, 4)]))
    
    else: 
        return word("result = backtrack(lexerbuf)")
    


def CodeGenerator__cg_state_func(this: CodeGenerator, i: int, lang: lang_2) -> None:
    CodeGenerator__push_toplevel_417FD60(this, vsep(of_array([Doc_op_Addition_Z7CFFAC00(word("def"), Doc_op_Multiply_Z7CFFAC00(Doc_op_Multiply_Z7CFFAC00(word(CodeGenerator__st_func_name_Z524259A4(this, i)), parens(word("lexerbuf: lexbuf"))), word(":"))), Doc_op_RightShift_2AAA0F3C(vsep(of_array([word("result = -1"), CodeGenerator___cg_state_func_Z11073E1D(this, lang), word("return result")])), 4)])))


def CodeGenerator__compile_lexer(this: CodeGenerator) -> Doc:
    pattern_input : Tuple[List[keep_token], str] = this.cu.lex_code
    error_msg_1 : str = ("\"" + replace(pattern_input[1], "\"", "\\\"")) + "\""
    initial_state_fun : str = CodeGenerator__st_func_name_Z524259A4(this, 0)
    token_ids : FSharpList[Doc] = of_array(map_2(lambda _arg1, this=this: pretty(_arg1.fields[0]) if (_arg1.tag == 1) else (word("None")), pattern_input[0], None))
    construct_table : Doc = Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("["), seplist(word(", "), token_ids)), word("]")), word(" # token_ids"))
    table_name : str = CodeGenerator__new_rnd_name(this)
    CodeGenerator__push_toplevel_417FD60(this, Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word(table_name), word("=")), construct_table))
    return vsep(of_array([Doc_op_Addition_Z7CFFAC00(word("def"), Doc_op_Multiply_Z7CFFAC00(Doc_op_Multiply_Z7CFFAC00(word("lex"), parens(word("lexerbuf: lexbuf"))), word(":"))), Doc_op_RightShift_2AAA0F3C(vsep(of_array([word("start(lexerbuf)"), Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("case_id"), word("=")), Doc_op_Multiply_Z7CFFAC00(word(initial_state_fun), parens(word("lexerbuf")))), Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("if case_id \u003c 0:"), word("raise")), Doc_op_Multiply_Z7CFFAC00(word("Exception"), parens(word(error_msg_1)))), Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("token_id"), word("=")), Doc_op_Multiply_Z7CFFAC00(Doc_op_Multiply_Z7CFFAC00(Doc_op_Multiply_Z7CFFAC00(word(table_name), word("[")), word("case_id")), word("]"))), word("if token_id is not None:"), Doc_op_RightShift_2AAA0F3C(vsep(singleton(Doc_op_Addition_Z7CFFAC00(word("return"), Doc_op_Multiply_Z7CFFAC00(word("token"), parens(seplist(word(", "), of_array([word("token_id"), word("lexeme(lexerbuf)"), word("lexerbuf.start_line"), word("lexerbuf.pos - lexerbuf.curr_bol"), word("lexerbuf.pos - lexerbuf.start_pos"), word("lexerbuf.start_pos"), word("lexerbuf.filename")]))))))), 4), word("return None")])), 4)]))


def codegen_python(cu: compiled_unit) -> Doc:
    return CodeGenerator__CodeGenDoc(CodeGenerator__ctor_24D518AB(cu))


