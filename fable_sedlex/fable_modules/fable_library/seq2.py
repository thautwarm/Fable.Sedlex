from typing import (TypeVar, Any, Optional, Callable, Tuple)
from .list import FSharpList
from .map_util import (add_to_set, try_get_value, get_item_from_dict, add_to_dict)
from .mutable_map import Dictionary
from .mutable_set import HashSet
from .seq import (delay, filter, map, to_array, to_list)
from .types import (Array, FSharpRef)
from .util import (IEnumerable, IEqualityComparer, get_enumerator)

_T = TypeVar("_T")

_KEY = TypeVar("_KEY")

def distinct(xs: IEnumerable[_T], comparer: IEqualityComparer[Any]) -> IEnumerable[_T]:
    def arrow_93(xs: IEnumerable[_T]=xs, comparer: IEqualityComparer[Any]=comparer) -> IEnumerable[_T]:
        hash_set : Any = HashSet([], comparer)
        def predicate(x: Optional[_T]=None) -> bool:
            return add_to_set(x, hash_set)

        return filter(predicate, xs)

    return delay(arrow_93)


def distinct_by(projection: Callable[[_T], _KEY], xs: IEnumerable[_T], comparer: IEqualityComparer[Any]) -> IEnumerable[_T]:
    def arrow_94(projection: Callable[[_T], _KEY]=projection, xs: IEnumerable[_T]=xs, comparer: IEqualityComparer[Any]=comparer) -> IEnumerable[_T]:
        hash_set : Any = HashSet([], comparer)
        def predicate(x: Optional[_T]=None) -> bool:
            return add_to_set(projection(x), hash_set)

        return filter(predicate, xs)

    return delay(arrow_94)


def except_(items_to_exclude: IEnumerable[_T], xs: IEnumerable[_T], comparer: IEqualityComparer[Any]) -> IEnumerable[_T]:
    def arrow_95(items_to_exclude: IEnumerable[_T]=items_to_exclude, xs: IEnumerable[_T]=xs, comparer: IEqualityComparer[Any]=comparer) -> IEnumerable[_T]:
        hash_set : Any = HashSet(items_to_exclude, comparer)
        def predicate(x: Optional[_T]=None) -> bool:
            return add_to_set(x, hash_set)

        return filter(predicate, xs)

    return delay(arrow_95)


def count_by(projection: Callable[[_T], _KEY], xs: IEnumerable[_T], comparer: IEqualityComparer[Any]) -> IEnumerable[Tuple[_KEY, int]]:
    def arrow_99(projection: Callable[[_T], _KEY]=projection, xs: IEnumerable[_T]=xs, comparer: IEqualityComparer[Any]=comparer) -> IEnumerable[Tuple[_KEY, int]]:
        dict_1 : Any = Dictionary([], comparer)
        keys : Array[_KEY] = []
        with get_enumerator(xs) as enumerator:
            while enumerator.System_Collections_IEnumerator_MoveNext():
                key : _KEY = projection(enumerator.System_Collections_Generic_IEnumerator_00601_get_Current())
                match_value : Tuple[bool, int]
                out_arg : int = 0
                def arrow_96(__unit: Any=None) -> int:
                    return out_arg

                def arrow_97(v: int) -> None:
                    nonlocal out_arg
                    out_arg = v or 0

                match_value = (try_get_value(dict_1, key, FSharpRef(arrow_96, arrow_97)), out_arg)
                if match_value[0]:
                    dict_1[key] = match_value[1] + 1

                else: 
                    dict_1[key] = 1
                    (keys.append(key))

        def arrow_98(key_1: Optional[_KEY]=None) -> Tuple[_KEY, int]:
            return (key_1, get_item_from_dict(dict_1, key_1))

        return map(arrow_98, keys)

    return delay(arrow_99)


