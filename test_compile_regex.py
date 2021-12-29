from fable_sedlex.sedlex import *
from fable_sedlex.code_gen_python import codegen_python
from fable_sedlex.code_gen import show_doc


digit = pinterval(ord('0'), ord('9'))

dquote = pchar('"')
backslash = pchar('\\')
dot = pchar('.')

exp = pseq([por(pchar('E'), pchar('e')), pplus(digit)])
flt = pseq([pstar(digit), dot, pplus(digit), popt(exp)])
integral = pseq([pplus(digit), popt(exp)])
string_lit = pseq([dquote, pstar(por(pcompl(dquote), pseq([backslash,  pany]))), dquote])
space = pchars(["\n", "\t", "\r", ' '])

EOF_ID = 0
cu = build(
    [
        (space, Lexer_discard),
        (flt, Lexer_tokenize(1)),
        (integral, Lexer_tokenize(2)),
        (string_lit, Lexer_tokenize(3)),
        (pstring("+"), Lexer_tokenize(4)),
        (pstring("+="), Lexer_tokenize(4)),
        (peof, Lexer_tokenize(EOF_ID))
    ], "my error")
