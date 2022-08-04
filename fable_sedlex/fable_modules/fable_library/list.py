from __future__ import annotations
from typing import (TypeVar, Optional, Callable, Any, Generic, Tuple)
from .array import (fill, fold_back as fold_back_1, fold_back2 as fold_back2_1, iterate as iterate_1, scan_back as scan_back_1, try_find_back as try_find_back_1, try_find_index_back as try_find_index_back_1, permute as permute_1, map as map_1, chunk_by_size as chunk_by_size_1, pairwise as pairwise_1, windowed as windowed_1, split_into as split_into_1, transpose as transpose_1)
from .option import (some, value as value_1, default_arg)
from .reflection import (TypeInfo, option_type, record_type, class_type)
from .string import join
from .types import (Record, Array)
from .util import (equals, structural_hash, compare, IEnumerator, to_iterator, get_enumerator, IDisposable, ignore, IEnumerable, is_array_like, IEqualityComparer, IComparer)
from .global_ import (SR_inputWasEmpty, SR_indexOutOfBounds, SR_keyNotFoundAlt, SR_differentLengths, IGenericAdder_1, IGenericAverager_1, SR_notEnoughElements, SR_inputMustBeNonNegative, SR_inputSequenceEmpty, SR_inputSequenceTooLong)

_T = TypeVar("_T")

___31171 = TypeVar("___31171")

___31170 = TypeVar("___31170")

___31232 = TypeVar("___31232")

___31231 = TypeVar("___31231")

___31111 = TypeVar("___31111")

___31110 = TypeVar("___31110")

___31142 = TypeVar("___31142")

___31141 = TypeVar("___31141")

__A = TypeVar("__A")

_STATE = TypeVar("_STATE")

_T1 = TypeVar("_T1")

_T2 = TypeVar("_T2")

__B = TypeVar("__B")

_U = TypeVar("_U")

_T3 = TypeVar("_T3")

_RESULT = TypeVar("_RESULT")

__C = TypeVar("__C")

def expr_69(gen0: TypeInfo) -> TypeInfo:
    return record_type("ListModule.FSharpList", [gen0], FSharpList, lambda: [("head", gen0), ("tail", option_type(FSharpList_reflection(gen0)))])


class FSharpList(Record, Generic[_T]):
    def __init__(self, head: _T, tail: Optional[FSharpList[_T]]) -> None:
        super().__init__()
        self.head = head
        self.tail = tail

    def __str__(self) -> str:
        xs : FSharpList[_T] = self
        return ("[" + join("; ", xs)) + "]"

    def __eq__(self, other: Any=None) -> bool:
        xs : FSharpList[_T] = self
        if xs is other:
            return True

        else: 
            def loop(xs_1_mut: FSharpList[___31171], ys_1_mut: FSharpList[___31171]) -> bool:
                while True:
                    (xs_1, ys_1) = (xs_1_mut, ys_1_mut)
                    matchValue : Optional[FSharpList[___31171]] = xs_1.tail
                    matchValue_1 : Optional[FSharpList[___31171]] = ys_1.tail
                    if matchValue is not None:
                        if matchValue_1 is not None:
                            xt : FSharpList[___31171] = matchValue
                            yt : FSharpList[___31171] = matchValue_1
                            if equals(xs_1.head, ys_1.head):
                                xs_1_mut = xt
                                ys_1_mut = yt
                                continue

                            else: 
                                return False


                        else: 
                            return False


                    elif matchValue_1 is not None:
                        return False

                    else: 
                        return True

                    break

            loop : Callable[[FSharpList[___31170], FSharpList[___31170]], bool] = loop
            return loop(xs, other)


    def GetHashCode(self) -> int:
        xs : FSharpList[_T] = self
        def loop(i_mut: int, h_mut: int, xs_1_mut: FSharpList[_T]) -> int:
            while True:
                (i, h, xs_1) = (i_mut, h_mut, xs_1_mut)
                match_value : Optional[FSharpList[_T]] = xs_1.tail
                if match_value is not None:
                    t : FSharpList[_T] = match_value
                    if i > 18:
                        return h

                    else: 
                        i_mut = i + 1
                        h_mut = ((h << 1) + structural_hash(xs_1.head)) + (631 * i)
                        xs_1_mut = t
                        continue


                else: 
                    return h

                break

        return loop(0, 0, xs)

    def to_json(self, _key: str) -> Any:
        this : FSharpList[_T] = self
        return list(this)

    def CompareTo(self, other: Any=None) -> int:
        xs : FSharpList[_T] = self
        def loop(xs_1_mut: FSharpList[___31232], ys_1_mut: FSharpList[___31232]) -> int:
            while True:
                (xs_1, ys_1) = (xs_1_mut, ys_1_mut)
                matchValue : Optional[FSharpList[___31232]] = xs_1.tail
                matchValue_1 : Optional[FSharpList[___31232]] = ys_1.tail
                if matchValue is not None:
                    if matchValue_1 is not None:
                        xt : FSharpList[___31232] = matchValue
                        yt : FSharpList[___31232] = matchValue_1
                        c : int = compare(xs_1.head, ys_1.head) or 0
                        if c == 0:
                            xs_1_mut = xt
                            ys_1_mut = yt
                            continue

                        else: 
                            return c


                    else: 
                        return 1


                elif matchValue_1 is not None:
                    return -1

                else: 
                    return 0

                break

        return loop(xs, other)

    def GetEnumerator(self) -> IEnumerator[_T]:
        xs : FSharpList[_T] = self
        return ListEnumerator_1__ctor_3002E699(xs)

    def __iter__(self) -> IEnumerator[_T]:
        return to_iterator(self.GetEnumerator())

    def System_Collections_IEnumerable_GetEnumerator(self) -> IEnumerator[Any]:
        xs : FSharpList[_T] = self
        return get_enumerator(xs)


FSharpList_reflection = expr_69

def expr_70(gen0: TypeInfo) -> TypeInfo:
    return class_type("ListModule.ListEnumerator`1", [gen0], ListEnumerator_1)


class ListEnumerator_1(IDisposable, Generic[_T]):
    def __init__(self, xs: FSharpList[_T]) -> None:
        self.xs = xs
        self.it = self.xs
        self.current = None

    def System_Collections_Generic_IEnumerator_00601_get_Current(self) -> _T:
        _ : ListEnumerator_1[_T] = self
        return _.current

    def System_Collections_IEnumerator_get_Current(self) -> Any:
        _ : ListEnumerator_1[_T] = self
        return _.current

    def System_Collections_IEnumerator_MoveNext(self) -> bool:
        _ : ListEnumerator_1[_T] = self
        match_value : Optional[FSharpList[_T]] = _.it.tail
        if match_value is not None:
            t : FSharpList[_T] = match_value
            _.current = _.it.head
            _.it = t
            return True

        else: 
            return False


    def System_Collections_IEnumerator_Reset(self) -> None:
        _ : ListEnumerator_1[_T] = self
        _.it = _.xs
        _.current = None

    def Dispose(self) -> None:
        pass


ListEnumerator_1_reflection = expr_70

def ListEnumerator_1__ctor_3002E699(xs: FSharpList[_T]) -> ListEnumerator_1[_T]:
    return ListEnumerator_1(xs)


def FSharpList_get_Empty() -> FSharpList[_T]:
    return FSharpList(None, None)


def FSharpList_Cons_305B8EAC(x: _T, xs: FSharpList[_T]) -> FSharpList[_T]:
    return FSharpList(x, xs)


