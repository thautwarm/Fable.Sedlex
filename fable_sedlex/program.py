from __future__ import annotations
import sys
from typing import (Optional, List)
from fable_modules.fable_library.list import of_array
from fable_modules.fable_library.string import (to_console, printf)
from .code_gen import (show_doc, Doc_op_RightShift_2AAA0F3C, Doc_op_Addition_Z7CFFAC00, word, vsep, Doc_op_Multiply_Z7CFFAC00)
from .sedlex import (compile_inline_thread, build, pstring, Lexer_tokenize, from_ustring, token)

def main(_arg1: List[str]) -> int:
    arg10 : Optional[token] = compile_inline_thread(build([(pstring("123"), Lexer_tokenize(2))], "error msg"))(from_ustring("123"))
    to_console(printf("%A"))(arg10)
    arg10_1 : str = show_doc(Doc_op_RightShift_2AAA0F3C(Doc_op_Addition_Z7CFFAC00(word("class"), vsep(of_array([word("def"), Doc_op_RightShift_2AAA0F3C(vsep(of_array([word("123"), Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(Doc_op_Addition_Z7CFFAC00(word("var"), word("x")), word("=")), Doc_op_Multiply_Z7CFFAC00(word("z"), word(";")))])), 3)]))), 2))
    to_console(printf("%s"))(arg10_1)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])


