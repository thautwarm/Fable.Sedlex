from fable_sedlex.sedlex import *
from test_compile_regex import cu
from dataclasses import dataclass

@dataclass
class MyToken:
  token_id: int
  lexeme : str
  line: int
  col: int
  span: int
  offset: int
  file: str

f = inline_thread(cu, lambda args: MyToken(*args))
buf = from_ustring(r'123 2345 + += 2.34E5 "sada\"sa" ')

tokens = []
EOF_ID = 0

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