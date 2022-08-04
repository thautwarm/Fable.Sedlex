from __future__ import annotations
from typing import (TypeVar, Any, Optional, Tuple, Generic)
from .map_util import (try_get_value, get_item_from_dict)
from .reflection import (TypeInfo, class_type)
from .resize_array import find_index
from .seq import (concat, iterate_indexed, to_array, delay, map, iterate)
from .string import format
from .types import (Array, FSharpRef)
from .util import (get_enumerator, IEnumerator, to_iterator, equals, ignore, IEnumerable, ICollection, IEqualityComparer, dispose)

_KEY = TypeVar("_KEY")

_VALUE = TypeVar("_VALUE")

def expr_36(gen0: TypeInfo, gen1: TypeInfo) -> TypeInfo:
    return class_type("Fable.Collections.Dictionary", [gen0, gen1], Dictionary)


class Dictionary(Generic[_KEY, _VALUE]):
    def __init__(self, pairs: IEnumerable[Any], comparer: IEqualityComparer[Any]) -> None:
        this : FSharpRef[Dictionary[_KEY, _VALUE]] = FSharpRef(None)
        self.comparer = comparer
        this.contents = self
        self.hash_map = dict([])
        self.init_00409 = 1
        with get_enumerator(pairs) as enumerator:
            while enumerator.System_Collections_IEnumerator_MoveNext():
                pair : Any = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
                Dictionary__Add_5BDDA1(this.contents, pair[0], pair[1])

    @property
    def Symbol_toStringTag(self) -> str:
        return "Dictionary"

    def to_json(self, _key: str) -> Any:
        this : Dictionary[_KEY, _VALUE] = self
        return list(this)

    def System_Collections_IEnumerable_GetEnumerator(self) -> IEnumerator[Any]:
        this : Dictionary[_KEY, _VALUE] = self
        return get_enumerator(this)

    def GetEnumerator(self) -> IEnumerator[Any]:
        this : Dictionary[_KEY, _VALUE] = self
        return get_enumerator(concat(this.hash_map.values()))

    def __iter__(self) -> IEnumerator[Any]:
        return to_iterator(self.GetEnumerator())

    def System_Collections_Generic_ICollection_00601_Add2B595(self, item: Any) -> None:
        this : Dictionary[_KEY, _VALUE] = self
        Dictionary__Add_5BDDA1(this, item[0], item[1])

    def System_Collections_Generic_ICollection_00601_Clear(self) -> None:
        this : Dictionary[_KEY, _VALUE] = self
        Dictionary__Clear(this)

    def System_Collections_Generic_ICollection_00601_Contains2B595(self, item: Any) -> bool:
        this : Dictionary[_KEY, _VALUE] = self
        match_value : Optional[Any] = Dictionary__TryFind_2B595(this, item[0])
        (pattern_matching_result,) = (None,)
        if match_value is not None:
            if equals(match_value[1], item[1]):
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1

        if pattern_matching_result == 0:
            return True

        elif pattern_matching_result == 1:
            return False


    def System_Collections_Generic_ICollection_00601_CopyToZ2E171D71(self, array: Array[Any], array_index: int) -> None:
        this : Dictionary[_KEY, _VALUE] = self
        def action(i: int, e: Any) -> None:
            array[array_index + i] = e

        iterate_indexed(action, this)

    def __len__(self) -> int:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__get_Count(this)

    def System_Collections_Generic_ICollection_00601_get_IsReadOnly(self) -> bool:
        return False

    def System_Collections_Generic_ICollection_00601_Remove2B595(self, item: Any) -> bool:
        this : Dictionary[_KEY, _VALUE] = self
        match_value : Optional[Any] = Dictionary__TryFind_2B595(this, item[0])
        if match_value is not None:
            if equals(match_value[1], item[1]):
                ignore(Dictionary__Remove_2B595(this, item[0]))

            return True

        else: 
            return False


    def System_Collections_Generic_IDictionary_00602_Add5BDDA1(self, key: _KEY, value: _VALUE) -> None:
        this : Dictionary[_KEY, _VALUE] = self
        Dictionary__Add_5BDDA1(this, key, value)

    def System_Collections_Generic_IDictionary_00602_ContainsKey2B595(self, key: Optional[_KEY]=None) -> bool:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__ContainsKey_2B595(this, key)

    def System_Collections_Generic_IDictionary_00602_get_Item2B595(self, key: Optional[_KEY]=None) -> _VALUE:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__get_Item_2B595(this, key)

    def System_Collections_Generic_IDictionary_00602_set_Item5BDDA1(self, key: _KEY, v: _VALUE) -> None:
        this : Dictionary[_KEY, _VALUE] = self
        Dictionary__set_Item_5BDDA1(this, key, v)

    def System_Collections_Generic_IDictionary_00602_get_Keys(self) -> ICollection[_KEY]:
        this : Dictionary[_KEY, _VALUE] = self
        def arrow_33(__unit: Any=None) -> IEnumerable[_KEY]:
            def arrow_32(pair: Any) -> _KEY:
                return pair[0]

            return map(arrow_32, this)

        return to_array(delay(arrow_33))

    def System_Collections_Generic_IDictionary_00602_Remove2B595(self, key: Optional[_KEY]=None) -> bool:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__Remove_2B595(this, key)

    def System_Collections_Generic_IDictionary_00602_TryGetValue6DC89625(self, key: _KEY, value: FSharpRef[_VALUE]) -> bool:
        this : Dictionary[_KEY, _VALUE] = self
        match_value : Optional[Any] = Dictionary__TryFind_2B595(this, key)
        if match_value is not None:
            pair : Any = match_value
            value.contents = pair[1]
            return True

        else: 
            return False


    def System_Collections_Generic_IDictionary_00602_get_Values(self) -> ICollection[_VALUE]:
        this : Dictionary[_KEY, _VALUE] = self
        def arrow_35(__unit: Any=None) -> IEnumerable[_VALUE]:
            def arrow_34(pair: Any) -> _VALUE:
                return pair[1]

            return map(arrow_34, this)

        return to_array(delay(arrow_35))

    @property
    def size(self) -> int:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__get_Count(this)

    def clear(self) -> None:
        this : Dictionary[_KEY, _VALUE] = self
        Dictionary__Clear(this)

    def delete(self, k: Optional[_KEY]=None) -> bool:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__Remove_2B595(this, k)

    def entries(self) -> IEnumerable[Tuple[_KEY, _VALUE]]:
        this : Dictionary[_KEY, _VALUE] = self
        def mapping(p: Any) -> Tuple[_KEY, _VALUE]:
            return (p[0], p[1])

        return map(mapping, this)

    def __getitem__(self, k: Optional[_KEY]=None) -> _VALUE:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__get_Item_2B595(this, k)

    def __contains__(self, k: Optional[_KEY]=None) -> bool:
        this : Dictionary[_KEY, _VALUE] = self
        return Dictionary__ContainsKey_2B595(this, k)

    def keys(self) -> IEnumerable[_KEY]:
        this : Dictionary[_KEY, _VALUE] = self
        def mapping(p: Any) -> _KEY:
            return p[0]

        return map(mapping, this)

    def __setitem__(self, k: _KEY, v: _VALUE) -> Map_2[_KEY, _VALUE]:
        this : Dictionary[_KEY, _VALUE] = self
        Dictionary__set_Item_5BDDA1(this, k, v)
        return this

    def values(self) -> IEnumerable[_VALUE]:
        this : Dictionary[_KEY, _VALUE] = self
        def mapping(p: Any) -> _VALUE:
            return p[1]

        return map(mapping, this)

    def for_each(self, f: Any, this_arg: Optional[Any]=None) -> None:
        this : Dictionary[_KEY, _VALUE] = self
        def action(p: Any) -> None:
            f(p[1], p[0], this)

        iterate(action, this)


