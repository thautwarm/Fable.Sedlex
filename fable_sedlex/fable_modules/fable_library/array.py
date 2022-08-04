from __future__ import annotations
import builtins
import functools
import math
from typing import (TypeVar, Callable, Optional, Any, Tuple)
from .option import (some, default_arg, map as map_1, value as value_1)
from .types import Array
from .util import (max as max_1, compare_primitives, IEnumerable, IEqualityComparer, ignore, get_enumerator, equals as equals_1, IComparer, min as min_1)
from .native import (Cons_1, Helpers_allocateArrayFromCons, Helpers_fillImpl, Helpers_spliceImpl, Helpers_copyToTypedArray)
from .global_ import (SR_indexOutOfBounds, IGenericAdder_1, IGenericAverager_1)

__A = TypeVar("__A")

_T = TypeVar("_T")

_U = TypeVar("_U")

_T1 = TypeVar("_T1")

_T2 = TypeVar("_T2")

_T3 = TypeVar("_T3")

_STATE = TypeVar("_STATE")

_RESULT = TypeVar("_RESULT")

__B = TypeVar("__B")

_A = TypeVar("_A")

_B = TypeVar("_B")

__C = TypeVar("__C")

def index_not_found() -> __A:
    raise Exception("An index satisfying the predicate was not found in the collection.")


def different_lengths() -> __A:
    raise Exception("Arrays had different lengths")


def append(array1: Array[_T], array2: Array[_T], cons: Cons_1[_T]) -> Array[_T]:
    len1 : int = len(array1) or 0
    len2 : int = len(array2) or 0
    new_array : Array[_T] = Helpers_allocateArrayFromCons(cons, len1 + len2)
    for i in range(0, (len1 - 1) + 1, 1):
        new_array[i] = array1[i]
    for i_1 in range(0, (len2 - 1) + 1, 1):
        new_array[i_1 + len1] = array2[i_1]
    return new_array


def filter(predicate: Callable[[_T], bool], array: Array[_T]) -> Array[_T]:
    return list(builtins.filter(predicate, array))


def fill(target: Array[_T], target_index: int, count: int, value: _T) -> Array[_T]:
    return Helpers_fillImpl(target, value, target_index, count)


def get_sub_array(array: Array[_T], start: int, count: int) -> Array[_T]:
    return array[start:start+count]


def last(array: Array[_T]) -> _T:
    if len(array) == 0:
        raise Exception("The input array was empty\\nParameter name: array")

    return array[len(array) - 1]


def try_last(array: Array[_T]) -> Optional[_T]:
    if len(array) == 0:
        return None

    else: 
        return some(array[len(array) - 1])



def map_indexed(f: Any, source: Array[_T], cons: Cons_1[_U]) -> Array[_U]:
    len_1 : int = len(source) or 0
    target : Array[_U] = Helpers_allocateArrayFromCons(cons, len_1)
    for i in range(0, (len_1 - 1) + 1, 1):
        target[i] = f(i, source[i])
    return target


def map(f: Callable[[_T], _U], source: Array[_T], cons: Cons_1[_U]) -> Array[_U]:
    len_1 : int = len(source) or 0
    target : Array[_U] = Helpers_allocateArrayFromCons(cons, len_1)
    for i in range(0, (len_1 - 1) + 1, 1):
        target[i] = f(source[i])
    return target


def map_indexed2(f: Any, source1: Array[_T1], source2: Array[_T2], cons: Cons_1[_U]) -> Array[_U]:
    if len(source1) != len(source2):
        raise Exception("Arrays had different lengths")

    result : Array[_U] = Helpers_allocateArrayFromCons(cons, len(source1))
    for i in range(0, (len(source1) - 1) + 1, 1):
        result[i] = f(i, source1[i], source2[i])
    return result


def map2(f: Any, source1: Array[_T1], source2: Array[_T2], cons: Cons_1[_U]) -> Array[_U]:
    if len(source1) != len(source2):
        raise Exception("Arrays had different lengths")

    result : Array[_U] = Helpers_allocateArrayFromCons(cons, len(source1))
    for i in range(0, (len(source1) - 1) + 1, 1):
        result[i] = f(source1[i], source2[i])
    return result


def map_indexed3(f: Any, source1: Array[_T1], source2: Array[_T2], source3: Array[_T3], cons: Cons_1[_U]) -> Array[_U]:
    if True if (len(source1) != len(source2)) else (len(source2) != len(source3)):
        raise Exception("Arrays had different lengths")

    result : Array[_U] = Helpers_allocateArrayFromCons(cons, len(source1))
    for i in range(0, (len(source1) - 1) + 1, 1):
        result[i] = f(i, source1[i], source2[i], source3[i])
    return result


def map3(f: Any, source1: Array[_T1], source2: Array[_T2], source3: Array[_T3], cons: Cons_1[_U]) -> Array[_U]:
    if True if (len(source1) != len(source2)) else (len(source2) != len(source3)):
        raise Exception("Arrays had different lengths")

    result : Array[_U] = Helpers_allocateArrayFromCons(cons, len(source1))
    for i in range(0, (len(source1) - 1) + 1, 1):
        result[i] = f(source1[i], source2[i], source3[i])
    return result


def map_fold(mapping: Any, state: _STATE, array: Array[_T], cons: Cons_1[_RESULT]) -> Tuple[Array[_RESULT], _STATE]:
    match_value : int = len(array) or 0
    if match_value == 0:
        return ([], state)

    else: 
        acc : _STATE = state
        res : Array[_RESULT] = Helpers_allocateArrayFromCons(cons, match_value)
        for i in range(0, (len(array) - 1) + 1, 1):
            pattern_input : Tuple[_RESULT, _STATE] = mapping(acc, array[i])
            res[i] = pattern_input[0]
            acc = pattern_input[1]
        return (res, acc)



