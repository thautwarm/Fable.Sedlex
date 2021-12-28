from __future__ import annotations
import sys
from typing import (Optional, List)
from fable_modules.fable_library.string import (to_console, printf)
from .sedlex import (compile_inline_thread, build, pstring, Lexer_tokenize, from_ustring, token)

def main(_arg1: List[str]) -> int:
    arg10 : Optional[token] = compile_inline_thread(build([(pstring("123"), Lexer_tokenize(2))], "error msg"))(from_ustring("123"))
    to_console(printf("%A"))(arg10)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])


