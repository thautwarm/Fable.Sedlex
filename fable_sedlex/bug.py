from __future__ import annotations
from fable_modules.fable_library.reflection import (TypeInfo, class_type)
from fable_modules.fable_library.string import (to_console, printf)

def expr_0() -> TypeInfo:
    return class_type("Bug.Test", None, Test)


class Test:
    def __init__(self, l: int, r: int) -> None:
        self.l = l or 0
        self.r = r or 0
        self.f = 0
    

Test_reflection = expr_0

def Test__ctor_Z37302880(l: int, r: int) -> Test:
    return Test(l, r)


def Test__Run(__: Test) -> int:
    return __.f + Test__call(__)


def Test__call(this: Test) -> int:
    this.f = this.l or 0
    return this.r


def test() -> None:
    arg10 : int = Test__Run(Test__ctor_Z37302880(1, 2)) or 0
    to_console(printf("%d"))(arg10)