def FSharpList__get_IsEmpty(xs: FSharpList[_T]) -> bool:
    return xs.tail is None


def FSharpList__get_Length(xs: FSharpList[_T]) -> int:
    def loop(i_mut: int, xs_1_mut: FSharpList[___31111], xs: FSharpList[_T]=xs) -> int:
        while True:
            (i, xs_1) = (i_mut, xs_1_mut)
            match_value : Optional[FSharpList[___31111]] = xs_1.tail
            if match_value is not None:
                i_mut = i + 1
                xs_1_mut = match_value
                continue

            else: 
                return i

            break

    return loop(0, xs)


def FSharpList__get_Head(xs: FSharpList[_T]) -> _T:
    match_value : Optional[FSharpList[_T]] = xs.tail
    if match_value is not None:
        return xs.head

    else: 
        raise Exception((SR_inputWasEmpty + "\\nParameter name: ") + "list")



def FSharpList__get_Tail(xs: FSharpList[_T]) -> FSharpList[_T]:
    match_value : Optional[FSharpList[_T]] = xs.tail
    if match_value is not None:
        return match_value

    else: 
        raise Exception((SR_inputWasEmpty + "\\nParameter name: ") + "list")



def FSharpList__get_Item_Z524259A4(xs: FSharpList[_T], index: int) -> _T:
    def loop(i_mut: int, xs_1_mut: FSharpList[___31142], xs: FSharpList[_T]=xs, index: int=index) -> ___31142:
        while True:
            (i, xs_1) = (i_mut, xs_1_mut)
            match_value : Optional[FSharpList[___31142]] = xs_1.tail
            if match_value is not None:
                if i == index:
                    return xs_1.head

                else: 
                    i_mut = i + 1
                    xs_1_mut = match_value
                    continue


            else: 
                raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

            break

    return loop(0, xs)


def empty() -> FSharpList[__A]:
    return FSharpList_get_Empty()


def cons(x: _T, xs: FSharpList[_T]) -> FSharpList[_T]:
    return FSharpList_Cons_305B8EAC(x, xs)


def singleton(x: Optional[__A]=None) -> FSharpList[__A]:
    return FSharpList_Cons_305B8EAC(x, FSharpList_get_Empty())


def is_empty(xs: FSharpList[_T]) -> bool:
    return FSharpList__get_IsEmpty(xs)


def length(xs: FSharpList[_T]) -> int:
    return FSharpList__get_Length(xs)


def head(xs: FSharpList[_T]) -> _T:
    return FSharpList__get_Head(xs)


def try_head(xs: FSharpList[_T]) -> Optional[_T]:
    if FSharpList__get_IsEmpty(xs):
        return None

    else: 
        return some(FSharpList__get_Head(xs))



def tail(xs: FSharpList[_T]) -> FSharpList[_T]:
    return FSharpList__get_Tail(xs)


def try_last(xs_mut: FSharpList[_T]) -> Optional[_T]:
    while True:
        (xs,) = (xs_mut,)
        if FSharpList__get_IsEmpty(xs):
            return None

        else: 
            t : FSharpList[_T] = FSharpList__get_Tail(xs)
            if FSharpList__get_IsEmpty(t):
                return some(FSharpList__get_Head(xs))

            else: 
                xs_mut = t
                continue


        break


def last(xs: FSharpList[_T]) -> _T:
    match_value : Optional[_T] = try_last(xs)
    if match_value is None:
        raise Exception(SR_inputWasEmpty)

    else: 
        return value_1(match_value)



def compare_with(comparer: Any, xs: FSharpList[_T], ys: FSharpList[_T]) -> int:
    def loop(xs_1_mut: FSharpList[_T], ys_1_mut: FSharpList[_T], comparer: Any=comparer, xs: FSharpList[_T]=xs, ys: FSharpList[_T]=ys) -> int:
        while True:
            (xs_1, ys_1) = (xs_1_mut, ys_1_mut)
            matchValue : bool = FSharpList__get_IsEmpty(xs_1)
            matchValue_1 : bool = FSharpList__get_IsEmpty(ys_1)
            if matchValue:
                if matchValue_1:
                    return 0

                else: 
                    return -1


            elif matchValue_1:
                return 1

            else: 
                c : int = comparer(FSharpList__get_Head(xs_1), FSharpList__get_Head(ys_1)) or 0
                if c == 0:
                    xs_1_mut = FSharpList__get_Tail(xs_1)
                    ys_1_mut = FSharpList__get_Tail(ys_1)
                    continue

                else: 
                    return c


            break

    return loop(xs, ys)


def to_array(xs: FSharpList[_T]) -> Array[_T]:
    len_1 : int = FSharpList__get_Length(xs) or 0
    res : Array[_T] = fill([0] * len_1, 0, len_1, None)
    def loop(i_mut: int, xs_1_mut: FSharpList[_T], xs: FSharpList[_T]=xs) -> None:
        while True:
            (i, xs_1) = (i_mut, xs_1_mut)
            if not FSharpList__get_IsEmpty(xs_1):
                res[i] = FSharpList__get_Head(xs_1)
                i_mut = i + 1
                xs_1_mut = FSharpList__get_Tail(xs_1)
                continue

            break

    loop(0, xs)
    return res


def fold(folder: Any, state: _STATE, xs: FSharpList[_T]) -> _STATE:
    acc : _STATE = state
    xs_1 : FSharpList[_T] = xs
    while not FSharpList__get_IsEmpty(xs_1):
        acc = folder(acc, FSharpList__get_Head(xs_1))
        xs_1 = FSharpList__get_Tail(xs_1)
    return acc


