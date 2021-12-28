fable-py --outDir fable_sedlex

# https://github.com/fable-compiler/Fable.Python/issues/30#issuecomment-1002059876
rm fable_sedlex/fable_modules/.gitignore

"import sys;import os;sys.path.append(os.path.dirname(__file__))" | Out-File -FilePath "fable_sedlex/__init__.py" 