def map_fold_back(mapping: Any, array: Array[_T], state: _STATE, cons: Cons_1[_RESULT]) -> Tuple[Array[_RESULT], _STATE]:
    match_value : int = len(array) or 0
    if match_value == 0:
        return ([], state)

    else: 
        acc : _STATE = state
        res : Array[_RESULT] = Helpers_allocateArrayFromCons(cons, match_value)
        for i in range(len(array) - 1, 0 - 1, -1):
            pattern_input : Tuple[_RESULT, _STATE] = mapping(array[i], acc)
            res[i] = pattern_input[0]
            acc = pattern_input[1]
        return (res, acc)



def indexed(source: Array[_T]) -> Array[Tuple[int, _T]]:
    len_1 : int = len(source) or 0
    target : Array[Tuple[int, _T]] = [None]*len_1
    for i in range(0, (len_1 - 1) + 1, 1):
        target[i] = (i, source[i])
    return target


def truncate(count: int, array: Array[_T]) -> Array[_T]:
    def arrow_47(x: int, y: int, count: int=count, array: Array[_T]=array) -> int:
        return compare_primitives(x, y)

    count_1 : int = max_1(arrow_47, 0, count) or 0
    return array[0:0+count_1]


def concat(arrays: IEnumerable[Array[_T]], cons: Cons_1[_T]) -> Array[_T]:
    arrays_1 : Array[Array[_T]] = arrays if (isinstance(arrays, list)) else (list(arrays))
    match_value : int = len(arrays_1) or 0
    if match_value == 0:
        return Helpers_allocateArrayFromCons(cons, 0)

    elif match_value == 1:
        return arrays_1[0]

    else: 
        total_idx : int = 0
        total_length : int = 0
        for idx in range(0, (len(arrays_1) - 1) + 1, 1):
            arr_1 : Array[_T] = arrays_1[idx]
            total_length = (total_length + len(arr_1)) or 0
        result : Array[_T] = Helpers_allocateArrayFromCons(cons, total_length)
        for idx_1 in range(0, (len(arrays_1) - 1) + 1, 1):
            arr_2 : Array[_T] = arrays_1[idx_1]
            for j in range(0, (len(arr_2) - 1) + 1, 1):
                result[total_idx] = arr_2[j]
                total_idx = (total_idx + 1) or 0
        return result



def collect(mapping: Callable[[_T], Array[_U]], array: Array[_T], cons: Cons_1[_U]) -> Array[_U]:
    return concat(map(mapping, array, None), cons)


def where(predicate: Callable[[__A], bool], array: Array[__A]) -> Array[__A]:
    return list(builtins.filter(predicate, array))


def index_of(array: Array[_T], item_1: _T, start: Optional[int], count: Optional[int], eq: IEqualityComparer[Any]) -> int:
    start_1 : int = default_arg(start, 0) or 0
    def mapping(c: int, array: Array[_T]=array, item_1: _T=item_1, start: Optional[int]=start, count: Optional[int]=count, eq: IEqualityComparer[Any]=eq) -> int:
        return start_1 + c

    end_0027 : int = default_arg(map_1(mapping, count), len(array)) or 0
    def loop(i_mut: int, array: Array[_T]=array, item_1: _T=item_1, start: Optional[int]=start, count: Optional[int]=count, eq: IEqualityComparer[Any]=eq) -> int:
        while True:
            (i,) = (i_mut,)
            if i >= end_0027:
                return -1

            elif eq.Equals(item_1, array[i]):
                return i

            else: 
                i_mut = i + 1
                continue

            break

    return loop(start_1)


def contains(value: _T, array: Array[_T], eq: IEqualityComparer[Any]) -> bool:
    return index_of(array, value, None, None, eq) >= 0


def empty(cons: Cons_1[__A]) -> Array[__A]:
    return Helpers_allocateArrayFromCons(cons, 0)


def singleton(value: _T, cons: Cons_1[_T]) -> Array[_T]:
    ar : Array[_T] = Helpers_allocateArrayFromCons(cons, 1)
    ar[0] = value
    return ar


def initialize(count: int, initializer: Callable[[int], _T], cons: Cons_1[_T]) -> Array[_T]:
    if count < 0:
        raise Exception("The input must be non-negative\\nParameter name: count")

    result : Array[_T] = Helpers_allocateArrayFromCons(cons, count)
    for i in range(0, (count - 1) + 1, 1):
        result[i] = initializer(i)
    return result


def pairwise(array: Array[_T]) -> Array[Tuple[_T, _T]]:
    if len(array) < 2:
        return []

    else: 
        count : int = (len(array) - 1) or 0
        result : Array[Tuple[_T, _T]] = [None]*count
        for i in range(0, (count - 1) + 1, 1):
            result[i] = (array[i], array[i + 1])
        return result



def replicate(count: int, initial: _T, cons: Cons_1[_T]) -> Array[_T]:
    if count < 0:
        raise Exception("The input must be non-negative\\nParameter name: count")

    result : Array[_T] = Helpers_allocateArrayFromCons(cons, count)
    for i in range(0, (len(result) - 1) + 1, 1):
        result[i] = initial
    return result


def copy(array: Array[_T]) -> Array[_T]:
    return array[:]


def reverse(array: Array[_T]) -> Array[_T]:
    array_1 : Array[_T] = array[:]
    return array_1[::-1]


def scan(folder: Any, state: _STATE, array: Array[_T], cons: Cons_1[_STATE]) -> Array[_STATE]:
    res : Array[_STATE] = Helpers_allocateArrayFromCons(cons, len(array) + 1)
    res[0] = state
    for i in range(0, (len(array) - 1) + 1, 1):
        res[i + 1] = folder(res[i], array[i])
    return res