Dictionary_reflection = expr_36

def Dictionary__ctor_6623D9B3(pairs: IEnumerable[Any], comparer: IEqualityComparer[Any]) -> Dictionary[_KEY, _VALUE]:
    return Dictionary(pairs, comparer)


def Dictionary__TryFindIndex_2B595(this: Dictionary[_KEY, _VALUE], k: _KEY) -> Tuple[bool, int, int]:
    h : int = this.comparer.GetHashCode(k) or 0
    match_value : Tuple[bool, Array[Any]]
    out_arg : Array[Any] = None
    def arrow_37(this: Dictionary[_KEY, _VALUE]=this, k: _KEY=k) -> Array[Any]:
        return out_arg

    def arrow_38(v: Array[Any], this: Dictionary[_KEY, _VALUE]=this, k: _KEY=k) -> None:
        nonlocal out_arg
        out_arg = v

    match_value = (try_get_value(this.hash_map, h, FSharpRef(arrow_37, arrow_38)), out_arg)
    if match_value[0]:
        def arrow_39(pair: Any, this: Dictionary[_KEY, _VALUE]=this, k: _KEY=k) -> bool:
            return this.comparer.Equals(k, pair[0])

        return (True, h, find_index(arrow_39, match_value[1]))

    else: 
        return (False, h, -1)



