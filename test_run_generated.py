from fable_sedlex.sedlex import from_ustring, lexbuf
from generated import lex, lexall, Token


buf = from_ustring(r'123 2345 + += 2.34E5 "sada\"sa" ')

tokens = []
EOF_ID = 0


def is_eof(x: Token):
    return x.token_id == 0

print()
print(list(lexall(buf, Token, is_eof)))
