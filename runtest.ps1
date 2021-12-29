pwsh.exe -F ./build.ps1

python test_interpreter.py
python test_codegen_py.py
python test_run_generated.py