def group_by(projection: Callable[[_T], _KEY], xs: IEnumerable[_T], comparer: IEqualityComparer[Any]) -> IEnumerable[Tuple[_KEY, IEnumerable[_T]]]:
    def arrow_103(projection: Callable[[_T], _KEY]=projection, xs: IEnumerable[_T]=xs, comparer: IEqualityComparer[Any]=comparer) -> IEnumerable[Tuple[_KEY, IEnumerable[_T]]]:
        dict_1 : Any = Dictionary([], comparer)
        keys : Array[_KEY] = []
        with get_enumerator(xs) as enumerator:
            while enumerator.System_Collections_IEnumerator_MoveNext():
                x : _T = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
                key : _KEY = projection(x)
                match_value : Tuple[bool, Array[_T]]
                out_arg : Array[_T] = None
                def arrow_100(__unit: Any=None) -> Array[_T]:
                    return out_arg

                def arrow_101(v: Array[_T]) -> None:
                    nonlocal out_arg
                    out_arg = v

                match_value = (try_get_value(dict_1, key, FSharpRef(arrow_100, arrow_101)), out_arg)
                if match_value[0]:
                    (match_value[1].append(x))

                else: 
                    add_to_dict(dict_1, key, [x])
                    (keys.append(key))

        def arrow_102(key_1: Optional[_KEY]=None) -> Tuple[_KEY, IEnumerable[_T]]:
            return (key_1, get_item_from_dict(dict_1, key_1))

        return map(arrow_102, keys)

    return delay(arrow_103)


def Array_distinct(xs: Array[_T], comparer: IEqualityComparer[Any]) -> Array[_T]:
    return to_array(distinct(xs, comparer))


def Array_distinctBy(projection: Callable[[_T], _KEY], xs: Array[_T], comparer: IEqualityComparer[Any]) -> Array[_T]:
    return to_array(distinct_by(projection, xs, comparer))


def Array_except(items_to_exclude: IEnumerable[_T], xs: Array[_T], comparer: IEqualityComparer[Any]) -> Array[_T]:
    return to_array(except_(items_to_exclude, xs, comparer))


def Array_countBy(projection: Callable[[_T], _KEY], xs: Array[_T], comparer: IEqualityComparer[Any]) -> Array[Tuple[_KEY, int]]:
    return to_array(count_by(projection, xs, comparer))


def Array_groupBy(projection: Callable[[_T], _KEY], xs: Array[_T], comparer: IEqualityComparer[Any]) -> Array[Tuple[_KEY, Array[_T]]]:
    def mapping(tupled_arg: Tuple[_KEY, IEnumerable[_T]], projection: Callable[[_T], _KEY]=projection, xs: Array[_T]=xs, comparer: IEqualityComparer[Any]=comparer) -> Tuple[_KEY, Array[_T]]:
        return (tupled_arg[0], to_array(tupled_arg[1]))

    return to_array(map(mapping, group_by(projection, xs, comparer)))


def List_distinct(xs: FSharpList[_T], comparer: IEqualityComparer[Any]) -> FSharpList[_T]:
    return to_list(distinct(xs, comparer))


def List_distinctBy(projection: Callable[[_T], _KEY], xs: FSharpList[_T], comparer: IEqualityComparer[Any]) -> FSharpList[_T]:
    return to_list(distinct_by(projection, xs, comparer))


def List_except(items_to_exclude: IEnumerable[_T], xs: FSharpList[_T], comparer: IEqualityComparer[Any]) -> FSharpList[_T]:
    return to_list(except_(items_to_exclude, xs, comparer))


def List_countBy(projection: Callable[[_T], _KEY], xs: FSharpList[_T], comparer: IEqualityComparer[Any]) -> FSharpList[Tuple[_KEY, int]]:
    return to_list(count_by(projection, xs, comparer))


def List_groupBy(projection: Callable[[_T], _KEY], xs: FSharpList[_T], comparer: IEqualityComparer[Any]) -> FSharpList[Tuple[_KEY, FSharpList[_T]]]:
    def mapping(tupled_arg: Tuple[_KEY, IEnumerable[_T]], projection: Callable[[_T], _KEY]=projection, xs: FSharpList[_T]=xs, comparer: IEqualityComparer[Any]=comparer) -> Tuple[_KEY, FSharpList[_T]]:
        return (tupled_arg[0], to_list(tupled_arg[1]))

    return to_list(map(mapping, group_by(projection, xs, comparer)))


