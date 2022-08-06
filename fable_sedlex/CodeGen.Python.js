import { add, tryFind, empty } from "./fable_modules/fable-library.3.7.6/Map.js";
import { replace, printf, toText } from "./fable_modules/fable-library.3.7.6/String.js";
import { append, singleton, map as map_1, reverse, cons, ofArray, ofSeq, ofArrayWithTail, empty as empty_1 } from "./fable_modules/fable-library.3.7.6/List.js";
import { parens, Doc_op_RightShift_1E15AFA6, vsep, pretty, Doc_op_Multiply_Z492644C0, bracket, seplist, word, Doc_op_Addition_Z492644C0, empty as empty_2 } from "./PrettyDoc.js";
import { disposeSafe, getEnumerator, int32ToString } from "./fable_modules/fable-library.3.7.6/Util.js";
import { map } from "./fable_modules/fable-library.3.7.6/Seq.js";
import { map as map_2 } from "./fable_modules/fable-library.3.7.6/Array.js";

export function codegen_python(import_head, cu) {
    let decision_funcs = empty();
    let tbl_cnt = 0;
    let dt_cnt = 0;
    let rnd_cnt = 0;
    const new_rnd_name = () => {
        rnd_cnt = ((rnd_cnt + 1) | 0);
        const arg10_2 = rnd_cnt | 0;
        return toText(printf("_sedlex_rnd_%d"))(arg10_2);
    };
    let tables = empty();
    let toplevels = empty_1();
    let later_toplevels = empty_1();
    const push_toplevel = (doc) => {
        toplevels = ofArrayWithTail([doc, empty_2], toplevels);
    };
    const push_later_toplevel = (doc_1) => {
        later_toplevels = ofArrayWithTail([doc_1, empty_2], later_toplevels);
    };
    const st_func_name = (i) => toText(printf("_sedlex_st_%d"))(i);
    const _cg_decision_func = (tree) => {
        switch (tree.tag) {
            case 2: {
                return Doc_op_Addition_Z492644C0(word("return"), word(int32ToString(tree.fields[0])));
            }
            case 1: {
                let tname;
                const table = tree.fields[1];
                const matchValue = tryFind(table, tables);
                if (matchValue == null) {
                    let table_doc;
                    const lst = ofSeq(map((arg) => word(int32ToString(arg)), table));
                    table_doc = seplist(word(", "), lst);
                    let n_1;
                    tbl_cnt = ((tbl_cnt + 1) | 0);
                    const arg10 = tbl_cnt | 0;
                    n_1 = toText(printf("_sedlex_DT_table_%d"))(arg10);
                    push_later_toplevel(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word(n_1), word("=")), bracket(table_doc)));
                    tables = add(table, n_1, tables);
                    tname = n_1;
                }
                else {
                    tname = matchValue;
                }
                return Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("return"), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word(tname), word("[")), word("c"))), word("-")), Doc_op_Multiply_Z492644C0(pretty(tree.fields[0]), word("]"))), word("-")), pretty(1));
            }
            default: {
                const yes_f = _cg_decision_func(tree.fields[1]);
                const no_f = _cg_decision_func(tree.fields[2]);
                return vsep(ofArray([Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("if"), word("c")), word("\u003c=")), Doc_op_Multiply_Z492644C0(word(int32ToString(tree.fields[0])), word(":"))), Doc_op_RightShift_1E15AFA6(yes_f, 4), word("else:"), Doc_op_RightShift_1E15AFA6(no_f, 4)]));
            }
        }
    };
    const cg_decision_func = (tree_1) => {
        const matchValue_1 = tryFind(tree_1, decision_funcs);
        if (matchValue_1 == null) {
            let dtname;
            dt_cnt = ((dt_cnt + 1) | 0);
            const arg10_1 = dt_cnt | 0;
            dtname = toText(printf("_sedlex_decide_%d"))(arg10_1);
            push_toplevel(vsep(ofArray([Doc_op_Addition_Z492644C0(word("def"), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word(dtname), parens(word("c: int"))), word(":"))), Doc_op_RightShift_1E15AFA6(_cg_decision_func(tree_1), 4)])));
            decision_funcs = add(tree_1, dtname, decision_funcs);
            return dtname;
        }
        else {
            return matchValue_1;
        }
    };
    const _cg_state_func = (lang) => {
        let lst_1;
        switch (lang.tag) {
            case 3: {
                return Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("result"), word("=")), Doc_op_Multiply_Z492644C0(word(st_func_name(lang.fields[0])), parens(word("lexerbuf"))));
            }
            case 4: {
                return Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("result"), word("=")), pretty(lang.fields[0]));
            }
            case 2: {
                return vsep(ofArray([word(toText(printf("mark(lexerbuf, %d)"))(lang.fields[0])), _cg_state_func(lang.fields[1])]));
            }
            case 0: {
                const cases = lang.fields[1];
                let names = empty_1();
                for (let idx = 0; idx <= (cases.length - 1); idx++) {
                    const body = _cg_state_func(cases[idx]);
                    const name_1 = new_rnd_name();
                    push_toplevel(vsep(ofArray([Doc_op_Addition_Z492644C0(word("def"), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word(name_1), parens(word("lexerbuf: lexbuf"))), word(":"))), Doc_op_RightShift_1E15AFA6(vsep(ofArray([word("result = -1"), body, word("return result")])), 4)])));
                    names = cons(name_1, names);
                }
                const names_1 = reverse(names);
                const func_table = new_rnd_name();
                push_later_toplevel(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word(func_table), word("=")), bracket((lst_1 = map_1(word, names_1), seplist(word(", "), lst_1)))));
                const default_body = _cg_state_func(lang.fields[2]);
                const test = Doc_op_Multiply_Z492644C0(word(cg_decision_func(lang.fields[0])), parens(word("public_next_int(lexerbuf)")));
                return vsep(ofArray([Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("state_id"), word("=")), test), Doc_op_Addition_Z492644C0(word("if"), Doc_op_Multiply_Z492644C0(word(toText(printf("state_id \u003e= 0"))), word(":"))), Doc_op_RightShift_1E15AFA6(vsep(singleton(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("result"), word("=")), Doc_op_Multiply_Z492644C0(word(toText(printf("%s[state_id]"))(func_table)), parens(word("lexerbuf")))))), 4), word("else:"), Doc_op_RightShift_1E15AFA6(default_body, 4)]));
            }
            default: {
                return word("result = backtrack(lexerbuf)");
            }
        }
    };
    const enumerator = getEnumerator(cu.states);
    try {
        while (enumerator["System.Collections.IEnumerator.MoveNext"]()) {
            const kv = enumerator["System.Collections.Generic.IEnumerator`1.get_Current"]();
            push_toplevel(vsep(ofArray([Doc_op_Addition_Z492644C0(word("def"), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word(st_func_name(kv[0])), parens(word("lexerbuf: lexbuf"))), word(":"))), Doc_op_RightShift_1E15AFA6(vsep(ofArray([word("result = -1"), _cg_state_func(kv[1]), word("return result")])), 4)])));
        }
    }
    finally {
        disposeSafe(enumerator);
    }
    const enumerator_1 = getEnumerator(cu.referenced_decision_trees);
    try {
        while (enumerator_1["System.Collections.IEnumerator.MoveNext"]()) {
            cg_decision_func(enumerator_1["System.Collections.Generic.IEnumerator`1.get_Current"]());
        }
    }
    finally {
        disposeSafe(enumerator_1);
    }
    let middle_toplevels;
    const patternInput = cu.lex_code;
    const error_msg_1 = ("\"" + replace(patternInput[1], "\"", "\\\"")) + "\"";
    const initial_state_fun = st_func_name(0);
    const token_ids = ofArray(map_2((_arg1) => ((_arg1.tag === 1) ? pretty(_arg1.fields[0]) : word("None")), patternInput[0]));
    const construct_table = Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("["), seplist(word(", "), token_ids)), word("]")), word(" # token_ids"));
    const table_name = new_rnd_name();
    push_toplevel(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word(table_name), word("=")), construct_table));
    middle_toplevels = vsep(ofArray([empty_2, word("@dataclasses.dataclass"), word("class Token:"), Doc_op_RightShift_1E15AFA6(vsep(ofArray([word("token_id: int"), word("lexeme : str"), word("line: int"), word("col: int"), word("span: int"), word("offset: int"), word("file: str")])), 4), empty_2, word("_Token = typing.TypeVar(\"_Token\")"), empty_2, word("class TokenConstructor(typing_extensions.Protocol[_Token]):"), Doc_op_RightShift_1E15AFA6(vsep(singleton(word("def __call__(self, token_id: int, lexeme: str, line: int, col: int, span: int, offset: int, file: str) -\u003e _Token: ..."))), 4), empty_2, Doc_op_Addition_Z492644C0(word("def"), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word("lex"), parens(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("lexerbuf: lexbuf"), word(", ")), word("construct_token: TokenConstructor[_Token]=Token")))), word(":"))), Doc_op_RightShift_1E15AFA6(vsep(ofArray([word("start(lexerbuf)"), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("case_id"), word("=")), Doc_op_Multiply_Z492644C0(word(initial_state_fun), parens(word("lexerbuf")))), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("if case_id \u003c 0:"), word("raise")), Doc_op_Multiply_Z492644C0(word("Exception"), parens(word(error_msg_1)))), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("token_id"), word("=")), Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(word(table_name), word("[")), word("case_id")), word("]"))), word("if token_id is not None:"), Doc_op_RightShift_1E15AFA6(vsep(singleton(Doc_op_Addition_Z492644C0(word("return"), Doc_op_Multiply_Z492644C0(word("construct_token"), parens(seplist(word(", "), ofArray([word("token_id"), word("lexeme(lexerbuf)"), word("lexerbuf.start_line"), word("lexerbuf.pos - lexerbuf.curr_bol"), word("lexerbuf.pos - lexerbuf.start_pos"), word("lexerbuf.start_pos"), word("lexerbuf.filename")]))))))), 4), word("return None")])), 4), word("def lexall(buf: lexbuf, construct: TokenConstructor[_Token], is_eof: Callable[[_Token], bool]):"), Doc_op_RightShift_1E15AFA6(vsep(ofArray([word("while True:"), Doc_op_RightShift_1E15AFA6(vsep(ofArray([word("token = lex(buf, construct)"), word("if token is None: continue"), word("if is_eof(token): break"), word("yield token")])), 4)])), 4)]));
    return vsep(append(singleton(vsep(ofArray([word(`from ${import_head}.sedlex import *`), word("import typing"), word("import typing_extensions"), word("import dataclasses")]))), append(toplevels, append(singleton(middle_toplevels), later_toplevels))));
}