def scan_back(folder: Any, array: Array[_T], state: _STATE, cons: Cons_1[_STATE]) -> Array[_STATE]:
    res : Array[_STATE] = Helpers_allocateArrayFromCons(cons, len(array) + 1)
    res[len(array)] = state
    for i in range(len(array) - 1, 0 - 1, -1):
        res[i] = folder(array[i], res[i + 1])
    return res


def skip(count: int, array: Array[_T], cons: Cons_1[_T]) -> Array[_T]:
    if count > len(array):
        raise Exception("count is greater than array length\\nParameter name: count")

    if count == len(array):
        return Helpers_allocateArrayFromCons(cons, 0)

    else: 
        count_1 : int = (0 if (count < 0) else count) or 0
        return array[count_1:]



def skip_while(predicate: Callable[[_T], bool], array: Array[_T], cons: Cons_1[_T]) -> Array[_T]:
    count : int = 0
    while predicate(array[count]) if (count < len(array)) else False:
        count = (count + 1) or 0
    if count == len(array):
        return Helpers_allocateArrayFromCons(cons, 0)

    else: 
        return array[count:]



def take(count: int, array: Array[_T], cons: Cons_1[_T]) -> Array[_T]:
    if count < 0:
        raise Exception("The input must be non-negative\\nParameter name: count")

    if count > len(array):
        raise Exception("count is greater than array length\\nParameter name: count")

    if count == 0:
        return Helpers_allocateArrayFromCons(cons, 0)

    else: 
        return array[0:0+count]



def take_while(predicate: Callable[[_T], bool], array: Array[_T], cons: Cons_1[_T]) -> Array[_T]:
    count : int = 0
    while predicate(array[count]) if (count < len(array)) else False:
        count = (count + 1) or 0
    if count == 0:
        return Helpers_allocateArrayFromCons(cons, 0)

    else: 
        return array[0:0+count]



def add_in_place(x: _T, array: Array[_T]) -> None:
    ignore(array.append(x))


def add_range_in_place(range: IEnumerable[_T], array: Array[_T]) -> None:
    with get_enumerator(range) as enumerator:
        while enumerator.System_Collections_IEnumerator_MoveNext():
            add_in_place(enumerator.System_Collections_Generic_IEnumerator_00601_get_Current(), array)


def insert_range_in_place(index: int, range: IEnumerable[_T], array: Array[_T]) -> None:
    i : int = index or 0
    with get_enumerator(range) as enumerator:
        while enumerator.System_Collections_IEnumerator_MoveNext():
            x : _T = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
            def arrow_48(index: int=index, range: IEnumerable[_T]=range, array: Array[_T]=array) -> Array[_T]:
                index_1 : int = i or 0
                return array.insert(index_1, x)

            ignore(arrow_48())
            i = (i + 1) or 0


def remove_in_place(item_1: _T, array: Array[_T], eq: IEqualityComparer[Any]) -> bool:
    i : int = index_of(array, item_1, None, None, eq) or 0
    if i > -1:
        ignore(Helpers_spliceImpl(array, i, 1))
        return True

    else: 
        return False



def remove_all_in_place(predicate: Callable[[_T], bool], array: Array[_T]) -> int:
    def count_remove_all(count: int, predicate: Callable[[_T], bool]=predicate, array: Array[_T]=array) -> int:
        i : int = (next((i for i, x in enumerate(array) if (predicate)(x)), -1)) or 0
        if i > -1:
            ignore(Helpers_spliceImpl(array, i, 1))
            return count_remove_all(count) + 1

        else: 
            return count


    return count_remove_all(0)


def copy_to(source: Array[_T], source_index: int, target: Array[_T], target_index: int, count: int) -> None:
    diff : int = (target_index - source_index) or 0
    for i in range(source_index, ((source_index + count) - 1) + 1, 1):
        target[i + diff] = source[i]


def copy_to_typed_array(source: Array[_T], source_index: int, target: Array[_T], target_index: int, count: int) -> None:
    try: 
        Helpers_copyToTypedArray(source, source_index, target, target_index, count)

    except Exception as match_value:
        copy_to(source, source_index, target, target_index, count)



def partition(f: Callable[[_T], bool], source: Array[_T], cons: Cons_1[_T]) -> Tuple[Array[_T], Array[_T]]:
    len_1 : int = len(source) or 0
    res1 : Array[_T] = Helpers_allocateArrayFromCons(cons, len_1)
    res2 : Array[_T] = Helpers_allocateArrayFromCons(cons, len_1)
    i_true : int = 0
    i_false : int = 0
    for i in range(0, (len_1 - 1) + 1, 1):
        if f(source[i]):
            res1[i_true] = source[i]
            i_true = (i_true + 1) or 0

        else: 
            res2[i_false] = source[i]
            i_false = (i_false + 1) or 0

    return (truncate(i_true, res1), truncate(i_false, res2))


def find(predicate: Callable[[_T], bool], array: Array[_T]) -> _T:
    match_value : Optional[_T] = next((x for x in array if (predicate)(x)), None)
    if match_value is None:
        return index_not_found()

    else: 
        return value_1(match_value)



def try_find(predicate: Callable[[_T], bool], array: Array[_T]) -> Optional[_T]:
    return next((x for x in array if (predicate)(x)), None)


def find_index(predicate: Callable[[_T], bool], array: Array[_T]) -> int:
    match_value : int = (next((i for i, x in enumerate(array) if (predicate)(x)), -1)) or 0
    if match_value > -1:
        return match_value

    else: 
        return index_not_found()



