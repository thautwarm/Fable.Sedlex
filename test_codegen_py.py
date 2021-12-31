from test_compile_regex import cu
from fable_sedlex.code_gen_python import codegen_python
from fable_sedlex.code_gen import show_doc


code = show_doc(codegen_python("fable_sedlex", cu))
# print(code)

with open("generated.py", 'w', encoding='utf8') as f:
    f.write(code)

