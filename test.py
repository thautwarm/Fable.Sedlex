from fable_sedlex.sedlex import *

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

f = compile_inline_thread(cu)
buf = from_ustring(r'123 2345 + += 2.34E5 "sada\"sa" ')

tokens = []
while True:
    try:
        x = f(buf)
    except Exception as e:
        print(e)
        raise
    print(x)
    if x is None:
        continue
    if x.token_id == EOF_ID:
        break
    tokens.append(x)

print(tokens)

from fable_sedlex.code_gen import *

# vsep(
#     [
#         word("def")
#         word("123")
#     ])