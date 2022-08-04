from __future__ import annotations
from typing import (TypeVar, Any, Generic, Optional)
from .array import (fill, copy_to, initialize)
from .reflection import (TypeInfo, class_type)
from .seq import (delay, enumerate_while, append, singleton, empty, to_array)
from .types import (Array, FSharpRef)
from .util import (compare, IComparer, equals, structural_hash, IEqualityComparer, get_enumerator, IEnumerable, IEnumerator, to_iterator, max, compare_primitives)

_T = TypeVar("_T")

_T_ = TypeVar("_T_")

def expr_10(gen0: TypeInfo) -> TypeInfo:
    return class_type("System.Collections.Generic.Comparer`1", [gen0], Comparer_1)


class Comparer_1(Generic[_T]):
    def Compare(self, x: _T, y: _T) -> int:
        return compare(x, y)


Comparer_1_reflection = expr_10

def Comparer_1__ctor() -> Comparer_1[Any]:
    return Comparer_1()


def Comparer_1_get_Default() -> IComparer[_T]:
    class ObjectExpr11(IComparer[_T_]):
        def Compare(self, x: _T_, y: _T_) -> int:
            return compare(x, y)

    return ObjectExpr11()


def expr_12(gen0: TypeInfo) -> TypeInfo:
    return class_type("System.Collections.Generic.EqualityComparer`1", [gen0], EqualityComparer_1)


class EqualityComparer_1(Generic[_T]):
    def __eq__(self, x: _T, y: _T) -> bool:
        return equals(x, y)

    def GetHashCode(self, x: Optional[_T]=None) -> int:
        return structural_hash(x)


EqualityComparer_1_reflection = expr_12

def EqualityComparer_1__ctor() -> EqualityComparer_1[Any]:
    return EqualityComparer_1()


def EqualityComparer_1_get_Default() -> IEqualityComparer[Any]:
    class ObjectExpr13(IEqualityComparer[Any]):
        def Equals(self, x: _T_, y: _T_) -> bool:
            return equals(x, y)

        def GetHashCode(self, x_1: Optional[_T_]=None) -> int:
            return structural_hash(x_1)

    return ObjectExpr13()


def expr_18(gen0: TypeInfo) -> TypeInfo:
    return class_type("System.Collections.Generic.Stack`1", [gen0], Stack_1)


class Stack_1(Generic[_T]):
    def __init__(self, initial_contents: Array[_T], initial_count: int) -> None:
        self.contents = initial_contents
        self.count = initial_count or 0

    def GetEnumerator(self) -> IEnumerator[_T]:
        _ : Stack_1[_T] = self
        def arrow_17(__unit: Any=None) -> IEnumerable[_T]:
            index : int = (_.count - 1) or 0
            def arrow_14(__unit: Any=None) -> bool:
                return index >= 0

            def arrow_16(__unit: Any=None) -> IEnumerable[_T]:
                def arrow_15(__unit: Any=None) -> IEnumerable[_T]:
                    nonlocal index
                    index = (index - 1) or 0
                    return empty()

                return append(singleton(_.contents[index]), delay(arrow_15))

            return enumerate_while(arrow_14, delay(arrow_16))

        return get_enumerator(delay(arrow_17))

    def __iter__(self) -> IEnumerator[_T]:
        return to_iterator(self.GetEnumerator())

    def System_Collections_IEnumerable_GetEnumerator(self) -> IEnumerator[Any]:
        this : Stack_1[_T] = self
        return get_enumerator(this)


Stack_1_reflection = expr_18

def Stack_1__ctor_Z2E171D71(initial_contents: Array[_T], initial_count: int) -> Stack_1[_T]:
    return Stack_1(initial_contents, initial_count)


def Stack_1__ctor_Z524259A4(initial_capacity: int) -> Stack_1[_T]:
    return Stack_1__ctor_Z2E171D71(fill([0] * initial_capacity, 0, initial_capacity, None), 0)


def Stack_1__ctor() -> Stack_1[_T]:
    return Stack_1__ctor_Z524259A4(4)


def Stack_1__ctor_BB573A(xs: IEnumerable[_T]) -> Stack_1[_T]:
    arr : Array[_T] = list(xs)
    return Stack_1__ctor_Z2E171D71(arr, len(arr))