def try_find_index(predicate: Callable[[_T], bool], array: Array[_T]) -> Optional[int]:
    match_value : int = (next((i for i, x in enumerate(array) if (predicate)(x)), -1)) or 0
    if match_value > -1:
        return match_value

    else: 
        return None



def pick(chooser: Callable[[__A], Optional[__B]], array: Array[__A]) -> __B:
    def loop(i_mut: int, chooser: Callable[[__A], Optional[__B]]=chooser, array: Array[__A]=array) -> __B:
        while True:
            (i,) = (i_mut,)
            if i >= len(array):
                return index_not_found()

            else: 
                match_value : Optional[__B] = chooser(array[i])
                if match_value is not None:
                    return value_1(match_value)

                else: 
                    i_mut = i + 1
                    continue


            break

    return loop(0)


def try_pick(chooser: Callable[[__A], Optional[__B]], array: Array[__A]) -> Optional[__B]:
    def loop(i_mut: int, chooser: Callable[[__A], Optional[__B]]=chooser, array: Array[__A]=array) -> Optional[__B]:
        while True:
            (i,) = (i_mut,)
            if i >= len(array):
                return None

            else: 
                match_value : Optional[__B] = chooser(array[i])
                if match_value is None:
                    i_mut = i + 1
                    continue

                else: 
                    return match_value


            break

    return loop(0)


def find_back(predicate: Callable[[__A], bool], array: Array[__A]) -> __A:
    def loop(i_mut: int, predicate: Callable[[__A], bool]=predicate, array: Array[__A]=array) -> __A:
        while True:
            (i,) = (i_mut,)
            if i < 0:
                return index_not_found()

            elif predicate(array[i]):
                return array[i]

            else: 
                i_mut = i - 1
                continue

            break

    return loop(len(array) - 1)


def try_find_back(predicate: Callable[[__A], bool], array: Array[__A]) -> Optional[__A]:
    def loop(i_mut: int, predicate: Callable[[__A], bool]=predicate, array: Array[__A]=array) -> Optional[__A]:
        while True:
            (i,) = (i_mut,)
            if i < 0:
                return None

            elif predicate(array[i]):
                return some(array[i])

            else: 
                i_mut = i - 1
                continue

            break

    return loop(len(array) - 1)


def find_last_index(predicate: Callable[[__A], bool], array: Array[__A]) -> int:
    def loop(i_mut: int, predicate: Callable[[__A], bool]=predicate, array: Array[__A]=array) -> int:
        while True:
            (i,) = (i_mut,)
            if i < 0:
                return -1

            elif predicate(array[i]):
                return i

            else: 
                i_mut = i - 1
                continue

            break

    return loop(len(array) - 1)


def find_index_back(predicate: Callable[[__A], bool], array: Array[__A]) -> int:
    def loop(i_mut: int, predicate: Callable[[__A], bool]=predicate, array: Array[__A]=array) -> int:
        while True:
            (i,) = (i_mut,)
            if i < 0:
                return index_not_found()

            elif predicate(array[i]):
                return i

            else: 
                i_mut = i - 1
                continue

            break

    return loop(len(array) - 1)


def try_find_index_back(predicate: Callable[[__A], bool], array: Array[__A]) -> Optional[int]:
    def loop(i_mut: int, predicate: Callable[[__A], bool]=predicate, array: Array[__A]=array) -> Optional[int]:
        while True:
            (i,) = (i_mut,)
            if i < 0:
                return None

            elif predicate(array[i]):
                return i

            else: 
                i_mut = i - 1
                continue

            break

    return loop(len(array) - 1)


def choose(chooser: Callable[[_T], Optional[_U]], array: Array[_T], cons: Cons_1[_U]) -> Array[_U]:
    res : Array[_U] = []
    for i in range(0, (len(array) - 1) + 1, 1):
        match_value : Optional[_U] = chooser(array[i])
        if match_value is not None:
            y : _U = value_1(match_value)
            ignore(res.append(y))

    if equals_1(cons, None):
        return res

    else: 
        def arrow_49(x: Optional[_U]=None, chooser: Callable[[_T], Optional[_U]]=chooser, array: Array[_T]=array, cons: Cons_1[_U]=cons) -> _U:
            return x

        return map(arrow_49, res, cons)



def fold_indexed(folder: Any, state: _STATE, array: Array[_T]) -> _STATE:
    def arrow_50(delegate_arg: _STATE, delegate_arg_1: _T, delegate_arg_2: int, folder: Any=folder, state: _STATE=state, array: Array[_T]=array) -> _STATE:
        return folder(delegate_arg_2, delegate_arg, delegate_arg_1)

    return array.reduce((arrow_50, state))


def fold(folder: Any, state: _STATE, array: Array[_T]) -> _STATE:
    def arrow_51(acc: _STATE, x: _T, folder: Any=folder, state: _STATE=state, array: Array[_T]=array) -> _STATE:
        return folder(acc, x)

    return functools.reduce(arrow_51, array, state)


def iterate(action: Callable[[_T], None], array: Array[_T]) -> None:
    for i in range(0, (len(array) - 1) + 1, 1):
        action(array[i])


def iterate_indexed(action: Any, array: Array[_T]) -> None:
    for i in range(0, (len(array) - 1) + 1, 1):
        action(i, array[i])


def iterate2(action: Any, array1: Array[_T], array2: Array[_T]) -> None:
    if len(array1) != len(array2):
        different_lengths()

    for i in range(0, (len(array1) - 1) + 1, 1):
        action(array1[i], array2[i])


def iterate_indexed2(action: Any, array1: Array[_T], array2: Array[_T]) -> None:
    if len(array1) != len(array2):
        different_lengths()

    for i in range(0, (len(array1) - 1) + 1, 1):
        action(i, array1[i], array2[i])


