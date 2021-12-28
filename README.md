NOTE: Currently we only have an interpreted mode, and this already satisfies my use case as I'm using PyPy and there is no performance penalty.

It's EASY to compile `compiled_unit`(see `compile_inline_thread` for how to write a custom backend) into source code for Python, F\# and others.

## Fable.Sedlex

Thanks to the [Fable.Python](https://github.com/fable-compiler/Fable.Python) compiler, this project managed to modify code from [the amazing OCaml `sedlex`](https://github.com/ocaml-community/sedlex/blob/master/src/syntax), implementing an ultimate lexer generator for (currently) both Python and F\#.

The most impressive feature of `sedlex` is that Sedlex statically analyses regular expressions built with lexer combinators, correctly ordering/merging/optimizing the lexical rules. **In short, `sedlex` is correct and efficient.**

**For Python users**: The generated Python code is located in `fable_sedlex`, and you can copy them to directly access such lexer generator in Python. 

**For .NET(C\#, F\#) users**: Copying `Sedlex.fs` will give you such lexer generator in .NET.

**For users in other programming languages**: You might access `compiled_unit` and write a code generator.

```python
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

> python test.py

{ token_id = 2
  lexeme = 123
  line = 0
  col = 3
  span = 3
  offset = 0
  file =  }
 ...

```