def Stack_1__Ensure_Z524259A4(_: Stack_1[_T], new_size: int) -> None:
    old_size : int = len(_.contents) or 0
    if new_size > old_size:
        old : Array[_T] = _.contents
        def arrow_20(x: int, y: int, _: Stack_1[_T]=_, new_size: int=new_size) -> int:
            return compare_primitives(x, y)

        def arrow_21(x: int, y: int, _: Stack_1[_T]=_, new_size: int=new_size) -> int:
            return compare_primitives(x, y)

        _.contents = fill([0] * max(arrow_20, new_size, old_size * 2), 0, max(arrow_21, new_size, old_size * 2), None)
        copy_to(old, 0, _.contents, 0, _.count)



def Stack_1__get_Count(_: Stack_1[_T]) -> int:
    return _.count


def Stack_1__Pop(_: Stack_1[_T]) -> _T:
    _.count = (_.count - 1) or 0
    return _.contents[_.count]


def Stack_1__Peek(_: Stack_1[_T]) -> _T:
    return _.contents[_.count - 1]


def Stack_1__Contains_2B595(_: Stack_1[_T], x: _T) -> bool:
    found : bool = False
    i : int = 0
    while (not found) if (i < _.count) else False:
        if equals(x, _.contents[i]):
            found = True

        else: 
            i = (i + 1) or 0

    return found


def Stack_1__TryPeek_1F3DB691(this: Stack_1[_T], result: FSharpRef[_T]) -> bool:
    if this.count > 0:
        result.contents = Stack_1__Peek(this)
        return True

    else: 
        return False



def Stack_1__TryPop_1F3DB691(this: Stack_1[_T], result: FSharpRef[_T]) -> bool:
    if this.count > 0:
        result.contents = Stack_1__Pop(this)
        return True

    else: 
        return False



def Stack_1__Push_2B595(this: Stack_1[_T], x: _T) -> None:
    Stack_1__Ensure_Z524259A4(this, this.count + 1)
    this.contents[this.count] = x
    this.count = (this.count + 1) or 0


def Stack_1__Clear(_: Stack_1[_T]) -> None:
    _.count = 0
    fill(_.contents, 0, len(_.contents), None)


def Stack_1__TrimExcess(this: Stack_1[_T]) -> None:
    if (this.count / len(this.contents)) > 0.9:
        Stack_1__Ensure_Z524259A4(this, this.count)



def Stack_1__ToArray(_: Stack_1[_T]) -> Array[_T]:
    def arrow_22(i: int, _: Stack_1[_T]=_) -> _T:
        return _.contents[(_.count - 1) - i]

    return initialize(_.count, arrow_22, None)


def expr_23(gen0: TypeInfo) -> TypeInfo:
    return class_type("System.Collections.Generic.Queue`1", [gen0], Queue_1)


class Queue_1(Generic[_T]):
    def __init__(self, initial_contents: Array[_T], initial_count: int) -> None:
        self.contents = initial_contents
        self.count = initial_count or 0
        self.head = 0
        self.tail = initial_count or 0

    def GetEnumerator(self) -> IEnumerator[_T]:
        _ : Queue_1[_T] = self
        return get_enumerator(Queue_1__toSeq(_))

    def __iter__(self) -> IEnumerator[_T]:
        return to_iterator(self.GetEnumerator())

    def System_Collections_IEnumerable_GetEnumerator(self) -> IEnumerator[Any]:
        this : Queue_1[_T] = self
        return get_enumerator(this)


Queue_1_reflection = expr_23

def Queue_1__ctor_Z2E171D71(initial_contents: Array[_T], initial_count: int) -> Queue_1[_T]:
    return Queue_1(initial_contents, initial_count)


def Queue_1__ctor_Z524259A4(initial_capacity: int) -> Queue_1[_T]:
    if initial_capacity < 0:
        raise Exception("capacity is less than 0")

    return Queue_1__ctor_Z2E171D71(fill([0] * initial_capacity, 0, initial_capacity, None), 0)


def Queue_1__ctor() -> Queue_1[_T]:
    return Queue_1__ctor_Z524259A4(4)


def Queue_1__ctor_BB573A(xs: IEnumerable[_T]) -> Queue_1[_T]:
    arr : Array[_T] = list(xs)
    return Queue_1__ctor_Z2E171D71(arr, len(arr))