def is_empty(array: Array[_T]) -> bool:
    return len(array) == 0


def for_all(predicate: Callable[[_T], bool], array: Array[_T]) -> bool:
    return all([predicate(x) for x in array])


def permute(f: Callable[[int], int], array: Array[_T]) -> Array[_T]:
    size : int = len(array) or 0
    res : Array[_T] = array[:]
    check_flags : Array[int] = [None]*size
    def arrow_52(i: int, x: _T, f: Callable[[int], int]=f, array: Array[_T]=array) -> None:
        j : int = f(i) or 0
        if True if (j < 0) else (j >= size):
            raise Exception("Not a valid permutation")

        res[j] = x
        check_flags[j] = 1

    iterate_indexed(arrow_52, array)
    def predicate(y: int, f: Callable[[int], int]=f, array: Array[_T]=array) -> bool:
        return 1 == y

    if not (all([predicate(x) for x in check_flags])):
        raise Exception("Not a valid permutation")

    return res


def set_slice(target: Array[_T], lower: Optional[int], upper: Optional[int], source: Array[_T]) -> None:
    lower_1 : int = default_arg(lower, 0) or 0
    upper_1 : int = default_arg(upper, -1) or 0
    length : int = ((upper_1 if (upper_1 >= 0) else (len(target) - 1)) - lower_1) or 0
    for i in range(0, length + 1, 1):
        target[i + lower_1] = source[i]


def sort_in_place_by(projection: Callable[[_A], _B], xs: Array[_A], comparer: IComparer[_B]) -> None:
    def arrow_53(x: _A, y: _A, projection: Callable[[_A], _B]=projection, xs: Array[_A]=xs, comparer: IComparer[_B]=comparer) -> int:
        return comparer.Compare(projection(x), projection(y))

    xs.sort()


def sort_in_place(xs: Array[_T], comparer: IComparer[_T]) -> None:
    def arrow_54(x: _T, y: _T, xs: Array[_T]=xs, comparer: IComparer[_T]=comparer) -> int:
        return comparer.Compare(x, y)

    xs.sort()


def sort(xs: Array[_T], comparer: IComparer[_T]) -> Array[_T]:
    xs_1 : Array[_T] = xs[:]
    def comparer_1(x: _T, y: _T, xs: Array[_T]=xs, comparer: IComparer[_T]=comparer) -> int:
        return comparer.Compare(x, y)

    xs_1.sort()
    return xs_1


def sort_by(projection: Callable[[_A], _B], xs: Array[_A], comparer: IComparer[_B]) -> Array[_A]:
    xs_1 : Array[_A] = xs[:]
    def comparer_1(x: _A, y: _A, projection: Callable[[_A], _B]=projection, xs: Array[_A]=xs, comparer: IComparer[_B]=comparer) -> int:
        return comparer.Compare(projection(x), projection(y))

    xs_1.sort()
    return xs_1


def sort_descending(xs: Array[_T], comparer: IComparer[_T]) -> Array[_T]:
    xs_1 : Array[_T] = xs[:]
    def comparer_1(x: _T, y: _T, xs: Array[_T]=xs, comparer: IComparer[_T]=comparer) -> int:
        return comparer.Compare(x, y) * -1

    xs_1.sort()
    return xs_1


def sort_by_descending(projection: Callable[[_A], _B], xs: Array[_A], comparer: IComparer[_B]) -> Array[_A]:
    xs_1 : Array[_A] = xs[:]
    def comparer_1(x: _A, y: _A, projection: Callable[[_A], _B]=projection, xs: Array[_A]=xs, comparer: IComparer[_B]=comparer) -> int:
        return comparer.Compare(projection(x), projection(y)) * -1

    xs_1.sort()
    return xs_1


def sort_with(comparer: Any, xs: Array[_T]) -> Array[_T]:
    comparer_1 : Callable[[_T, _T], int] = comparer
    xs_1 : Array[_T] = xs[:]
    xs_1.sort()
    return xs_1


def all_pairs(xs: Array[_T1], ys: Array[_T2]) -> Array[Tuple[_T1, _T2]]:
    len1 : int = len(xs) or 0
    len2 : int = len(ys) or 0
    res : Array[Tuple[_T1, _T2]] = [None]*(len1 * len2)
    for i in range(0, (len(xs) - 1) + 1, 1):
        for j in range(0, (len(ys) - 1) + 1, 1):
            res[(i * len2) + j] = (xs[i], ys[j])
    return res


def unfold(generator: Callable[[_STATE], Optional[Tuple[_T, _STATE]]], state: _STATE) -> Array[_T]:
    res : Array[_T] = []
    def loop(state_1_mut: Optional[_STATE]=None, generator: Callable[[_STATE], Optional[Tuple[_T, _STATE]]]=generator, state: _STATE=state) -> None:
        while True:
            (state_1,) = (state_1_mut,)
            match_value : Optional[Tuple[_T, _STATE]] = generator(state_1)
            if match_value is not None:
                x : _T = match_value[0]
                s : _STATE = match_value[1]
                ignore(res.append(x))
                state_1_mut = s
                continue

            break

    loop(state)
    return res


def unzip(array: Array[Tuple[__A, __B]]) -> Tuple[Array[__A], Array[__B]]:
    len_1 : int = len(array) or 0
    res1 : Array[__A] = [None]*len_1
    res2 : Array[__B] = [None]*len_1
    def arrow_55(i: int, tupled_arg: Tuple[__A, __B], array: Array[Tuple[__A, __B]]=array) -> None:
        res1[i] = tupled_arg[0]
        res2[i] = tupled_arg[1]

    iterate_indexed(arrow_55, array)
    return (res1, res2)