def reverse(xs: FSharpList[_T]) -> FSharpList[_T]:
    def arrow_71(acc: FSharpList[_T], x: _T, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        return FSharpList_Cons_305B8EAC(x, acc)

    return fold(arrow_71, FSharpList_get_Empty(), xs)


def fold_back(folder: Any, xs: FSharpList[_T], state: _STATE) -> _STATE:
    return fold_back_1(folder, to_array(xs), state)


def fold_indexed(folder: Any, state: _STATE, xs: FSharpList[_T]) -> _STATE:
    def loop(i_mut: int, acc_mut: _STATE, xs_1_mut: FSharpList[_T], folder: Any=folder, state: _STATE=state, xs: FSharpList[_T]=xs) -> _STATE:
        while True:
            (i, acc, xs_1) = (i_mut, acc_mut, xs_1_mut)
            if FSharpList__get_IsEmpty(xs_1):
                return acc

            else: 
                i_mut = i + 1
                acc_mut = folder(i, acc, FSharpList__get_Head(xs_1))
                xs_1_mut = FSharpList__get_Tail(xs_1)
                continue

            break

    return loop(0, state, xs)


def fold2(folder: Any, state: _STATE, xs: FSharpList[_T1], ys: FSharpList[_T2]) -> _STATE:
    acc : _STATE = state
    xs_1 : FSharpList[_T1] = xs
    ys_1 : FSharpList[_T2] = ys
    while (not FSharpList__get_IsEmpty(ys_1)) if (not FSharpList__get_IsEmpty(xs_1)) else False:
        acc = folder(acc, FSharpList__get_Head(xs_1), FSharpList__get_Head(ys_1))
        xs_1 = FSharpList__get_Tail(xs_1)
        ys_1 = FSharpList__get_Tail(ys_1)
    return acc


def fold_back2(folder: Any, xs: FSharpList[_T1], ys: FSharpList[_T2], state: _STATE) -> _STATE:
    return fold_back2_1(folder, to_array(xs), to_array(ys), state)


def unfold(gen: Callable[[_STATE], Optional[Tuple[_T, _STATE]]], state: _STATE) -> FSharpList[_T]:
    def loop(acc_mut: _STATE, node_mut: FSharpList[_T], gen: Callable[[_STATE], Optional[Tuple[_T, _STATE]]]=gen, state: _STATE=state) -> FSharpList[_T]:
        while True:
            (acc, node) = (acc_mut, node_mut)
            match_value : Optional[Tuple[_T, _STATE]] = gen(acc)
            if match_value is not None:
                acc_mut = match_value[1]
                def arrow_72(acc: _STATE=acc, node: FSharpList[_T]=node) -> FSharpList[_T]:
                    t : FSharpList[_T] = FSharpList(match_value[0], None)
                    node.tail = t
                    return t

                node_mut = arrow_72()
                continue

            else: 
                return node

            break

    root : FSharpList[_T] = FSharpList_get_Empty()
    node_1 : FSharpList[_T] = loop(state, root)
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    node_1.tail = t_2
    return FSharpList__get_Tail(root)


def iterate(action: Callable[[__A], None], xs: FSharpList[__A]) -> None:
    def arrow_73(unit_var: None, x: __A, action: Callable[[__A], None]=action, xs: FSharpList[__A]=xs) -> None:
        action(x)

    fold(arrow_73, None, xs)


def iterate2(action: Any, xs: FSharpList[__A], ys: FSharpList[__B]) -> None:
    def arrow_74(unit_var: None, x: __A, y: __B, action: Any=action, xs: FSharpList[__A]=xs, ys: FSharpList[__B]=ys) -> None:
        action(x, y)

    fold2(arrow_74, None, xs, ys)


def iterate_indexed(action: Any, xs: FSharpList[__A]) -> None:
    def arrow_75(i: int, x: __A, action: Any=action, xs: FSharpList[__A]=xs) -> int:
        action(i, x)
        return i + 1

    ignore(fold(arrow_75, 0, xs))


def iterate_indexed2(action: Any, xs: FSharpList[__A], ys: FSharpList[__B]) -> None:
    def arrow_76(i: int, x: __A, y: __B, action: Any=action, xs: FSharpList[__A]=xs, ys: FSharpList[__B]=ys) -> int:
        action(i, x, y)
        return i + 1

    ignore(fold2(arrow_76, 0, xs, ys))


def to_seq(xs: FSharpList[_T]) -> IEnumerable[_T]:
    return xs


def of_array_with_tail(xs: Array[_T], tail_1: FSharpList[_T]) -> FSharpList[_T]:
    res : FSharpList[_T] = tail_1
    for i in range(len(xs) - 1, 0 - 1, -1):
        res = FSharpList_Cons_305B8EAC(xs[i], res)
    return res


def of_array(xs: Array[_T]) -> FSharpList[_T]:
    return of_array_with_tail(xs, FSharpList_get_Empty())


def of_seq(xs: IEnumerable[_T]) -> FSharpList[_T]:
    if is_array_like(xs):
        return of_array(xs)

    elif isinstance(xs, FSharpList):
        return xs

    else: 
        root : FSharpList[_T] = FSharpList_get_Empty()
        node : FSharpList[_T] = root
        with get_enumerator(xs) as enumerator:
            while enumerator.System_Collections_IEnumerator_MoveNext():
                x : _T = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
                def arrow_77(xs: IEnumerable[_T]=xs) -> FSharpList[_T]:
                    xs_3 : FSharpList[_T] = node
                    t : FSharpList[_T] = FSharpList(x, None)
                    xs_3.tail = t
                    return t

                node = arrow_77()
        xs_5 : FSharpList[_T] = node
        t_2 : FSharpList[_T] = FSharpList_get_Empty()
        xs_5.tail = t_2
        return FSharpList__get_Tail(root)



def concat(lists: IEnumerable[FSharpList[_T]]) -> FSharpList[_T]:
    root : FSharpList[_T] = FSharpList_get_Empty()
    node : FSharpList[_T] = root
    def action(xs: FSharpList[_T], lists: IEnumerable[FSharpList[_T]]=lists) -> None:
        nonlocal node
        def arrow_78(acc: FSharpList[_T], x: _T, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
            t : FSharpList[_T] = FSharpList(x, None)
            acc.tail = t
            return t

        node = fold(arrow_78, node, xs)

    if is_array_like(lists):
        iterate_1(action, lists)

    elif isinstance(lists, FSharpList):
        iterate(action, lists)

    else: 
        with get_enumerator(lists) as enumerator:
            while enumerator.System_Collections_IEnumerator_MoveNext():
                action(enumerator.System_Collections_Generic_IEnumerator_00601_get_Current())

    xs_6 : FSharpList[_T] = node
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    xs_6.tail = t_2
    return FSharpList__get_Tail(root)


def scan(folder: Any, state: _STATE, xs: FSharpList[_T]) -> FSharpList[_STATE]:
    root : FSharpList[_STATE] = FSharpList_get_Empty()
    node : FSharpList[_STATE]
    t : FSharpList[_STATE] = FSharpList(state, None)
    root.tail = t
    node = t
    acc : _STATE = state
    xs_3 : FSharpList[_T] = xs
    while not FSharpList__get_IsEmpty(xs_3):
        acc = folder(acc, FSharpList__get_Head(xs_3))
        def arrow_79(folder: Any=folder, state: _STATE=state, xs: FSharpList[_T]=xs) -> FSharpList[_STATE]:
            xs_4 : FSharpList[_STATE] = node
            t_2 : FSharpList[_STATE] = FSharpList(acc, None)
            xs_4.tail = t_2
            return t_2

        node = arrow_79()
        xs_3 = FSharpList__get_Tail(xs_3)
    xs_6 : FSharpList[_STATE] = node
    t_4 : FSharpList[_STATE] = FSharpList_get_Empty()
    xs_6.tail = t_4
    return FSharpList__get_Tail(root)


def scan_back(folder: Any, xs: FSharpList[_T], state: _STATE) -> FSharpList[_STATE]:
    return of_array(scan_back_1(folder, to_array(xs), state, None))


def append(xs: FSharpList[_T], ys: FSharpList[_T]) -> FSharpList[_T]:
    def arrow_80(acc: FSharpList[_T], x: _T, xs: FSharpList[_T]=xs, ys: FSharpList[_T]=ys) -> FSharpList[_T]:
        return FSharpList_Cons_305B8EAC(x, acc)

    return fold(arrow_80, ys, reverse(xs))


def collect(mapping: Callable[[_T], FSharpList[_U]], xs: FSharpList[_T]) -> FSharpList[_U]:
    root : FSharpList[_U] = FSharpList_get_Empty()
    node : FSharpList[_U] = root
    ys : FSharpList[_T] = xs
    while not FSharpList__get_IsEmpty(ys):
        zs : FSharpList[_U] = mapping(FSharpList__get_Head(ys))
        while not FSharpList__get_IsEmpty(zs):
            def arrow_81(mapping: Callable[[_T], FSharpList[_U]]=mapping, xs: FSharpList[_T]=xs) -> FSharpList[_U]:
                xs_1 : FSharpList[_U] = node
                t : FSharpList[_U] = FSharpList(FSharpList__get_Head(zs), None)
                xs_1.tail = t
                return t

            node = arrow_81()
            zs = FSharpList__get_Tail(zs)
        ys = FSharpList__get_Tail(ys)
    xs_3 : FSharpList[_U] = node
    t_2 : FSharpList[_U] = FSharpList_get_Empty()
    xs_3.tail = t_2
    return FSharpList__get_Tail(root)


def map_indexed(mapping: Any, xs: FSharpList[_T]) -> FSharpList[_U]:
    root : FSharpList[_U] = FSharpList_get_Empty()
    def folder(i: int, acc: FSharpList[_U], x: _T, mapping: Any=mapping, xs: FSharpList[_T]=xs) -> FSharpList[_U]:
        t : FSharpList[_U] = FSharpList(mapping(i, x), None)
        acc.tail = t
        return t

    node : FSharpList[_U] = fold_indexed(folder, root, xs)
    t_2 : FSharpList[_U] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def map(mapping: Callable[[_T], _U], xs: FSharpList[_T]) -> FSharpList[_U]:
    root : FSharpList[_U] = FSharpList_get_Empty()
    def folder(acc: FSharpList[_U], x: _T, mapping: Callable[[_T], _U]=mapping, xs: FSharpList[_T]=xs) -> FSharpList[_U]:
        t : FSharpList[_U] = FSharpList(mapping(x), None)
        acc.tail = t
        return t

    node : FSharpList[_U] = fold(folder, root, xs)
    t_2 : FSharpList[_U] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def indexed(xs: FSharpList[__A]) -> FSharpList[Tuple[int, __A]]:
    def arrow_82(i: int, x: __A, xs: FSharpList[__A]=xs) -> Tuple[int, __A]:
        return (i, x)

    return map_indexed(arrow_82, xs)


def map2(mapping: Any, xs: FSharpList[_T1], ys: FSharpList[_T2]) -> FSharpList[_U]:
    root : FSharpList[_U] = FSharpList_get_Empty()
    def folder(acc: FSharpList[_U], x: _T1, y: _T2, mapping: Any=mapping, xs: FSharpList[_T1]=xs, ys: FSharpList[_T2]=ys) -> FSharpList[_U]:
        t : FSharpList[_U] = FSharpList(mapping(x, y), None)
        acc.tail = t
        return t

    node : FSharpList[_U] = fold2(folder, root, xs, ys)
    t_2 : FSharpList[_U] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def map_indexed2(mapping: Any, xs: FSharpList[_T1], ys: FSharpList[_T2]) -> FSharpList[_U]:
    def loop(i_mut: int, acc_mut: FSharpList[_U], xs_1_mut: FSharpList[_T1], ys_1_mut: FSharpList[_T2], mapping: Any=mapping, xs: FSharpList[_T1]=xs, ys: FSharpList[_T2]=ys) -> FSharpList[_U]:
        while True:
            (i, acc, xs_1, ys_1) = (i_mut, acc_mut, xs_1_mut, ys_1_mut)
            if True if FSharpList__get_IsEmpty(xs_1) else FSharpList__get_IsEmpty(ys_1):
                return acc

            else: 
                i_mut = i + 1
                def arrow_83(i: int=i, acc: FSharpList[_U]=acc, xs_1: FSharpList[_T1]=xs_1, ys_1: FSharpList[_T2]=ys_1) -> FSharpList[_U]:
                    t : FSharpList[_U] = FSharpList(mapping(i, FSharpList__get_Head(xs_1), FSharpList__get_Head(ys_1)), None)
                    acc.tail = t
                    return t

                acc_mut = arrow_83()
                xs_1_mut = FSharpList__get_Tail(xs_1)
                ys_1_mut = FSharpList__get_Tail(ys_1)
                continue

            break

    root : FSharpList[_U] = FSharpList_get_Empty()
    node_1 : FSharpList[_U] = loop(0, root, xs, ys)
    t_2 : FSharpList[_U] = FSharpList_get_Empty()
    node_1.tail = t_2
    return FSharpList__get_Tail(root)


def map3(mapping: Any, xs: FSharpList[_T1], ys: FSharpList[_T2], zs: FSharpList[_T3]) -> FSharpList[_U]:
    def loop(acc_mut: FSharpList[_U], xs_1_mut: FSharpList[_T1], ys_1_mut: FSharpList[_T2], zs_1_mut: FSharpList[_T3], mapping: Any=mapping, xs: FSharpList[_T1]=xs, ys: FSharpList[_T2]=ys, zs: FSharpList[_T3]=zs) -> FSharpList[_U]:
        while True:
            (acc, xs_1, ys_1, zs_1) = (acc_mut, xs_1_mut, ys_1_mut, zs_1_mut)
            if True if (True if FSharpList__get_IsEmpty(xs_1) else FSharpList__get_IsEmpty(ys_1)) else FSharpList__get_IsEmpty(zs_1):
                return acc

            else: 
                def arrow_84(acc: FSharpList[_U]=acc, xs_1: FSharpList[_T1]=xs_1, ys_1: FSharpList[_T2]=ys_1, zs_1: FSharpList[_T3]=zs_1) -> FSharpList[_U]:
                    t : FSharpList[_U] = FSharpList(mapping(FSharpList__get_Head(xs_1), FSharpList__get_Head(ys_1), FSharpList__get_Head(zs_1)), None)
                    acc.tail = t
                    return t

                acc_mut = arrow_84()
                xs_1_mut = FSharpList__get_Tail(xs_1)
                ys_1_mut = FSharpList__get_Tail(ys_1)
                zs_1_mut = FSharpList__get_Tail(zs_1)
                continue

            break

    root : FSharpList[_U] = FSharpList_get_Empty()
    node_1 : FSharpList[_U] = loop(root, xs, ys, zs)
    t_2 : FSharpList[_U] = FSharpList_get_Empty()
    node_1.tail = t_2
    return FSharpList__get_Tail(root)


def map_fold(mapping: Any, state: _STATE, xs: FSharpList[_T]) -> Tuple[FSharpList[_RESULT], _STATE]:
    def folder(tupled_arg: Tuple[FSharpList[_RESULT], _STATE], x: _T, mapping: Any=mapping, state: _STATE=state, xs: FSharpList[_T]=xs) -> Tuple[FSharpList[_RESULT], _STATE]:
        pattern_input : Tuple[_RESULT, _STATE] = mapping(tupled_arg[1], x)
        def arrow_85(tupled_arg: Tuple[FSharpList[_RESULT], _STATE]=tupled_arg, x: _T=x) -> FSharpList[_RESULT]:
            t : FSharpList[_RESULT] = FSharpList(pattern_input[0], None)
            tupled_arg[0].tail = t
            return t

        return (arrow_85(), pattern_input[1])

    root : FSharpList[_RESULT] = FSharpList_get_Empty()
    pattern_input_1 : Tuple[FSharpList[_RESULT], _STATE] = fold(folder, (root, state), xs)
    t_2 : FSharpList[_RESULT] = FSharpList_get_Empty()
    pattern_input_1[0].tail = t_2
    return (FSharpList__get_Tail(root), pattern_input_1[1])


def map_fold_back(mapping: Any, xs: FSharpList[_T], state: _STATE) -> Tuple[FSharpList[_RESULT], _STATE]:
    def arrow_86(acc: _STATE, x: _T, mapping: Any=mapping, xs: FSharpList[_T]=xs, state: _STATE=state) -> Tuple[_RESULT, _STATE]:
        return mapping(x, acc)

    return map_fold(arrow_86, state, reverse(xs))


def try_pick(f: Callable[[_T], Optional[__A]], xs: FSharpList[_T]) -> Optional[__A]:
    def loop(xs_1_mut: FSharpList[_T], f: Callable[[_T], Optional[__A]]=f, xs: FSharpList[_T]=xs) -> Optional[__A]:
        while True:
            (xs_1,) = (xs_1_mut,)
            if FSharpList__get_IsEmpty(xs_1):
                return None

            else: 
                match_value : Optional[__A] = f(FSharpList__get_Head(xs_1))
                if match_value is None:
                    xs_1_mut = FSharpList__get_Tail(xs_1)
                    continue

                else: 
                    return match_value


            break

    return loop(xs)


def pick(f: Callable[[__A], Optional[__B]], xs: FSharpList[__A]) -> __B:
    match_value : Optional[__B] = try_pick(f, xs)
    if match_value is None:
        raise Exception(SR_keyNotFoundAlt)

    else: 
        return value_1(match_value)



def try_find(f: Callable[[__A], bool], xs: FSharpList[__A]) -> Optional[__A]:
    def arrow_87(x: Optional[__A]=None, f: Callable[[__A], bool]=f, xs: FSharpList[__A]=xs) -> Optional[__A]:
        return some(x) if f(x) else None

    return try_pick(arrow_87, xs)


def find(f: Callable[[__A], bool], xs: FSharpList[__A]) -> __A:
    match_value : Optional[__A] = try_find(f, xs)
    if match_value is None:
        raise Exception(SR_keyNotFoundAlt)

    else: 
        return value_1(match_value)



def try_find_back(f: Callable[[__A], bool], xs: FSharpList[__A]) -> Optional[__A]:
    return try_find_back_1(f, to_array(xs))


def find_back(f: Callable[[__A], bool], xs: FSharpList[__A]) -> __A:
    match_value : Optional[__A] = try_find_back(f, xs)
    if match_value is None:
        raise Exception(SR_keyNotFoundAlt)

    else: 
        return value_1(match_value)



def try_find_index(f: Callable[[_T], bool], xs: FSharpList[_T]) -> Optional[int]:
    def loop(i_mut: int, xs_1_mut: FSharpList[_T], f: Callable[[_T], bool]=f, xs: FSharpList[_T]=xs) -> Optional[int]:
        while True:
            (i, xs_1) = (i_mut, xs_1_mut)
            if FSharpList__get_IsEmpty(xs_1):
                return None

            elif f(FSharpList__get_Head(xs_1)):
                return i

            else: 
                i_mut = i + 1
                xs_1_mut = FSharpList__get_Tail(xs_1)
                continue

            break

    return loop(0, xs)


def find_index(f: Callable[[__A], bool], xs: FSharpList[__A]) -> int:
    match_value : Optional[int] = try_find_index(f, xs)
    if match_value is None:
        raise Exception(SR_keyNotFoundAlt)

    else: 
        return match_value



def try_find_index_back(f: Callable[[__A], bool], xs: FSharpList[__A]) -> Optional[int]:
    return try_find_index_back_1(f, to_array(xs))


def find_index_back(f: Callable[[__A], bool], xs: FSharpList[__A]) -> int:
    match_value : Optional[int] = try_find_index_back(f, xs)
    if match_value is None:
        raise Exception(SR_keyNotFoundAlt)

    else: 
        return match_value



def try_item(n: int, xs: FSharpList[_T]) -> Optional[_T]:
    def loop(i_mut: int, xs_1_mut: FSharpList[_T], n: int=n, xs: FSharpList[_T]=xs) -> Optional[_T]:
        while True:
            (i, xs_1) = (i_mut, xs_1_mut)
            if FSharpList__get_IsEmpty(xs_1):
                return None

            elif i == n:
                return some(FSharpList__get_Head(xs_1))

            else: 
                i_mut = i + 1
                xs_1_mut = FSharpList__get_Tail(xs_1)
                continue

            break

    return loop(0, xs)


def item(n: int, xs: FSharpList[_T]) -> _T:
    return FSharpList__get_Item_Z524259A4(xs, n)


def filter(f: Callable[[_T], bool], xs: FSharpList[_T]) -> FSharpList[_T]:
    root : FSharpList[_T] = FSharpList_get_Empty()
    def folder(acc: FSharpList[_T], x: _T, f: Callable[[_T], bool]=f, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        if f(x):
            t : FSharpList[_T] = FSharpList(x, None)
            acc.tail = t
            return t

        else: 
            return acc


    node : FSharpList[_T] = fold(folder, root, xs)
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def partition(f: Callable[[_T], bool], xs: FSharpList[_T]) -> Tuple[FSharpList[_T], FSharpList[_T]]:
    pattern_input : Tuple[FSharpList[_T], FSharpList[_T]] = (FSharpList_get_Empty(), FSharpList_get_Empty())
    root2 : FSharpList[_T] = pattern_input[1]
    root1 : FSharpList[_T] = pattern_input[0]
    def folder(tupled_arg: Tuple[FSharpList[_T], FSharpList[_T]], x: _T, f: Callable[[_T], bool]=f, xs: FSharpList[_T]=xs) -> Tuple[FSharpList[_T], FSharpList[_T]]:
        lacc : FSharpList[_T] = tupled_arg[0]
        racc : FSharpList[_T] = tupled_arg[1]
        if f(x):
            def arrow_88(tupled_arg: Tuple[FSharpList[_T], FSharpList[_T]]=tupled_arg, x: _T=x) -> FSharpList[_T]:
                t : FSharpList[_T] = FSharpList(x, None)
                lacc.tail = t
                return t

            return (arrow_88(), racc)

        else: 
            def arrow_89(tupled_arg: Tuple[FSharpList[_T], FSharpList[_T]]=tupled_arg, x: _T=x) -> FSharpList[_T]:
                t_2 : FSharpList[_T] = FSharpList(x, None)
                racc.tail = t_2
                return t_2

            return (lacc, arrow_89())


    pattern_input_1 : Tuple[FSharpList[_T], FSharpList[_T]] = fold(folder, (root1, root2), xs)
    t_4 : FSharpList[_T] = FSharpList_get_Empty()
    pattern_input_1[0].tail = t_4
    t_5 : FSharpList[_T] = FSharpList_get_Empty()
    pattern_input_1[1].tail = t_5
    return (FSharpList__get_Tail(root1), FSharpList__get_Tail(root2))


def choose(f: Callable[[_T], Optional[_T]], xs: FSharpList[_T]) -> FSharpList[_T]:
    root : FSharpList[_T] = FSharpList_get_Empty()
    def folder(acc: FSharpList[_T], x: _T, f: Callable[[_T], Optional[_T]]=f, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        match_value : Optional[_T] = f(x)
        if match_value is None:
            return acc

        else: 
            t : FSharpList[_T] = FSharpList(value_1(match_value), None)
            acc.tail = t
            return t


    node : FSharpList[_T] = fold(folder, root, xs)
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def contains(value: _T, xs: FSharpList[_T], eq: IEqualityComparer[Any]) -> bool:
    def arrow_90(v: Optional[_T]=None, value: _T=value, xs: FSharpList[_T]=xs, eq: IEqualityComparer[Any]=eq) -> bool:
        return eq.Equals(value, v)

    return try_find_index(arrow_90, xs) is not None


def initialize(n: int, f: Callable[[int], _T]) -> FSharpList[_T]:
    root : FSharpList[_T] = FSharpList_get_Empty()
    node : FSharpList[_T] = root
    for i in range(0, (n - 1) + 1, 1):
        def arrow_91(n: int=n, f: Callable[[int], _T]=f) -> FSharpList[_T]:
            xs : FSharpList[_T] = node
            t : FSharpList[_T] = FSharpList(f(i), None)
            xs.tail = t
            return t

        node = arrow_91()
    xs_2 : FSharpList[_T] = node
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    xs_2.tail = t_2
    return FSharpList__get_Tail(root)


def replicate(n: int, x: __A) -> FSharpList[__A]:
    def arrow_92(_arg: int, n: int=n, x: __A=x) -> __A:
        return x

    return initialize(n, arrow_92)


def reduce(f: Any, xs: FSharpList[_T]) -> _T:
    if FSharpList__get_IsEmpty(xs):
        raise Exception(SR_inputWasEmpty)

    else: 
        return fold(f, head(xs), tail(xs))



def reduce_back(f: Any, xs: FSharpList[_T]) -> _T:
    if FSharpList__get_IsEmpty(xs):
        raise Exception(SR_inputWasEmpty)

    else: 
        return fold_back(f, tail(xs), head(xs))



def for_all(f: Callable[[__A], bool], xs: FSharpList[__A]) -> bool:
    def arrow_112(acc: bool, x: __A, f: Callable[[__A], bool]=f, xs: FSharpList[__A]=xs) -> bool:
        return f(x) if acc else False

    return fold(arrow_112, True, xs)


def for_all2(f: Any, xs: FSharpList[__A], ys: FSharpList[__B]) -> bool:
    def arrow_113(acc: bool, x: __A, y: __B, f: Any=f, xs: FSharpList[__A]=xs, ys: FSharpList[__B]=ys) -> bool:
        return f(x, y) if acc else False

    return fold2(arrow_113, True, xs, ys)


def exists(f: Callable[[__A], bool], xs: FSharpList[__A]) -> bool:
    return try_find_index(f, xs) is not None


def exists2(f_mut: Any, xs_mut: FSharpList[_T1], ys_mut: FSharpList[_T2]) -> bool:
    while True:
        (f, xs, ys) = (f_mut, xs_mut, ys_mut)
        matchValue : bool = FSharpList__get_IsEmpty(xs)
        matchValue_1 : bool = FSharpList__get_IsEmpty(ys)
        (pattern_matching_result,) = (None,)
        if matchValue:
            if matchValue_1:
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 2


        elif matchValue_1:
            pattern_matching_result = 2

        else: 
            pattern_matching_result = 1

        if pattern_matching_result == 0:
            return False

        elif pattern_matching_result == 1:
            if f(FSharpList__get_Head(xs), FSharpList__get_Head(ys)):
                return True

            else: 
                f_mut = f
                xs_mut = FSharpList__get_Tail(xs)
                ys_mut = FSharpList__get_Tail(ys)
                continue


        elif pattern_matching_result == 2:
            raise Exception((SR_differentLengths + "\\nParameter name: ") + "list2")

        break


def unzip(xs: FSharpList[Tuple[__A, __B]]) -> Tuple[FSharpList[__A], FSharpList[__B]]:
    def arrow_114(tupled_arg: Tuple[__A, __B], tupled_arg_1: Tuple[FSharpList[__A], FSharpList[__B]], xs: FSharpList[Tuple[__A, __B]]=xs) -> Tuple[FSharpList[__A], FSharpList[__B]]:
        return (FSharpList_Cons_305B8EAC(tupled_arg[0], tupled_arg_1[0]), FSharpList_Cons_305B8EAC(tupled_arg[1], tupled_arg_1[1]))

    return fold_back(arrow_114, xs, (FSharpList_get_Empty(), FSharpList_get_Empty()))


def unzip3(xs: FSharpList[Tuple[__A, __B, __C]]) -> Tuple[FSharpList[__A], FSharpList[__B], FSharpList[__C]]:
    def arrow_115(tupled_arg: Tuple[__A, __B, __C], tupled_arg_1: Tuple[FSharpList[__A], FSharpList[__B], FSharpList[__C]], xs: FSharpList[Tuple[__A, __B, __C]]=xs) -> Tuple[FSharpList[__A], FSharpList[__B], FSharpList[__C]]:
        return (FSharpList_Cons_305B8EAC(tupled_arg[0], tupled_arg_1[0]), FSharpList_Cons_305B8EAC(tupled_arg[1], tupled_arg_1[1]), FSharpList_Cons_305B8EAC(tupled_arg[2], tupled_arg_1[2]))

    return fold_back(arrow_115, xs, (FSharpList_get_Empty(), FSharpList_get_Empty(), FSharpList_get_Empty()))


def zip(xs: FSharpList[__A], ys: FSharpList[__B]) -> FSharpList[Tuple[__A, __B]]:
    def arrow_116(x: __A, y: __B, xs: FSharpList[__A]=xs, ys: FSharpList[__B]=ys) -> Tuple[__A, __B]:
        return (x, y)

    return map2(arrow_116, xs, ys)


def zip3(xs: FSharpList[__A], ys: FSharpList[__B], zs: FSharpList[__C]) -> FSharpList[Tuple[__A, __B, __C]]:
    def arrow_117(x: __A, y: __B, z: __C, xs: FSharpList[__A]=xs, ys: FSharpList[__B]=ys, zs: FSharpList[__C]=zs) -> Tuple[__A, __B, __C]:
        return (x, y, z)

    return map3(arrow_117, xs, ys, zs)


def sort_with(comparer: Any, xs: FSharpList[_T]) -> FSharpList[_T]:
    arr : Array[_T] = to_array(xs)
    arr.sort()
    return of_array(arr)


def sort(xs: FSharpList[_T], comparer: IComparer[_T]) -> FSharpList[_T]:
    def arrow_118(x: _T, y: _T, xs: FSharpList[_T]=xs, comparer: IComparer[_T]=comparer) -> int:
        return comparer.Compare(x, y)

    return sort_with(arrow_118, xs)


def sort_by(projection: Callable[[_T], _U], xs: FSharpList[_T], comparer: IComparer[_U]) -> FSharpList[_T]:
    def arrow_119(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: FSharpList[_T]=xs, comparer: IComparer[_U]=comparer) -> int:
        return comparer.Compare(projection(x), projection(y))

    return sort_with(arrow_119, xs)


def sort_descending(xs: FSharpList[_T], comparer: IComparer[_T]) -> FSharpList[_T]:
    def arrow_120(x: _T, y: _T, xs: FSharpList[_T]=xs, comparer: IComparer[_T]=comparer) -> int:
        return comparer.Compare(x, y) * -1

    return sort_with(arrow_120, xs)


def sort_by_descending(projection: Callable[[_T], _U], xs: FSharpList[_T], comparer: IComparer[_U]) -> FSharpList[_T]:
    def arrow_121(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: FSharpList[_T]=xs, comparer: IComparer[_U]=comparer) -> int:
        return comparer.Compare(projection(x), projection(y)) * -1

    return sort_with(arrow_121, xs)


def sum(xs: FSharpList[_T], adder: IGenericAdder_1[_T]) -> _T:
    def arrow_122(acc: _T, x: _T, xs: FSharpList[_T]=xs, adder: IGenericAdder_1[_T]=adder) -> _T:
        return adder.Add(acc, x)

    return fold(arrow_122, adder.GetZero(), xs)


def sum_by(f: Callable[[_T], _U], xs: FSharpList[_T], adder: IGenericAdder_1[_U]) -> _U:
    def arrow_123(acc: _U, x: _T, f: Callable[[_T], _U]=f, xs: FSharpList[_T]=xs, adder: IGenericAdder_1[_U]=adder) -> _U:
        return adder.Add(acc, f(x))

    return fold(arrow_123, adder.GetZero(), xs)


def max_by(projection: Callable[[_T], _U], xs: FSharpList[_T], comparer: IComparer[_U]) -> _T:
    def arrow_124(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: FSharpList[_T]=xs, comparer: IComparer[_U]=comparer) -> _T:
        return y if (comparer.Compare(projection(y), projection(x)) > 0) else x

    return reduce(arrow_124, xs)


def max(xs: FSharpList[_T], comparer: IComparer[_T]) -> _T:
    def arrow_125(x: _T, y: _T, xs: FSharpList[_T]=xs, comparer: IComparer[_T]=comparer) -> _T:
        return y if (comparer.Compare(y, x) > 0) else x

    return reduce(arrow_125, xs)


def min_by(projection: Callable[[_T], _U], xs: FSharpList[_T], comparer: IComparer[_U]) -> _T:
    def arrow_126(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: FSharpList[_T]=xs, comparer: IComparer[_U]=comparer) -> _T:
        return x if (comparer.Compare(projection(y), projection(x)) > 0) else y

    return reduce(arrow_126, xs)


def min(xs: FSharpList[_T], comparer: IComparer[_T]) -> _T:
    def arrow_127(x: _T, y: _T, xs: FSharpList[_T]=xs, comparer: IComparer[_T]=comparer) -> _T:
        return x if (comparer.Compare(y, x) > 0) else y

    return reduce(arrow_127, xs)


def average(xs: FSharpList[_T], averager: IGenericAverager_1[_T]) -> _T:
    count : int = 0
    def folder(acc: _T, x: _T, xs: FSharpList[_T]=xs, averager: IGenericAverager_1[_T]=averager) -> _T:
        nonlocal count
        count = (count + 1) or 0
        return averager.Add(acc, x)

    total : _T = fold(folder, averager.GetZero(), xs)
    return averager.DivideByInt(total, count)


def average_by(f: Callable[[_T], _U], xs: FSharpList[_T], averager: IGenericAverager_1[_U]) -> _U:
    count : int = 0
    def arrow_128(acc: _U, x: _T, f: Callable[[_T], _U]=f, xs: FSharpList[_T]=xs, averager: IGenericAverager_1[_U]=averager) -> _U:
        nonlocal count
        count = (count + 1) or 0
        return averager.Add(acc, f(x))

    total : _U = fold(arrow_128, averager.GetZero(), xs)
    return averager.DivideByInt(total, count)


def permute(f: Callable[[int], int], xs: FSharpList[_T]) -> FSharpList[_T]:
    return of_array(permute_1(f, to_array(xs)))


def chunk_by_size(chunk_size: int, xs: FSharpList[_T]) -> FSharpList[FSharpList[_T]]:
    def mapping(xs_1: Array[_T], chunk_size: int=chunk_size, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        return of_array(xs_1)

    return of_array(map_1(mapping, chunk_by_size_1(chunk_size, to_array(xs)), None))


def all_pairs(xs: FSharpList[_T1], ys: FSharpList[_T2]) -> FSharpList[Tuple[_T1, _T2]]:
    root : FSharpList[Tuple[_T1, _T2]] = FSharpList_get_Empty()
    node : FSharpList[Tuple[_T1, _T2]] = root
    def arrow_131(x: Optional[_T1]=None, xs: FSharpList[_T1]=xs, ys: FSharpList[_T2]=ys) -> None:
        def arrow_130(y: Optional[_T2]=None) -> None:
            nonlocal node
            def arrow_129(__unit: Any=None) -> FSharpList[Tuple[_T1, _T2]]:
                xs_1 : FSharpList[Tuple[_T1, _T2]] = node
                t : FSharpList[Tuple[_T1, _T2]] = FSharpList((x, y), None)
                xs_1.tail = t
                return t

            node = arrow_129()

        iterate(arrow_130, ys)

    iterate(arrow_131, xs)
    xs_3 : FSharpList[Tuple[_T1, _T2]] = node
    t_2 : FSharpList[Tuple[_T1, _T2]] = FSharpList_get_Empty()
    xs_3.tail = t_2
    return FSharpList__get_Tail(root)


def skip(count_mut: int, xs_mut: FSharpList[_T]) -> FSharpList[_T]:
    while True:
        (count, xs) = (count_mut, xs_mut)
        if count <= 0:
            return xs

        elif FSharpList__get_IsEmpty(xs):
            raise Exception((SR_notEnoughElements + "\\nParameter name: ") + "list")

        else: 
            count_mut = count - 1
            xs_mut = FSharpList__get_Tail(xs)
            continue

        break


def skip_while(predicate_mut: Callable[[_T], bool], xs_mut: FSharpList[_T]) -> FSharpList[_T]:
    while True:
        (predicate, xs) = (predicate_mut, xs_mut)
        if FSharpList__get_IsEmpty(xs):
            return xs

        elif not predicate(FSharpList__get_Head(xs)):
            return xs

        else: 
            predicate_mut = predicate
            xs_mut = FSharpList__get_Tail(xs)
            continue

        break


def take(count: int, xs: FSharpList[_T]) -> FSharpList[_T]:
    if count < 0:
        raise Exception((SR_inputMustBeNonNegative + "\\nParameter name: ") + "count")

    def loop(i_mut: int, acc_mut: FSharpList[_T], xs_1_mut: FSharpList[_T], count: int=count, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        while True:
            (i, acc, xs_1) = (i_mut, acc_mut, xs_1_mut)
            if i <= 0:
                return acc

            elif FSharpList__get_IsEmpty(xs_1):
                raise Exception((SR_notEnoughElements + "\\nParameter name: ") + "list")

            else: 
                i_mut = i - 1
                def arrow_132(i: int=i, acc: FSharpList[_T]=acc, xs_1: FSharpList[_T]=xs_1) -> FSharpList[_T]:
                    t : FSharpList[_T] = FSharpList(FSharpList__get_Head(xs_1), None)
                    acc.tail = t
                    return t

                acc_mut = arrow_132()
                xs_1_mut = FSharpList__get_Tail(xs_1)
                continue

            break

    root : FSharpList[_T] = FSharpList_get_Empty()
    node : FSharpList[_T] = loop(count, root, xs)
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def take_while(predicate: Callable[[_T], bool], xs: FSharpList[_T]) -> FSharpList[_T]:
    def loop(acc_mut: FSharpList[_T], xs_1_mut: FSharpList[_T], predicate: Callable[[_T], bool]=predicate, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        while True:
            (acc, xs_1) = (acc_mut, xs_1_mut)
            if FSharpList__get_IsEmpty(xs_1):
                return acc

            elif not predicate(FSharpList__get_Head(xs_1)):
                return acc

            else: 
                def arrow_133(acc: FSharpList[_T]=acc, xs_1: FSharpList[_T]=xs_1) -> FSharpList[_T]:
                    t : FSharpList[_T] = FSharpList(FSharpList__get_Head(xs_1), None)
                    acc.tail = t
                    return t

                acc_mut = arrow_133()
                xs_1_mut = FSharpList__get_Tail(xs_1)
                continue

            break

    root : FSharpList[_T] = FSharpList_get_Empty()
    node : FSharpList[_T] = loop(root, xs)
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def truncate(count: int, xs: FSharpList[_T]) -> FSharpList[_T]:
    def loop(i_mut: int, acc_mut: FSharpList[_T], xs_1_mut: FSharpList[_T], count: int=count, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        while True:
            (i, acc, xs_1) = (i_mut, acc_mut, xs_1_mut)
            if i <= 0:
                return acc

            elif FSharpList__get_IsEmpty(xs_1):
                return acc

            else: 
                i_mut = i - 1
                def arrow_134(i: int=i, acc: FSharpList[_T]=acc, xs_1: FSharpList[_T]=xs_1) -> FSharpList[_T]:
                    t : FSharpList[_T] = FSharpList(FSharpList__get_Head(xs_1), None)
                    acc.tail = t
                    return t

                acc_mut = arrow_134()
                xs_1_mut = FSharpList__get_Tail(xs_1)
                continue

            break

    root : FSharpList[_T] = FSharpList_get_Empty()
    node : FSharpList[_T] = loop(count, root, xs)
    t_2 : FSharpList[_T] = FSharpList_get_Empty()
    node.tail = t_2
    return FSharpList__get_Tail(root)


def get_slice(start_index: Optional[int], end_index: Optional[int], xs: FSharpList[_T]) -> FSharpList[_T]:
    len_1 : int = length(xs) or 0
    start_index_1 : int = default_arg(start_index, 0) or 0
    end_index_1 : int = default_arg(end_index, len_1 - 1) or 0
    if start_index_1 < 0:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "startIndex")

    elif end_index_1 >= len_1:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "endIndex")

    elif end_index_1 < start_index_1:
        return FSharpList_get_Empty()

    else: 
        return take((end_index_1 - start_index_1) + 1, skip(start_index_1, xs))



def split_at(index: int, xs: FSharpList[_T]) -> Tuple[FSharpList[_T], FSharpList[_T]]:
    if index < 0:
        raise Exception((SR_inputMustBeNonNegative + "\\nParameter name: ") + "index")

    if index > FSharpList__get_Length(xs):
        raise Exception((SR_notEnoughElements + "\\nParameter name: ") + "index")

    return (take(index, xs), skip(index, xs))


def exactly_one(xs: FSharpList[_T]) -> _T:
    if FSharpList__get_IsEmpty(xs):
        raise Exception((SR_inputSequenceEmpty + "\\nParameter name: ") + "list")

    elif FSharpList__get_IsEmpty(FSharpList__get_Tail(xs)):
        return FSharpList__get_Head(xs)

    else: 
        raise Exception((SR_inputSequenceTooLong + "\\nParameter name: ") + "list")



def try_exactly_one(xs: FSharpList[_T]) -> Optional[_T]:
    if FSharpList__get_IsEmpty(FSharpList__get_Tail(xs)) if (not FSharpList__get_IsEmpty(xs)) else False:
        return some(FSharpList__get_Head(xs))

    else: 
        return None



def where(predicate: Callable[[_T], bool], xs: FSharpList[_T]) -> FSharpList[_T]:
    return filter(predicate, xs)


def pairwise(xs: FSharpList[_T]) -> FSharpList[Tuple[_T, _T]]:
    return of_array(pairwise_1(to_array(xs)))


def windowed(window_size: int, xs: FSharpList[_T]) -> FSharpList[FSharpList[_T]]:
    def mapping(xs_1: Array[_T], window_size: int=window_size, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        return of_array(xs_1)

    return of_array(map_1(mapping, windowed_1(window_size, to_array(xs)), None))


def split_into(chunks: int, xs: FSharpList[_T]) -> FSharpList[FSharpList[_T]]:
    def mapping(xs_1: Array[_T], chunks: int=chunks, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        return of_array(xs_1)

    return of_array(map_1(mapping, split_into_1(chunks, to_array(xs)), None))


def transpose(lists: IEnumerable[FSharpList[_T]]) -> FSharpList[FSharpList[_T]]:
    def mapping_1(xs_1: Array[_T], lists: IEnumerable[FSharpList[_T]]=lists) -> FSharpList[_T]:
        return of_array(xs_1)

    def mapping(xs: FSharpList[_T], lists: IEnumerable[FSharpList[_T]]=lists) -> Array[_T]:
        return to_array(xs)

    return of_array(map_1(mapping_1, transpose_1(map_1(mapping, list(lists), None), None), None))


def insert_at(index: int, y: _T, xs: FSharpList[_T]) -> FSharpList[_T]:
    i : int = -1
    is_done : bool = False
    def folder(acc: FSharpList[_T], x: _T, index: int=index, y: _T=y, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        nonlocal i, is_done
        i = (i + 1) or 0
        if i == index:
            is_done = True
            return FSharpList_Cons_305B8EAC(x, FSharpList_Cons_305B8EAC(y, acc))

        else: 
            return FSharpList_Cons_305B8EAC(x, acc)


    result : FSharpList[_T] = fold(folder, FSharpList_get_Empty(), xs)
    def arrow_135(index: int=index, y: _T=y, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    return reverse(result if is_done else (FSharpList_Cons_305B8EAC(y, result) if ((i + 1) == index) else arrow_135()))


def insert_many_at(index: int, ys: IEnumerable[_T], xs: FSharpList[_T]) -> FSharpList[_T]:
    i : int = -1
    is_done : bool = False
    ys_1 : FSharpList[_T] = of_seq(ys)
    def folder(acc: FSharpList[_T], x: _T, index: int=index, ys: IEnumerable[_T]=ys, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        nonlocal i, is_done
        i = (i + 1) or 0
        if i == index:
            is_done = True
            return FSharpList_Cons_305B8EAC(x, append(ys_1, acc))

        else: 
            return FSharpList_Cons_305B8EAC(x, acc)


    result : FSharpList[_T] = fold(folder, FSharpList_get_Empty(), xs)
    def arrow_136(index: int=index, ys: IEnumerable[_T]=ys, xs: FSharpList[_T]=xs) -> FSharpList[_T]:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    return reverse(result if is_done else (append(ys_1, result) if ((i + 1) == index) else arrow_136()))


def remove_at(index: int, xs: FSharpList[_T]) -> FSharpList[_T]:
    i : int = -1
    is_done : bool = False
    def f(_arg: Optional[_T]=None, index: int=index, xs: FSharpList[_T]=xs) -> bool:
        nonlocal i, is_done
        i = (i + 1) or 0
        if i == index:
            is_done = True
            return False

        else: 
            return True


    ys : FSharpList[_T] = filter(f, xs)
    if not is_done:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    return ys


def remove_many_at(index: int, count: int, xs: FSharpList[_T]) -> FSharpList[_T]:
    i : int = -1
    status : int = -1
    def f(_arg: Optional[_T]=None, index: int=index, count: int=count, xs: FSharpList[_T]=xs) -> bool:
        nonlocal i, status
        i = (i + 1) or 0
        if i == index:
            status = 0
            return False

        elif i > index:
            if i < (index + count):
                return False

            else: 
                status = 1
                return True


        else: 
            return True


    ys : FSharpList[_T] = filter(f, xs)
    status_1 : int = (1 if (((i + 1) == (index + count)) if (status == 0) else False) else status) or 0
    if status_1 < 1:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + ("index" if (status_1 < 0) else "count"))

    return ys


def update_at(index: int, y: _T, xs: FSharpList[_T]) -> FSharpList[_T]:
    is_done : bool = False
    def mapping(i: int, x: _T, index: int=index, y: _T=y, xs: FSharpList[_T]=xs) -> _T:
        nonlocal is_done
        if i == index:
            is_done = True
            return y

        else: 
            return x


    ys : FSharpList[_T] = map_indexed(mapping, xs)
    if not is_done:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    return ys