def Queue_1__get_Count(_: Queue_1[_T]) -> int:
    return _.count


def Queue_1__Enqueue_2B595(_: Queue_1[_T], value: _T) -> None:
    if _.count == Queue_1__size(_):
        Queue_1__ensure_Z524259A4(_, _.count + 1)

    _.contents[_.tail] = value
    _.tail = ((_.tail + 1) % Queue_1__size(_)) or 0
    _.count = (_.count + 1) or 0


def Queue_1__Dequeue(_: Queue_1[_T]) -> _T:
    if _.count == 0:
        raise Exception("Queue is empty")

    value : _T = _.contents[_.head]
    _.head = ((_.head + 1) % Queue_1__size(_)) or 0
    _.count = (_.count - 1) or 0
    return value


def Queue_1__Peek(_: Queue_1[_T]) -> _T:
    if _.count == 0:
        raise Exception("Queue is empty")

    return _.contents[_.head]


def Queue_1__TryDequeue_1F3DB691(this: Queue_1[_T], result: FSharpRef[_T]) -> bool:
    if this.count == 0:
        return False

    else: 
        result.contents = Queue_1__Dequeue(this)
        return True



def Queue_1__TryPeek_1F3DB691(this: Queue_1[_T], result: FSharpRef[_T]) -> bool:
    if this.count == 0:
        return False

    else: 
        result.contents = Queue_1__Peek(this)
        return True



def Queue_1__Contains_2B595(_: Queue_1[_T], x: _T) -> bool:
    found : bool = False
    i : int = 0
    while (not found) if (i < _.count) else False:
        if equals(x, _.contents[Queue_1__toIndex_Z524259A4(_, i)]):
            found = True

        else: 
            i = (i + 1) or 0

    return found


def Queue_1__Clear(_: Queue_1[_T]) -> None:
    _.count = 0
    _.head = 0
    _.tail = 0
    fill(_.contents, 0, Queue_1__size(_), None)


def Queue_1__TrimExcess(_: Queue_1[_T]) -> None:
    if (_.count / len(_.contents)) > 0.9:
        Queue_1__ensure_Z524259A4(_, _.count)



def Queue_1__ToArray(_: Queue_1[_T]) -> Array[_T]:
    return to_array(Queue_1__toSeq(_))


def Queue_1__CopyTo_Z2E171D71(_: Queue_1[_T], target: Array[_T], start: int) -> None:
    i : int = start or 0
    with get_enumerator(Queue_1__toSeq(_)) as enumerator:
        while enumerator.System_Collections_IEnumerator_MoveNext():
            item : _T = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
            target[i] = item
            i = (i + 1) or 0


def Queue_1__size(this: Queue_1[_T]) -> int:
    return len(this.contents)


def Queue_1__toIndex_Z524259A4(this: Queue_1[_T], i: int) -> int:
    return (this.head + i) % Queue_1__size(this)


def Queue_1__ensure_Z524259A4(this: Queue_1[_T], required_size: int) -> None:
    new_buffer : Array[_T] = fill([0] * required_size, 0, required_size, None)
    if this.head < this.tail:
        copy_to(this.contents, this.head, new_buffer, 0, this.count)

    else: 
        copy_to(this.contents, this.head, new_buffer, 0, Queue_1__size(this) - this.head)
        copy_to(this.contents, 0, new_buffer, Queue_1__size(this) - this.head, this.tail)

    this.head = 0
    this.tail = this.count or 0
    this.contents = new_buffer


def Queue_1__toSeq(this: Queue_1[_T]) -> IEnumerable[_T]:
    def arrow_27(this: Queue_1[_T]=this) -> IEnumerable[_T]:
        i : int = 0
        def arrow_24(__unit: Any=None) -> bool:
            return i < this.count

        def arrow_26(__unit: Any=None) -> IEnumerable[_T]:
            def arrow_25(__unit: Any=None) -> IEnumerable[_T]:
                nonlocal i
                i = (i + 1) or 0
                return empty()

            return append(singleton(this.contents[Queue_1__toIndex_Z524259A4(this, i)]), delay(arrow_25))

        return enumerate_while(arrow_24, delay(arrow_26))

    return delay(arrow_27)


