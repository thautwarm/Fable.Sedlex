from __future__ import annotations
from typing import (Any, TypeVar, Optional, Callable)
from .util import (equals, structural_hash, IComparer, IEqualityComparer, IDisposable, dispose, ignore)
from .fsharp_collections import (ComparisonIdentity_Structural, HashIdentity_Structural)
from .system_text import (StringBuilder, StringBuilder__Append_Z721C83C5)

_T = TypeVar("_T")

__A = TypeVar("__A")

__B = TypeVar("__B")

class ObjectExpr8(IEqualityComparer):
    def System_Collections_IEqualityComparer_Equals541DA560(self, x: Any=None, y: Any=None) -> bool:
        return equals(x, y)

    def System_Collections_IEqualityComparer_GetHashCode4E60E31B(self, x_1: Any=None) -> int:
        return structural_hash(x_1)


LanguagePrimitives_GenericEqualityComparer : IEqualityComparer = ObjectExpr8()

class ObjectExpr9(IEqualityComparer):
    def System_Collections_IEqualityComparer_Equals541DA560(self, x: Any=None, y: Any=None) -> bool:
        return equals(x, y)

    def System_Collections_IEqualityComparer_GetHashCode4E60E31B(self, x_1: Any=None) -> int:
        return structural_hash(x_1)


LanguagePrimitives_GenericEqualityERComparer : IEqualityComparer = ObjectExpr9()

def LanguagePrimitives_FastGenericComparer() -> IComparer[_T]:
    return ComparisonIdentity_Structural()


def LanguagePrimitives_FastGenericComparerFromTable() -> IComparer[_T]:
    return ComparisonIdentity_Structural()


def LanguagePrimitives_FastGenericEqualityComparer() -> IEqualityComparer[Any]:
    return HashIdentity_Structural()


def LanguagePrimitives_FastGenericEqualityComparerFromTable() -> IEqualityComparer[Any]:
    return HashIdentity_Structural()


def Operators_Failure(message: str) -> Exception:
    return Exception(message)


def Operators_FailurePattern(exn: Exception) -> Optional[str]:
    return str(exn)


def Operators_NullArg(x: str) -> __A:
    raise Exception(x)


def Operators_Using(resource: IDisposable, action: Callable[[IDisposable], __A]) -> __A:
    try: 
        return action(resource)

    finally: 
        if equals(resource, None):
            pass

        else: 
            dispose(resource)




def Operators_Lock(_lockObj: __A, action: Callable[[], __B]) -> __B:
    return action()


def ExtraTopLevelOperators_LazyPattern(input: Any) -> __A:
    return input.Value


def PrintfModule_PrintFormatToStringBuilderThen(continuation: Callable[[], __A], builder: StringBuilder, format: Any) -> __B:
    def append(s: str, continuation: Callable[[], __A]=continuation, builder: StringBuilder=builder, format: Any=format) -> __A:
        ignore(StringBuilder__Append_Z721C83C5(builder, s))
        return continuation()

    return format.cont(append)


def PrintfModule_PrintFormatToStringBuilder(builder: StringBuilder, format: Any) -> __A:
    def arrow_19(builder: StringBuilder=builder, format: Any=format) -> None:
        ignore()

    return PrintfModule_PrintFormatToStringBuilderThen(arrow_19, builder, format)