def unzip3(array: Array[Tuple[__A, __B, __C]]) -> Tuple[Array[__A], Array[__B], Array[__C]]:
    len_1 : int = len(array) or 0
    res1 : Array[__A] = [None]*len_1
    res2 : Array[__B] = [None]*len_1
    res3 : Array[__C] = [None]*len_1
    def arrow_56(i: int, tupled_arg: Tuple[__A, __B, __C], array: Array[Tuple[__A, __B, __C]]=array) -> None:
        res1[i] = tupled_arg[0]
        res2[i] = tupled_arg[1]
        res3[i] = tupled_arg[2]

    iterate_indexed(arrow_56, array)
    return (res1, res2, res3)


def zip(array1: Array[_T], array2: Array[_U]) -> Array[Tuple[_T, _U]]:
    if len(array1) != len(array2):
        different_lengths()

    result : Array[Tuple[_T, _U]] = [None]*len(array1)
    for i in range(0, (len(array1) - 1) + 1, 1):
        result[i] = (array1[i], array2[i])
    return result


def zip3(array1: Array[_T], array2: Array[_U], array3: Array[_U]) -> Array[Tuple[_T, _U, _U]]:
    if True if (len(array1) != len(array2)) else (len(array2) != len(array3)):
        different_lengths()

    result : Array[Tuple[_T, _U, _U]] = [None]*len(array1)
    for i in range(0, (len(array1) - 1) + 1, 1):
        result[i] = (array1[i], array2[i], array3[i])
    return result


def chunk_by_size(chunk_size: int, array: Array[_T]) -> Array[Array[_T]]:
    if chunk_size < 1:
        raise Exception("The input must be positive.\\nParameter name: size")

    if len(array) == 0:
        return [[]]

    else: 
        result : Array[Array[_T]] = []
        for x in range(0, (int(math.ceil(len(array) / chunk_size)) - 1) + 1, 1):
            start : int = (x * chunk_size) or 0
            slice : Array[_T] = array[start:start+chunk_size]
            ignore(result.append(slice))
        return result



def split_at(index: int, array: Array[_T]) -> Tuple[Array[_T], Array[_T]]:
    if True if (index < 0) else (index > len(array)):
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    return (array[0:0+index], array[index:])


def compare_with(comparer: Any, array1: Array[_T], array2: Array[_T]) -> int:
    if array1 is None:
        if array2 is None:
            return 0

        else: 
            return -1


    elif array2 is None:
        return 1

    else: 
        i : int = 0
        result : int = 0
        length1 : int = len(array1) or 0
        length2 : int = len(array2) or 0
        if length1 > length2:
            return 1

        elif length1 < length2:
            return -1

        else: 
            while (result == 0) if (i < length1) else False:
                result = comparer(array1[i], array2[i]) or 0
                i = (i + 1) or 0
            return result




def equals_with(equals: Any, array1: Array[_T], array2: Array[_T]) -> bool:
    if array1 is None:
        if array2 is None:
            return True

        else: 
            return False


    elif array2 is None:
        return False

    else: 
        i : int = 0
        result : bool = True
        length1 : int = len(array1) or 0
        length2 : int = len(array2) or 0
        if length1 > length2:
            return False

        elif length1 < length2:
            return False

        else: 
            while result if (i < length1) else False:
                result = equals(array1[i], array2[i])
                i = (i + 1) or 0
            return result




def exactly_one(array: Array[_T]) -> _T:
    if len(array) == 1:
        return array[0]

    elif len(array) == 0:
        raise Exception("The input sequence was empty\\nParameter name: array")

    else: 
        raise Exception("Input array too long\\nParameter name: array")



def try_exactly_one(array: Array[_T]) -> Optional[_T]:
    if len(array) == 1:
        return some(array[0])

    else: 
        return None



def head(array: Array[_T]) -> _T:
    if len(array) == 0:
        raise Exception("The input array was empty\\nParameter name: array")

    else: 
        return array[0]



def try_head(array: Array[_T]) -> Optional[_T]:
    if len(array) == 0:
        return None

    else: 
        return some(array[0])



def tail(array: Array[_T]) -> Array[_T]:
    if len(array) == 0:
        raise Exception("Not enough elements\\nParameter name: array")

    return array[1:]


def item(index: int, array: Array[__A]) -> __A:
    return array[index]


def try_item(index: int, array: Array[_T]) -> Optional[_T]:
    if True if (index < 0) else (index >= len(array)):
        return None

    else: 
        return some(array[index])



def fold_back_indexed(folder: Any, array: Array[_T], state: _STATE) -> _STATE:
    def arrow_57(delegate_arg: _STATE, delegate_arg_1: _T, delegate_arg_2: int, folder: Any=folder, array: Array[_T]=array, state: _STATE=state) -> _STATE:
        return folder(delegate_arg_2, delegate_arg_1, delegate_arg)

    return array.reduceRight((arrow_57, state))


def fold_back(folder: Any, array: Array[_T], state: _STATE) -> _STATE:
    def arrow_58(acc: _STATE, x: _T, folder: Any=folder, array: Array[_T]=array, state: _STATE=state) -> _STATE:
        return folder(x, acc)

    return functools.reduce(arrow_58, array[::-1], state)


def fold_indexed2(folder: Any, state: __A, array1: Array[__B], array2: Array[__C]) -> __A:
    acc : __A = state
    if len(array1) != len(array2):
        raise Exception("Arrays have different lengths")

    for i in range(0, (len(array1) - 1) + 1, 1):
        acc = folder(i, acc, array1[i], array2[i])
    return acc


