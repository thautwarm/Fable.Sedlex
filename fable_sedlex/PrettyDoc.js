import { toString, Union } from "./fable_modules/fable-library.3.7.6/Types.js";
import { class_type, union_type, string_type, int32_type, list_type } from "./fable_modules/fable-library.3.7.6/Reflection.js";
import { skip, head, last, append, concat as concat_1, take } from "./fable_modules/fable-library.3.7.6/Array.js";
import { toList, map } from "./fable_modules/fable-library.3.7.6/Seq.js";
import { head as head_1, tail, isEmpty, cons, empty as empty_1 } from "./fable_modules/fable-library.3.7.6/List.js";
import { replicate } from "./fable_modules/fable-library.3.7.6/String.js";
import { disposeSafe, getEnumerator } from "./fable_modules/fable-library.3.7.6/Util.js";
import { StringBuilder__Append_Z721C83C5, StringBuilder_$ctor } from "./fable_modules/fable-library.3.7.6/System.Text.js";

export class Doc extends Union {
    constructor(tag, ...fields) {
        super();
        this.tag = (tag | 0);
        this.fields = fields;
    }
    cases() {
        return ["Concat", "VSep", "Align", "Indent", "Segment", "Empty"];
    }
}

export function Doc$reflection() {
    return union_type("Fable.Sedlex.PrettyDoc.Doc", [], Doc, () => [[["Item1", Doc$reflection()], ["Item2", Doc$reflection()]], [["Item", list_type(Doc$reflection())]], [["Item", Doc$reflection()]], [["Item1", int32_type], ["Item2", Doc$reflection()]], [["Item", string_type]], []]);
}

export function Doc_op_Multiply_Z492644C0(a, b) {
    return new Doc(0, a, b);
}

export function Doc_op_Addition_Z492644C0(a, b) {
    return Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(a, new Doc(4, " ")), b);
}

export function Doc_op_RightShift_1E15AFA6(a, b) {
    return new Doc(3, b, a);
}

export class DocPrimitive extends Union {
    constructor(tag, ...fields) {
        super();
        this.tag = (tag | 0);
        this.fields = fields;
    }
    cases() {
        return ["DP_PopIndent", "DP_PushCurrentIndent", "DP_PushIndent", "DP_Word"];
    }
}

export function DocPrimitive$reflection() {
    return union_type("Fable.Sedlex.PrettyDoc.DocPrimitive", [], DocPrimitive, () => [[], [], [["Item", int32_type]], [["Item", string_type]]]);
}

export function Array_drop(i, arr) {
    return take(arr.length - i, arr);
}

export function compileToPrims(doc) {
    switch (doc.tag) {
        case 0: {
            const l_1 = compileToPrims(doc.fields[0]);
            const r_1 = compileToPrims(doc.fields[1]);
            if (l_1.length === 0) {
                return r_1;
            }
            else if (r_1.length === 0) {
                return l_1;
            }
            else {
                return concat_1([Array_drop(1, l_1), [append(last(l_1), head(r_1))], skip(1, r_1)]);
            }
        }
        case 2: {
            const it = compileToPrims(doc.fields[0]);
            if (it.length === 0) {
                return it;
            }
            else {
                it[0] = append([new DocPrimitive(1)], it[0]);
                it[it.length - 1] = append(it[it.length - 1], [new DocPrimitive(0)]);
                return it;
            }
        }
        case 3: {
            const prefix = [new DocPrimitive(2, doc.fields[0])];
            const it_1 = compileToPrims(doc.fields[1]);
            if (it_1.length === 0) {
                return it_1;
            }
            else {
                it_1[0] = append(prefix, it_1[0]);
                it_1[it_1.length - 1] = append(it_1[it_1.length - 1], [new DocPrimitive(0)]);
                return it_1;
            }
        }
        case 1: {
            return concat_1(map(compileToPrims, doc.fields[0]));
        }
        case 4: {
            return [[new DocPrimitive(3, doc.fields[0])]];
        }
        default: {
            return [];
        }
    }
}

export class Stack$1 {
    constructor(init) {
        this._content = ((init != null) ? toList(init) : empty_1());
    }
}

