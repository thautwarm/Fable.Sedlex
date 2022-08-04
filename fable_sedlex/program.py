from __future__ import annotations
import sys
from typing import (Tuple, Optional)
from .fable_modules.fable_library.list import of_array
from .fable_modules.fable_library.reflection import (TypeInfo, int32_type, string_type, record_type)
from .fable_modules.fable_library.string import (to_console, printf)
from .fable_modules.fable_library.types import (Record, Array)
from .pretty_doc import (show_doc, Doc_op_RightShift_1E15AFA6, Doc_op_Addition_Z492644C0, word, vsep, Doc_op_Multiply_Z492644C0)
from .sedlex import (token, inline_thread, build, pstring, Lexer_tokenize, from_ustring)

def expr_2() -> TypeInfo:
    return record_type("Main.MyToken", [], MyToken, lambda: [("s_token_id", int32_type), ("s_lexeme", string_type), ("s_line", int32_type), ("s_col", int32_type), ("s_span", int32_type), ("s_offset", int32_type), ("s_file", string_type)])


class MyToken(Record):
    def __init__(self, s_token_id: int, s_lexeme: str, s_line: int, s_col: int, s_span: int, s_offset: int, s_file: str) -> None:
        super().__init__()
        self.s_token_id = s_token_id or 0
        self.s_lexeme = s_lexeme
        self.s_line = s_line or 0
        self.s_col = s_col or 0
        self.s_span = s_span or 0
        self.s_offset = s_offset or 0
        self.s_file = s_file

    @property
    def col(self) -> int:
        this : MyToken = self
        return this.s_col

    @property
    def file(self) -> str:
        this : MyToken = self
        return this.s_file

    @property
    def lexeme(self) -> str:
        this : MyToken = self
        return this.s_lexeme

    @property
    def line(self) -> int:
        this : MyToken = self
        return this.s_line

    @property
    def offset(self) -> int:
        this : MyToken = self
        return this.s_offset

    @property
    def span(self) -> int:
        this : MyToken = self
        return this.s_span

    @property
    def token_id(self) -> int:
        __ : MyToken = self
        return __.s_token_id


MyToken_reflection = expr_2

def create_my_token(token_id: int, lexeme: str, line: int, col: int, span: int, offset: int, file: str) -> token:
    return MyToken(token_id, lexeme, line, col, span, offset, file)


def main(_arg: Array[str]) -> int:
    def arrow_4(tupled_arg: Tuple[int, str, int, int, int, int, str], _arg: Array[str]=_arg) -> token:
        return create_my_token(tupled_arg[0], tupled_arg[1], tupled_arg[2], tupled_arg[3], tupled_arg[4], tupled_arg[5], tupled_arg[6])

    arg : Optional[token] = inline_thread(build([(pstring("123"), Lexer_tokenize(2))], "error msg"), arrow_4)(from_ustring("123"))
    to_console(printf("%A"))(arg)
    arg_1 : str = show_doc(Doc_op_RightShift_1E15AFA6(Doc_op_Addition_Z492644C0(word("class"), vsep(of_array([word("def"), Doc_op_RightShift_1E15AFA6(vsep(of_array([word("123"), Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(Doc_op_Addition_Z492644C0(word("var"), word("x")), word("=")), Doc_op_Multiply_Z492644C0(word("z"), word(";")))])), 3)]))), 2))
    to_console(printf("%s"))(arg_1)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])