def fold2(folder: Any, state: _STATE, array1: Array[_T1], array2: Array[_T2]) -> _STATE:
    def arrow_59(_arg: int, acc: _STATE, x: _T1, y: _T2, folder: Any=folder, state: _STATE=state, array1: Array[_T1]=array1, array2: Array[_T2]=array2) -> _STATE:
        return folder(acc, x, y)

    return fold_indexed2(arrow_59, state, array1, array2)


def fold_back_indexed2(folder: Any, array1: Array[_T1], array2: Array[_T2], state: _STATE) -> _STATE:
    acc : _STATE = state
    if len(array1) != len(array2):
        different_lengths()

    size : int = len(array1) or 0
    for i in range(1, size + 1, 1):
        acc = folder(i - 1, array1[size - i], array2[size - i], acc)
    return acc


def fold_back2(f: Any, array1: Array[_T1], array2: Array[_T2], state: _STATE) -> _STATE:
    def arrow_60(_arg: int, x: _T1, y: _T2, acc: _STATE, f: Any=f, array1: Array[_T1]=array1, array2: Array[_T2]=array2, state: _STATE=state) -> _STATE:
        return f(x, y, acc)

    return fold_back_indexed2(arrow_60, array1, array2, state)


def reduce(reduction: Any, array: Array[_T]) -> _T:
    if len(array) == 0:
        raise Exception("The input array was empty")

    return functools.reduce(reduction, array)


def reduce_back(reduction: Any, array: Array[_T]) -> _T:
    if len(array) == 0:
        raise Exception("The input array was empty")

    return functools.reduce(reduction, array[::-1])


def for_all2(predicate: Any, array1: Array[__A], array2: Array[__B]) -> bool:
    def arrow_61(acc: bool, x: __A, y: __B, predicate: Any=predicate, array1: Array[__A]=array1, array2: Array[__B]=array2) -> bool:
        return predicate(x, y) if acc else False

    return fold2(arrow_61, True, array1, array2)


def exists_offset(predicate_mut: Callable[[_T], bool], array_mut: Array[_T], index_mut: int) -> bool:
    while True:
        (predicate, array, index) = (predicate_mut, array_mut, index_mut)
        if index == len(array):
            return False

        elif predicate(array[index]):
            return True

        else: 
            predicate_mut = predicate
            array_mut = array
            index_mut = index + 1
            continue

        break


def exists(predicate: Callable[[__A], bool], array: Array[__A]) -> bool:
    return exists_offset(predicate, array, 0)


def exists_offset2(predicate_mut: Any, array1_mut: Array[__A], array2_mut: Array[__B], index_mut: int) -> bool:
    while True:
        (predicate, array1, array2, index) = (predicate_mut, array1_mut, array2_mut, index_mut)
        if index == len(array1):
            return False

        elif predicate(array1[index], array2[index]):
            return True

        else: 
            predicate_mut = predicate
            array1_mut = array1
            array2_mut = array2
            index_mut = index + 1
            continue

        break


def exists2(predicate: Any, array1: Array[__A], array2: Array[__B]) -> bool:
    if len(array1) != len(array2):
        different_lengths()

    return exists_offset2(predicate, array1, array2, 0)


def sum(array: Array[_T], adder: IGenericAdder_1[_T]) -> _T:
    acc : _T = adder.GetZero()
    for i in range(0, (len(array) - 1) + 1, 1):
        acc = adder.Add(acc, array[i])
    return acc


def sum_by(projection: Callable[[_T], _T2], array: Array[_T], adder: IGenericAdder_1[_T2]) -> _T2:
    acc : _T2 = adder.GetZero()
    for i in range(0, (len(array) - 1) + 1, 1):
        acc = adder.Add(acc, projection(array[i]))
    return acc


def max_by(projection: Callable[[_A], _B], xs: Array[_A], comparer: IComparer[_B]) -> _A:
    def arrow_62(x: _A, y: _A, projection: Callable[[_A], _B]=projection, xs: Array[_A]=xs, comparer: IComparer[_B]=comparer) -> _A:
        return y if (comparer.Compare(projection(y), projection(x)) > 0) else x

    return reduce(arrow_62, xs)


def max(xs: Array[_A], comparer: IComparer[_A]) -> _A:
    def arrow_63(x: _A, y: _A, xs: Array[_A]=xs, comparer: IComparer[_A]=comparer) -> _A:
        return y if (comparer.Compare(y, x) > 0) else x

    return reduce(arrow_63, xs)


def min_by(projection: Callable[[_A], _B], xs: Array[_A], comparer: IComparer[_B]) -> _A:
    def arrow_64(x: _A, y: _A, projection: Callable[[_A], _B]=projection, xs: Array[_A]=xs, comparer: IComparer[_B]=comparer) -> _A:
        return x if (comparer.Compare(projection(y), projection(x)) > 0) else y

    return reduce(arrow_64, xs)


def min(xs: Array[_A], comparer: IComparer[_A]) -> _A:
    def arrow_65(x: _A, y: _A, xs: Array[_A]=xs, comparer: IComparer[_A]=comparer) -> _A:
        return x if (comparer.Compare(y, x) > 0) else y

    return reduce(arrow_65, xs)


def average(array: Array[_T], averager: IGenericAverager_1[_T]) -> _T:
    if len(array) == 0:
        raise Exception("The input array was empty\\nParameter name: array")

    total : _T = averager.GetZero()
    for i in range(0, (len(array) - 1) + 1, 1):
        total = averager.Add(total, array[i])
    return averager.DivideByInt(total, len(array))