export function Stack$1$reflection(gen0) {
    return class_type("Fable.Sedlex.PrettyDoc.Stack`1", [gen0], Stack$1);
}

export function Stack$1_$ctor_2605DBCF(init) {
    return new Stack$1(init);
}

export function Stack$1__Push_2B595(__, a) {
    __._content = cons(a, __._content);
}

export function Stack$1__Pop(__) {
    const matchValue = __._content;
    if (!isEmpty(matchValue)) {
        __._content = tail(matchValue);
        return head_1(matchValue);
    }
    else {
        const exn = new Error("negative stacksize");
        throw exn;
    }
}

export function Stack$1__get_Last(__) {
    const matchValue = __._content;
    if (!isEmpty(matchValue)) {
        return head_1(matchValue);
    }
    else {
        const exn = new Error("negative stacksize");
        throw exn;
    }
}

export function render(setences, write) {
    const levels = Stack$1_$ctor_2605DBCF([0]);
    if (setences.length === 0) {
    }
    else {
        for (let idx = 0; idx <= (setences.length - 1); idx++) {
            const words = setences[idx];
            let col = 0;
            let initialized = false;
            for (let idx_1 = 0; idx_1 <= (words.length - 1); idx_1++) {
                const word_1 = words[idx_1];
                switch (word_1.tag) {
                    case 1: {
                        Stack$1__Push_2B595(levels, col);
                        break;
                    }
                    case 0: {
                        Stack$1__Pop(levels);
                        break;
                    }
                    case 2: {
                        Stack$1__Push_2B595(levels, Stack$1__get_Last(levels) + word_1.fields[0]);
                        break;
                    }
                    default: {
                        const s = word_1.fields[0];
                        if (!initialized) {
                            col = ((Stack$1__get_Last(levels) + col) | 0);
                            write(replicate(col, " "));
                            initialized = true;
                        }
                        write(s);
                        col = ((col + s.length) | 0);
                    }
                }
            }
            write("\n");
        }
    }
}

export function pretty(s) {
    let copyOfStruct;
    return new Doc(4, (copyOfStruct = s, toString(copyOfStruct)));
}

export function seg(s) {
    return new Doc(4, s);
}

export function word(s) {
    return seg(s);
}

export function vsep(lines) {
    return new Doc(1, lines);
}

export function align(seg_1) {
    return new Doc(2, seg_1);
}

export function indent(i, x) {
    return new Doc(3, i, x);
}

export function concat(a, b) {
    return new Doc(0, a, b);
}

export const empty = new Doc(5);

export function parens(content) {
    return Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(seg("("), content), seg(")"));
}

export function bracket(content) {
    return Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(seg("["), content), seg("]"));
}

export function listof(lst) {
    if (!isEmpty(lst)) {
        let res = head_1(lst);
        const enumerator = getEnumerator(tail(lst));
        try {
            while (enumerator["System.Collections.IEnumerator.MoveNext"]()) {
                const each = enumerator["System.Collections.Generic.IEnumerator`1.get_Current"]();
                res = Doc_op_Multiply_Z492644C0(res, each);
            }
        }
        finally {
            disposeSafe(enumerator);
        }
        return res;
    }
    else {
        return empty;
    }
}

export function seplist(sep, lst) {
    if (!isEmpty(lst)) {
        let res = head_1(lst);
        const enumerator = getEnumerator(tail(lst));
        try {
            while (enumerator["System.Collections.IEnumerator.MoveNext"]()) {
                const each = enumerator["System.Collections.Generic.IEnumerator`1.get_Current"]();
                res = Doc_op_Multiply_Z492644C0(Doc_op_Multiply_Z492644C0(res, sep), each);
            }
        }
        finally {
            disposeSafe(enumerator);
        }
        return res;
    }
    else {
        return empty;
    }
}

export function showDoc(doc) {
    const sb = StringBuilder_$ctor();
    render(compileToPrims(doc), (x) => {
        StringBuilder__Append_Z721C83C5(sb, x);
    });
    return toString(sb);
}

export function genDoc(doc, write) {
    render(compileToPrims(doc), write);
}

