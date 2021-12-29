from fable_sedlex.sedlex import from_ustring, lexbuf
from generated import lex


buf = from_ustring(r'123 2345 + += 2.34E5 "sada\"sa" ')

tokens = []
EOF_ID = 0

while True:
    try:
        x = lex(buf)
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