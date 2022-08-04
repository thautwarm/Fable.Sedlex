from typing import (TypeVar, Callable, Any, Optional)
from .util import (IEqualityComparer, structural_hash, equals, physical_hash, IComparer, compare)

_T = TypeVar("_T")

_T_ = TypeVar("_T_")

def HashIdentity_FromFunctions(hash_1: Callable[[_T], int], eq: Any) -> IEqualityComparer[Any]:
    class ObjectExpr0(IEqualityComparer[Any]):
        def Equals(self, x: _T_, y: _T_, hash_1: Callable[[_T], int]=hash_1, eq: Any=eq) -> bool:
            return eq(x, y)

        def GetHashCode(self, x_1: Optional[_T_]=None, hash_1: Callable[[_T], int]=hash_1, eq: Any=eq) -> int:
            return hash_1(x_1)

    return ObjectExpr0()


def HashIdentity_Structural() -> IEqualityComparer[Any]:
    def arrow_1(obj: Optional[_T]=None) -> int:
        return structural_hash(obj)

    def arrow_2(e: _T, e_1: _T) -> bool:
        return equals(e, e_1)

    return HashIdentity_FromFunctions(arrow_1, arrow_2)


def HashIdentity_Reference() -> IEqualityComparer[Any]:
    def arrow_3(obj: Optional[_T]=None) -> int:
        return physical_hash(obj)

    def arrow_4(e: _T, e_1: _T) -> bool:
        return e == e_1

    return HashIdentity_FromFunctions(arrow_3, arrow_4)


def ComparisonIdentity_FromFunction(comparer: Any) -> IComparer[_T]:
    class ObjectExpr5(IComparer[_T_]):
        def Compare(self, x: _T_, y: _T_, comparer: Any=comparer) -> int:
            return comparer(x, y)

    return ObjectExpr5()


def ComparisonIdentity_Structural() -> IComparer[_T]:
    def arrow_6(e: _T, e_1: _T) -> int:
        return compare(e, e_1)

    return ComparisonIdentity_FromFunction(arrow_6)