def Dictionary__TryFind_2B595(this: Dictionary[_KEY, _VALUE], k: _KEY) -> Optional[Any]:
    match_value : Tuple[bool, int, int] = Dictionary__TryFindIndex_2B595(this, k)
    (pattern_matching_result,) = (None,)
    if match_value[0]:
        if match_value[2] > -1:
            pattern_matching_result = 0

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return get_item_from_dict(this.hash_map, match_value[1])[match_value[2]]

    elif pattern_matching_result == 1:
        return None



def Dictionary__get_Comparer(this: Dictionary[_KEY, _VALUE]) -> IEqualityComparer[Any]:
    return this.comparer


def Dictionary__Clear(this: Dictionary[_KEY, _VALUE]) -> None:
    this.hash_map.clear()


def Dictionary__get_Count(this: Dictionary[_KEY, _VALUE]) -> int:
    count : int = 0
    enumerator : Any = get_enumerator(this.hash_map.values())
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            pairs : Array[Any] = enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()
            count = (count + len(pairs)) or 0

    finally: 
        dispose(enumerator)

    return count


def Dictionary__get_Item_2B595(this: Dictionary[_KEY, _VALUE], k: _KEY) -> _VALUE:
    match_value : Optional[Any] = Dictionary__TryFind_2B595(this, k)
    if match_value is not None:
        return match_value[1]

    else: 
        raise Exception("The item was not found in collection")



def Dictionary__set_Item_5BDDA1(this: Dictionary[_KEY, _VALUE], k: _KEY, v: _VALUE) -> None:
    match_value : Tuple[bool, int, int] = Dictionary__TryFindIndex_2B595(this, k)
    if match_value[0]:
        if match_value[2] > -1:
            get_item_from_dict(this.hash_map, match_value[1])[match_value[2]] = (k, v)

        else: 
            value : None = (get_item_from_dict(this.hash_map, match_value[1]).append((k, v)))
            ignore()


    else: 
        this.hash_map[match_value[1]] = [(k, v)]



def Dictionary__Add_5BDDA1(this: Dictionary[_KEY, _VALUE], k: _KEY, v: _VALUE) -> None:
    match_value : Tuple[bool, int, int] = Dictionary__TryFindIndex_2B595(this, k)
    if match_value[0]:
        if match_value[2] > -1:
            raise Exception(format("An item with the same key has already been added. Key: {0}", k))

        else: 
            value : None = (get_item_from_dict(this.hash_map, match_value[1]).append((k, v)))
            ignore()


    else: 
        this.hash_map[match_value[1]] = [(k, v)]



def Dictionary__ContainsKey_2B595(this: Dictionary[_KEY, _VALUE], k: _KEY) -> bool:
    match_value : Tuple[bool, int, int] = Dictionary__TryFindIndex_2B595(this, k)
    (pattern_matching_result,) = (None,)
    if match_value[0]:
        if match_value[2] > -1:
            pattern_matching_result = 0

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return True

    elif pattern_matching_result == 1:
        return False



def Dictionary__Remove_2B595(this: Dictionary[_KEY, _VALUE], k: _KEY) -> bool:
    match_value : Tuple[bool, int, int] = Dictionary__TryFindIndex_2B595(this, k)
    (pattern_matching_result,) = (None,)
    if match_value[0]:
        if match_value[2] > -1:
            pattern_matching_result = 0

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        get_item_from_dict(this.hash_map, match_value[1]).pop(match_value[2])
        return True

    elif pattern_matching_result == 1:
        return False