def average_by(projection: Callable[[_T], _T2], array: Array[_T], averager: IGenericAverager_1[_T2]) -> _T2:
    if len(array) == 0:
        raise Exception("The input array was empty\\nParameter name: array")

    total : _T2 = averager.GetZero()
    for i in range(0, (len(array) - 1) + 1, 1):
        total = averager.Add(total, projection(array[i]))
    return averager.DivideByInt(total, len(array))


def windowed(window_size: int, source: Array[_T]) -> Array[Array[_T]]:
    if window_size <= 0:
        raise Exception("windowSize must be positive")

    res : Array[Array[_T]]
    def arrow_66(x: int, y: int, window_size: int=window_size, source: Array[_T]=source) -> int:
        return compare_primitives(x, y)

    len_1 : int = max_1(arrow_66, 0, (len(source) - window_size) + 1) or 0
    res = [None]*len_1
    for i in range(window_size, len(source) + 1, 1):
        res[i - window_size] = source[i - window_size:(i - 1) + 1]
    return res


def split_into(chunks: int, array: Array[_T]) -> Array[Array[_T]]:
    if chunks < 1:
        raise Exception("The input must be positive.\\nParameter name: chunks")

    if len(array) == 0:
        return [[]]

    else: 
        result : Array[Array[_T]] = []
        def arrow_67(x: int, y: int, chunks: int=chunks, array: Array[_T]=array) -> int:
            return compare_primitives(x, y)

        chunks_1 : int = min_1(arrow_67, chunks, len(array)) or 0
        min_chunk_size : int = (len(array) // chunks_1) or 0
        chunks_with_extra_item : int = (len(array) % chunks_1) or 0
        for i in range(0, (chunks_1 - 1) + 1, 1):
            chunk_size : int = ((min_chunk_size + 1) if (i < chunks_with_extra_item) else min_chunk_size) or 0
            def arrow_68(x_1: int, y_1: int, chunks: int=chunks, array: Array[_T]=array) -> int:
                return compare_primitives(x_1, y_1)

            start : int = ((i * min_chunk_size) + min_1(arrow_68, chunks_with_extra_item, i)) or 0
            slice : Array[_T] = array[start:start+chunk_size]
            ignore(result.append(slice))
        return result



def transpose(arrays: IEnumerable[Array[_T]], cons: Cons_1[_T]) -> Array[Array[_T]]:
    arrays_1 : Array[Array[_T]] = arrays if (isinstance(arrays, list)) else (list(arrays))
    len_1 : int = len(arrays_1) or 0
    if len_1 == 0:
        return [None]*0

    else: 
        len_inner : int = len(arrays_1[0]) or 0
        def predicate(a: Array[_T], arrays: IEnumerable[Array[_T]]=arrays, cons: Cons_1[_T]=cons) -> bool:
            return len(a) == len_inner

        if not for_all(predicate, arrays_1):
            different_lengths()

        result : Array[Array[_T]] = [None]*len_inner
        for i in range(0, (len_inner - 1) + 1, 1):
            result[i] = Helpers_allocateArrayFromCons(cons, len_1)
            for j in range(0, (len_1 - 1) + 1, 1):
                result[i][j] = arrays_1[j][i]
        return result



def insert_at(index: int, y: _T, xs: Array[_T]) -> Array[_T]:
    len_1 : int = len(xs) or 0
    if True if (index < 0) else (index > len_1):
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    target : Array[_T] = [x for i, x in enumerate(list(xs)+[0]*((len_1 + 1)-len(xs))) if i < (len_1 + 1)]
    for i in range(0, (index - 1) + 1, 1):
        target[i] = xs[i]
    target[index] = y
    for i_1 in range(index, (len_1 - 1) + 1, 1):
        target[i_1 + 1] = xs[i_1]
    return target


def insert_many_at(index: int, ys: IEnumerable[_T], xs: Array[_T]) -> Array[_T]:
    len_1 : int = len(xs) or 0
    if True if (index < 0) else (index > len_1):
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    ys_1 : Array[_T] = list(ys)
    len2 : int = len(ys_1) or 0
    target : Array[_T] = [x for i, x in enumerate(list(xs)+[0]*((len_1 + len2)-len(xs))) if i < (len_1 + len2)]
    for i in range(0, (index - 1) + 1, 1):
        target[i] = xs[i]
    for i_1 in range(0, (len2 - 1) + 1, 1):
        target[index + i_1] = ys_1[i_1]
    for i_2 in range(index, (len_1 - 1) + 1, 1):
        target[i_2 + len2] = xs[i_2]
    return target


def remove_at(index: int, xs: Array[_T]) -> Array[_T]:
    if True if (index < 0) else (index >= len(xs)):
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    i : int = -1
    def predicate(_arg: Optional[_T]=None, index: int=index, xs: Array[_T]=xs) -> bool:
        nonlocal i
        i = (i + 1) or 0
        return i != index

    return filter(predicate, xs)


def remove_many_at(index: int, count: int, xs: Array[_T]) -> Array[_T]:
    i : int = -1
    status : int = -1
    def predicate(_arg: Optional[_T]=None, index: int=index, count: int=count, xs: Array[_T]=xs) -> bool:
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


    ys : Array[_T] = filter(predicate, xs)
    status_1 : int = (1 if (((i + 1) == (index + count)) if (status == 0) else False) else status) or 0
    if status_1 < 1:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + ("index" if (status_1 < 0) else "count"))

    return ys


def update_at(index: int, y: _T, xs: Array[_T]) -> Array[_T]:
    len_1 : int = len(xs) or 0
    if True if (index < 0) else (index >= len_1):
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    target : Array[_T] = [x for i, x in enumerate(list(xs)+[0]*(len_1-len(xs))) if i < len_1]
    for i in range(0, (len_1 - 1) + 1, 1):
        target[i] = y if (i == index) else xs[i]
    return target


