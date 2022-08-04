from __future__ import annotations
from typing import (TypeVar, Any, Callable, Generic, Optional, Tuple)
from .array import (singleton as singleton_1, try_find_back as try_find_back_1, try_find_index_back as try_find_index_back_1, fold_back as fold_back_1, fold_back2 as fold_back2_1, try_head as try_head_1, try_item as try_item_1, map_fold as map_fold_1, map_fold_back as map_fold_back_1, reduce_back as reduce_back_1, reverse as reverse_1, scan_back as scan_back_1, pairwise as pairwise_1, map as map_1, split_into as split_into_1, windowed as windowed_1, transpose as transpose_1, permute as permute_1, chunk_by_size as chunk_by_size_1)
from .fsharp_core import (Operators_NullArg, Operators_Lock)
from .list import (FSharpList, to_array as to_array_1, of_array as of_array_1, of_seq as of_seq_1, try_head as try_head_2, is_empty as is_empty_1, try_item as try_item_2, length as length_1)
from .option import (value as value_1, some)
from .reflection import (TypeInfo, class_type)
from .types import (to_string, Array)
from .util import (get_enumerator, IEnumerator, to_iterator, IDisposable, is_disposable, dispose as dispose_2, IEnumerable, is_array_like, IEqualityComparer, equals, ignore, clear, IComparer)
from .global_ import (IGenericAdder_1, IGenericAverager_1, SR_indexOutOfBounds)

__A = TypeVar("__A")

_T = TypeVar("_T")

_U = TypeVar("_U")

_STATE = TypeVar("_STATE")

__B = TypeVar("__B")

_T1 = TypeVar("_T1")

_T2 = TypeVar("_T2")

_T3 = TypeVar("_T3")

_RESULT = TypeVar("_RESULT")

SR_enumerationAlreadyFinished : str = "Enumeration already finished."

SR_enumerationNotStarted : str = "Enumeration has not started. Call MoveNext."

SR_inputSequenceEmpty : str = "The input sequence was empty."

SR_inputSequenceTooLong : str = "The input sequence contains more than one element."

SR_keyNotFoundAlt : str = "An index satisfying the predicate was not found in the collection."

SR_notEnoughElements : str = "The input sequence has an insufficient number of elements."

SR_resetNotSupported : str = "Reset is not supported on this enumerator."

def Enumerator_noReset() -> __A:
    raise Exception(SR_resetNotSupported)


def Enumerator_notStarted() -> __A:
    raise Exception(SR_enumerationNotStarted)


def Enumerator_alreadyFinished() -> __A:
    raise Exception(SR_enumerationAlreadyFinished)


def expr_137(gen0: TypeInfo) -> TypeInfo:
    return class_type("SeqModule.Enumerator.Seq", [gen0], Enumerator_Seq)


class Enumerator_Seq(Generic[_T]):
    def __init__(self, f: Callable[[], IEnumerator[_T]]) -> None:
        self.f = f

    def __str__(self) -> str:
        xs : Enumerator_Seq[_T] = self
        max_count : int = 4
        i : int = 0
        str_1 : str = "seq ["
        with get_enumerator(xs) as e:
            while e.System_Collections_IEnumerator_MoveNext() if (i < max_count) else False:
                if i > 0:
                    str_1 = str_1 + "; "

                str_1 = str_1 + to_string(e.System_Collections_Generic_IEnumerator_00601_get_Current())
                i = (i + 1) or 0
            if i == max_count:
                str_1 = str_1 + "; ..."

            return str_1 + "]"

    def GetEnumerator(self) -> IEnumerator[_T]:
        x : Enumerator_Seq[_T] = self
        return x.f()

    def __iter__(self) -> IEnumerator[_T]:
        return to_iterator(self.GetEnumerator())

    def System_Collections_IEnumerable_GetEnumerator(self) -> IEnumerator[Any]:
        x : Enumerator_Seq[_T] = self
        return x.f()


Enumerator_Seq_reflection = expr_137

def Enumerator_Seq__ctor_673A07F2(f: Callable[[], IEnumerator[_T]]) -> Enumerator_Seq[_T]:
    return Enumerator_Seq(f)


def expr_138(gen0: TypeInfo) -> TypeInfo:
    return class_type("SeqModule.Enumerator.FromFunctions`1", [gen0], Enumerator_FromFunctions_1)


class Enumerator_FromFunctions_1(IDisposable, Generic[_T]):
    def __init__(self, current: Callable[[], _T], next_1: Callable[[], bool], dispose: Callable[[], None]) -> None:
        self.current = current
        self.next = next_1
        self.dispose = dispose

    def System_Collections_Generic_IEnumerator_00601_get_Current(self) -> _T:
        _ : Enumerator_FromFunctions_1[_T] = self
        return _.current()

    def System_Collections_IEnumerator_get_Current(self) -> Any:
        _ : Enumerator_FromFunctions_1[_T] = self
        return _.current()

    def System_Collections_IEnumerator_MoveNext(self) -> bool:
        _ : Enumerator_FromFunctions_1[_T] = self
        return _.next()

    def System_Collections_IEnumerator_Reset(self) -> None:
        Enumerator_noReset()

    def Dispose(self) -> None:
        _ : Enumerator_FromFunctions_1[_T] = self
        _.dispose()


Enumerator_FromFunctions_1_reflection = expr_138

def Enumerator_FromFunctions_1__ctor_58C54629(current: Callable[[], _T], next_1: Callable[[], bool], dispose: Callable[[], None]) -> Enumerator_FromFunctions_1[_T]:
    return Enumerator_FromFunctions_1(current, next_1, dispose)


def Enumerator_cast(e: IEnumerator[Any]) -> IEnumerator[_T]:
    def current(e: IEnumerator[Any]=e) -> _T:
        return e.System_Collections_IEnumerator_get_Current()

    def next_1(e: IEnumerator[Any]=e) -> bool:
        return e.System_Collections_IEnumerator_MoveNext()

    def dispose(e: IEnumerator[Any]=e) -> None:
        if is_disposable(e):
            dispose_2(e)


    return Enumerator_FromFunctions_1__ctor_58C54629(current, next_1, dispose)


def Enumerator_concat(sources: IEnumerable[_U]) -> IEnumerator[_T]:
    outer_opt : Optional[IEnumerator[_U]] = None
    inner_opt : Optional[IEnumerator[_T]] = None
    started : bool = False
    finished : bool = False
    curr : Optional[_T] = None
    def current(sources: IEnumerable[_U]=sources) -> _T:
        if not started:
            Enumerator_notStarted()

        elif finished:
            Enumerator_alreadyFinished()

        if curr is not None:
            return value_1(curr)

        else: 
            return Enumerator_alreadyFinished()


    def finish(sources: IEnumerable[_U]=sources) -> None:
        nonlocal finished, inner_opt, outer_opt
        finished = True
        if inner_opt is not None:
            inner : IEnumerator[_T] = inner_opt
            try: 
                dispose_2(inner)

            finally: 
                inner_opt = None


        if outer_opt is not None:
            outer : IEnumerator[_U] = outer_opt
            try: 
                dispose_2(outer)

            finally: 
                outer_opt = None



    def loop(sources: IEnumerable[_U]=sources) -> bool:
        res : Optional[bool] = None
        while res is None:
            nonlocal curr, inner_opt, outer_opt
            outer_opt_1 : Optional[IEnumerator[_U]] = outer_opt
            inner_opt_1 : Optional[IEnumerator[_T]] = inner_opt
            if outer_opt_1 is not None:
                if inner_opt_1 is not None:
                    inner_1 : IEnumerator[_T] = inner_opt_1
                    if inner_1.System_Collections_IEnumerator_MoveNext():
                        curr = some(inner_1.System_Collections_Generic_IEnumerator_00601_get_Current())
                        res = True

                    else: 
                        try: 
                            dispose_2(inner_1)

                        finally: 
                            inner_opt = None



                else: 
                    outer_1 : IEnumerator[_U] = outer_opt_1
                    if outer_1.System_Collections_IEnumerator_MoveNext():
                        ie : _U = outer_1.System_Collections_Generic_IEnumerator_00601_get_Current()
                        def arrow_139(__unit: Any=None) -> IEnumerator[_T]:
                            copy_of_struct : _U = ie
                            return get_enumerator(copy_of_struct)

                        inner_opt = arrow_139()

                    else: 
                        finish()
                        res = False



            else: 
                outer_opt = get_enumerator(sources)

        return value_1(res)

    def next_1(sources: IEnumerable[_U]=sources) -> bool:
        nonlocal started
        if not started:
            started = True

        if finished:
            return False

        else: 
            return loop()


    def dispose(sources: IEnumerable[_U]=sources) -> None:
        if not finished:
            finish()


    return Enumerator_FromFunctions_1__ctor_58C54629(current, next_1, dispose)


def Enumerator_enumerateThenFinally(f: Callable[[], None], e: IEnumerator[_T]) -> IEnumerator[_T]:
    def current(f: Callable[[], None]=f, e: IEnumerator[_T]=e) -> _T:
        return e.System_Collections_Generic_IEnumerator_00601_get_Current()

    def next_1(f: Callable[[], None]=f, e: IEnumerator[_T]=e) -> bool:
        return e.System_Collections_IEnumerator_MoveNext()

    def dispose(f: Callable[[], None]=f, e: IEnumerator[_T]=e) -> None:
        try: 
            dispose_2(e)

        finally: 
            f()


    return Enumerator_FromFunctions_1__ctor_58C54629(current, next_1, dispose)


def Enumerator_generateWhileSome(openf: Callable[[], _T], compute: Callable[[_T], Optional[_U]], closef: Callable[[_T], None]) -> IEnumerator[_U]:
    started : bool = False
    curr : Optional[_U] = None
    state : Optional[_T] = some(openf())
    def current(openf: Callable[[], _T]=openf, compute: Callable[[_T], Optional[_U]]=compute, closef: Callable[[_T], None]=closef) -> _U:
        if not started:
            Enumerator_notStarted()

        if curr is not None:
            return value_1(curr)

        else: 
            return Enumerator_alreadyFinished()


    def dispose(openf: Callable[[], _T]=openf, compute: Callable[[_T], Optional[_U]]=compute, closef: Callable[[_T], None]=closef) -> None:
        nonlocal state
        if state is not None:
            x_1 : _T = value_1(state)
            try: 
                closef(x_1)

            finally: 
                state = None



    def finish(openf: Callable[[], _T]=openf, compute: Callable[[_T], Optional[_U]]=compute, closef: Callable[[_T], None]=closef) -> None:
        nonlocal curr
        try: 
            dispose()

        finally: 
            curr = None


    def next_1(openf: Callable[[], _T]=openf, compute: Callable[[_T], Optional[_U]]=compute, closef: Callable[[_T], None]=closef) -> bool:
        nonlocal started, curr
        if not started:
            started = True

        if state is not None:
            s : _T = value_1(state)
            match_value_1 : Optional[_U]
            try: 
                match_value_1 = compute(s)

            except Exception as match_value:
                finish()
                raise match_value

            if match_value_1 is not None:
                curr = match_value_1
                return True

            else: 
                finish()
                return False


        else: 
            return False


    return Enumerator_FromFunctions_1__ctor_58C54629(current, next_1, dispose)


def Enumerator_unfold(f: Callable[[_STATE], Optional[Tuple[_T, _STATE]]], state: _STATE) -> IEnumerator[_T]:
    curr : Optional[Tuple[_T, _STATE]] = None
    acc : _STATE = state
    def current(f: Callable[[_STATE], Optional[Tuple[_T, _STATE]]]=f, state: _STATE=state) -> _T:
        if curr is not None:
            x : _T = curr[0]
            st : _STATE = curr[1]
            return x

        else: 
            return Enumerator_notStarted()


    def next_1(f: Callable[[_STATE], Optional[Tuple[_T, _STATE]]]=f, state: _STATE=state) -> bool:
        nonlocal curr, acc
        curr = f(acc)
        if curr is not None:
            x_1 : _T = curr[0]
            st_1 : _STATE = curr[1]
            acc = st_1
            return True

        else: 
            return False


    def dispose(f: Callable[[_STATE], Optional[Tuple[_T, _STATE]]]=f, state: _STATE=state) -> None:
        pass

    return Enumerator_FromFunctions_1__ctor_58C54629(current, next_1, dispose)


def index_not_found() -> __A:
    raise Exception(SR_keyNotFoundAlt)


def check_non_null(arg_name: str, arg: __A) -> None:
    if arg is None:
        Operators_NullArg(arg_name)



def mk_seq(f: Callable[[], IEnumerator[_T]]) -> IEnumerable[_T]:
    return Enumerator_Seq__ctor_673A07F2(f)


def of_seq(xs: IEnumerable[_T]) -> IEnumerator[_T]:
    check_non_null("source", xs)
    return get_enumerator(xs)


def delay(generator: Callable[[], IEnumerable[_T]]) -> IEnumerable[_T]:
    def arrow_140(generator: Callable[[], IEnumerable[_T]]=generator) -> IEnumerator[_T]:
        return get_enumerator(generator())

    return mk_seq(arrow_140)


def concat(sources: IEnumerable[__A]) -> IEnumerable[_T]:
    def arrow_141(sources: IEnumerable[__A]=sources) -> IEnumerator[_T]:
        return Enumerator_concat(sources)

    return mk_seq(arrow_141)


def unfold(generator: Callable[[_STATE], Optional[Tuple[_T, _STATE]]], state: _STATE) -> IEnumerable[_T]:
    def arrow_142(generator: Callable[[_STATE], Optional[Tuple[_T, _STATE]]]=generator, state: _STATE=state) -> IEnumerator[_T]:
        return Enumerator_unfold(generator, state)

    return mk_seq(arrow_142)


def empty() -> IEnumerable[_T]:
    def arrow_143(__unit: Any=None) -> IEnumerable[_T]:
        return [0] * 0

    return delay(arrow_143)


def singleton(x: Optional[_T]=None) -> IEnumerable[_T]:
    def arrow_144(x: _T=x) -> IEnumerable[_T]:
        return singleton_1(x, None)

    return delay(arrow_144)


def of_array(arr: Array[_T]) -> IEnumerable[_T]:
    return arr


def to_array(xs: IEnumerable[_T]) -> Array[_T]:
    if isinstance(xs, FSharpList):
        return to_array_1(xs)

    else: 
        return list(xs)



def of_list(xs: FSharpList[_T]) -> IEnumerable[_T]:
    return xs


def to_list(xs: IEnumerable[_T]) -> IEnumerable[_T]:
    if is_array_like(xs):
        return of_array_1(xs)

    elif isinstance(xs, FSharpList):
        return xs

    else: 
        return of_seq_1(xs)



def generate(create: Callable[[], __A], compute: Callable[[__A], Optional[__B]], dispose: Callable[[__A], None]) -> IEnumerable[__B]:
    def arrow_145(create: Callable[[], __A]=create, compute: Callable[[__A], Optional[__B]]=compute, dispose: Callable[[__A], None]=dispose) -> IEnumerator[__B]:
        return Enumerator_generateWhileSome(create, compute, dispose)

    return mk_seq(arrow_145)


def generate_indexed(create: Callable[[], __A], compute: Any, dispose: Callable[[__A], None]) -> IEnumerable[__B]:
    def arrow_147(create: Callable[[], __A]=create, compute: Any=compute, dispose: Callable[[__A], None]=dispose) -> IEnumerator[__B]:
        i : int = -1
        def arrow_146(x: Optional[__A]=None) -> Optional[__B]:
            nonlocal i
            i = (i + 1) or 0
            return compute(i, x)

        return Enumerator_generateWhileSome(create, arrow_146, dispose)

    return mk_seq(arrow_147)


def append(xs: IEnumerable[_T], ys: IEnumerable[_T]) -> IEnumerable[_T]:
    return concat([xs, ys])


def cast(xs: IEnumerable[Any]) -> IEnumerable[__A]:
    def arrow_148(xs: IEnumerable[Any]=xs) -> IEnumerator[__A]:
        check_non_null("source", xs)
        return Enumerator_cast(get_enumerator(xs))

    return mk_seq(arrow_148)


def choose(chooser: Callable[[_T], Optional[_U]], xs: IEnumerable[_T]) -> IEnumerable[_U]:
    def arrow_149(chooser: Callable[[_T], Optional[_U]]=chooser, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_150(e: IEnumerator[_T], chooser: Callable[[_T], Optional[_U]]=chooser, xs: IEnumerable[_T]=xs) -> Optional[_U]:
        curr : Optional[_U] = None
        while e.System_Collections_IEnumerator_MoveNext() if (curr is None) else False:
            curr = chooser(e.System_Collections_Generic_IEnumerator_00601_get_Current())
        return curr

    def arrow_151(e_1: IEnumerator[_T], chooser: Callable[[_T], Optional[_U]]=chooser, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate(arrow_149, arrow_150, arrow_151)


def compare_with(comparer: Any, xs: IEnumerable[_T], ys: IEnumerable[_T]) -> int:
    with of_seq(xs) as e1:
        with of_seq(ys) as e2:
            c : int = 0
            b1 : bool = e1.System_Collections_IEnumerator_MoveNext()
            b2 : bool = e2.System_Collections_IEnumerator_MoveNext()
            while b2 if (b1 if (c == 0) else False) else False:
                c = comparer(e1.System_Collections_Generic_IEnumerator_00601_get_Current(), e2.System_Collections_Generic_IEnumerator_00601_get_Current()) or 0
                if c == 0:
                    b1 = e1.System_Collections_IEnumerator_MoveNext()
                    b2 = e2.System_Collections_IEnumerator_MoveNext()

            if c != 0:
                return c

            elif b1:
                return 1

            elif b2:
                return -1

            else: 
                return 0



def contains(value: _T, xs: IEnumerable[_T], comparer: IEqualityComparer[Any]) -> bool:
    with of_seq(xs) as e:
        found : bool = False
        while e.System_Collections_IEnumerator_MoveNext() if (not found) else False:
            found = comparer.Equals(value, e.System_Collections_Generic_IEnumerator_00601_get_Current())
        return found


def enumerate_from_functions(create: Callable[[], __A], move_next: Callable[[__A], bool], current: Callable[[__A], __B]) -> IEnumerable[__B]:
    def arrow_152(x: Optional[__A]=None, create: Callable[[], __A]=create, move_next: Callable[[__A], bool]=move_next, current: Callable[[__A], __B]=current) -> Optional[__B]:
        return some(current(x)) if move_next(x) else None

    def arrow_153(x_1: Optional[__A]=None, create: Callable[[], __A]=create, move_next: Callable[[__A], bool]=move_next, current: Callable[[__A], __B]=current) -> None:
        match_value : Any = x_1
        if is_disposable(match_value):
            dispose_2(match_value)


    return generate(create, arrow_152, arrow_153)


def enumerate_then_finally(source: IEnumerable[_T], compensation: Callable[[], None]) -> IEnumerable[_T]:
    compensation_1 : Callable[[], None] = compensation
    def arrow_154(source: IEnumerable[_T]=source, compensation: Callable[[], None]=compensation) -> IEnumerator[_T]:
        try: 
            return Enumerator_enumerateThenFinally(compensation_1, of_seq(source))

        except Exception as match_value:
            compensation_1()
            raise match_value


    return mk_seq(arrow_154)


def enumerate_using(resource: _T, source: Callable[[_T], __A]) -> IEnumerable[_U]:
    def compensation(resource: _T=resource, source: Callable[[_T], __A]=source) -> None:
        if equals(resource, None):
            pass

        else: 
            copy_of_struct : _T = resource
            dispose_2(copy_of_struct)


    def arrow_155(resource: _T=resource, source: Callable[[_T], __A]=source) -> IEnumerator[_U]:
        try: 
            return Enumerator_enumerateThenFinally(compensation, of_seq(source(resource)))

        except Exception as match_value_1:
            compensation()
            raise match_value_1


    return mk_seq(arrow_155)


def enumerate_while(guard: Callable[[], bool], xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_156(i: int, guard: Callable[[], bool]=guard, xs: IEnumerable[_T]=xs) -> Optional[Tuple[IEnumerable[_T], int]]:
        return ((xs, i + 1)) if guard() else None

    return concat(unfold(arrow_156, 0))


def filter(f: Callable[[_T], bool], xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def chooser(x: Optional[_T]=None, f: Callable[[_T], bool]=f, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        if f(x):
            return some(x)

        else: 
            return None


    return choose(chooser, xs)


def exists(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> bool:
    with of_seq(xs) as e:
        found : bool = False
        while e.System_Collections_IEnumerator_MoveNext() if (not found) else False:
            found = predicate(e.System_Collections_Generic_IEnumerator_00601_get_Current())
        return found


def exists2(predicate: Any, xs: IEnumerable[_T1], ys: IEnumerable[_T2]) -> bool:
    with of_seq(xs) as e1:
        with of_seq(ys) as e2:
            found : bool = False
            while e2.System_Collections_IEnumerator_MoveNext() if (e1.System_Collections_IEnumerator_MoveNext() if (not found) else False) else False:
                found = predicate(e1.System_Collections_Generic_IEnumerator_00601_get_Current(), e2.System_Collections_Generic_IEnumerator_00601_get_Current())
            return found


def exactly_one(xs: IEnumerable[_T]) -> _T:
    with of_seq(xs) as e:
        if e.System_Collections_IEnumerator_MoveNext():
            v : _T = e.System_Collections_Generic_IEnumerator_00601_get_Current()
            if e.System_Collections_IEnumerator_MoveNext():
                raise Exception((SR_inputSequenceTooLong + "\\nParameter name: ") + "source")

            else: 
                return v


        else: 
            raise Exception((SR_inputSequenceEmpty + "\\nParameter name: ") + "source")



def try_exactly_one(xs: IEnumerable[_T]) -> Optional[_T]:
    with of_seq(xs) as e:
        if e.System_Collections_IEnumerator_MoveNext():
            v : _T = e.System_Collections_Generic_IEnumerator_00601_get_Current()
            if e.System_Collections_IEnumerator_MoveNext():
                return None

            else: 
                return some(v)


        else: 
            return None



def try_find(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> Optional[_T]:
    with of_seq(xs) as e:
        res : Optional[_T] = None
        while e.System_Collections_IEnumerator_MoveNext() if (res is None) else False:
            c : _T = e.System_Collections_Generic_IEnumerator_00601_get_Current()
            if predicate(c):
                res = some(c)

        return res


def find(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> _T:
    match_value : Optional[_T] = try_find(predicate, xs)
    if match_value is None:
        return index_not_found()

    else: 
        return value_1(match_value)



def try_find_back(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> Optional[_T]:
    return try_find_back_1(predicate, to_array(xs))


def find_back(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> _T:
    match_value : Optional[_T] = try_find_back(predicate, xs)
    if match_value is None:
        return index_not_found()

    else: 
        return value_1(match_value)



def try_find_index(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> Optional[int]:
    with of_seq(xs) as e:
        def loop(i_mut: int, predicate: Callable[[_T], bool]=predicate, xs: IEnumerable[_T]=xs) -> Optional[int]:
            while True:
                (i,) = (i_mut,)
                if e.System_Collections_IEnumerator_MoveNext():
                    if predicate(e.System_Collections_Generic_IEnumerator_00601_get_Current()):
                        return i

                    else: 
                        i_mut = i + 1
                        continue


                else: 
                    return None

                break

        loop : Callable[[int], Optional[int]] = loop
        return loop(0)


def find_index(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> int:
    match_value : Optional[int] = try_find_index(predicate, xs)
    if match_value is None:
        return index_not_found()

    else: 
        return match_value



def try_find_index_back(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> Optional[int]:
    return try_find_index_back_1(predicate, to_array(xs))


def find_index_back(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> int:
    match_value : Optional[int] = try_find_index_back(predicate, xs)
    if match_value is None:
        return index_not_found()

    else: 
        return match_value



def fold(folder: Any, state: _STATE, xs: IEnumerable[_T]) -> _STATE:
    with of_seq(xs) as e:
        acc : _STATE = state
        while e.System_Collections_IEnumerator_MoveNext():
            acc = folder(acc, e.System_Collections_Generic_IEnumerator_00601_get_Current())
        return acc


def fold_back(folder: Any, xs: IEnumerable[_T], state: __A) -> __A:
    return fold_back_1(folder, to_array(xs), state)


def fold2(folder: Any, state: _STATE, xs: IEnumerable[_T1], ys: IEnumerable[_T2]) -> _STATE:
    with of_seq(xs) as e1:
        with of_seq(ys) as e2:
            acc : _STATE = state
            while e2.System_Collections_IEnumerator_MoveNext() if e1.System_Collections_IEnumerator_MoveNext() else False:
                acc = folder(acc, e1.System_Collections_Generic_IEnumerator_00601_get_Current(), e2.System_Collections_Generic_IEnumerator_00601_get_Current())
            return acc


def fold_back2(folder: Any, xs: IEnumerable[_T1], ys: IEnumerable[_T2], state: _STATE) -> _STATE:
    return fold_back2_1(folder, to_array(xs), to_array(ys), state)


def for_all(predicate: Callable[[__A], bool], xs: IEnumerable[__A]) -> bool:
    def arrow_157(x: Optional[__A]=None, predicate: Callable[[__A], bool]=predicate, xs: IEnumerable[__A]=xs) -> bool:
        return not predicate(x)

    return not exists(arrow_157, xs)


def for_all2(predicate: Any, xs: IEnumerable[__A], ys: IEnumerable[__B]) -> bool:
    def arrow_158(x: __A, y: __B, predicate: Any=predicate, xs: IEnumerable[__A]=xs, ys: IEnumerable[__B]=ys) -> bool:
        return not predicate(x, y)

    return not exists2(arrow_158, xs, ys)


def try_head(xs: IEnumerable[_T]) -> Optional[_T]:
    if is_array_like(xs):
        return try_head_1(xs)

    elif isinstance(xs, FSharpList):
        return try_head_2(xs)

    else: 
        with of_seq(xs) as e:
            if e.System_Collections_IEnumerator_MoveNext():
                return some(e.System_Collections_Generic_IEnumerator_00601_get_Current())

            else: 
                return None




def head(xs: IEnumerable[_T]) -> _T:
    match_value : Optional[_T] = try_head(xs)
    if match_value is None:
        raise Exception((SR_inputSequenceEmpty + "\\nParameter name: ") + "source")

    else: 
        return value_1(match_value)



def initialize(count: int, f: Callable[[int], __A]) -> IEnumerable[__A]:
    def arrow_159(i: int, count: int=count, f: Callable[[int], __A]=f) -> Optional[Tuple[__A, int]]:
        return ((f(i), i + 1)) if (i < count) else None

    return unfold(arrow_159, 0)


def initialize_infinite(f: Callable[[int], __A]) -> IEnumerable[__A]:
    return initialize(2147483647, f)


def is_empty(xs: IEnumerable[_T]) -> bool:
    if is_array_like(xs):
        return len(xs) == 0

    elif isinstance(xs, FSharpList):
        return is_empty_1(xs)

    else: 
        with of_seq(xs) as e:
            return not e.System_Collections_IEnumerator_MoveNext()



def try_item(index: int, xs: IEnumerable[_T]) -> Optional[_T]:
    if is_array_like(xs):
        return try_item_1(index, xs)

    elif isinstance(xs, FSharpList):
        return try_item_2(index, xs)

    else: 
        with of_seq(xs) as e:
            def loop(index_1_mut: int, index: int=index, xs: IEnumerable[_T]=xs) -> Optional[_T]:
                while True:
                    (index_1,) = (index_1_mut,)
                    if not e.System_Collections_IEnumerator_MoveNext():
                        return None

                    elif index_1 == 0:
                        return some(e.System_Collections_Generic_IEnumerator_00601_get_Current())

                    else: 
                        index_1_mut = index_1 - 1
                        continue

                    break

            loop : Callable[[int], Optional[_T]] = loop
            return loop(index)



def item(index: int, xs: IEnumerable[_T]) -> _T:
    match_value : Optional[_T] = try_item(index, xs)
    if match_value is None:
        raise Exception((SR_notEnoughElements + "\\nParameter name: ") + "index")

    else: 
        return value_1(match_value)



def iterate(action: Callable[[__A], None], xs: IEnumerable[__A]) -> None:
    def arrow_160(unit_var: None, x: __A, action: Callable[[__A], None]=action, xs: IEnumerable[__A]=xs) -> None:
        action(x)

    fold(arrow_160, None, xs)


def iterate2(action: Any, xs: IEnumerable[__A], ys: IEnumerable[__B]) -> None:
    def arrow_161(unit_var: None, x: __A, y: __B, action: Any=action, xs: IEnumerable[__A]=xs, ys: IEnumerable[__B]=ys) -> None:
        action(x, y)

    fold2(arrow_161, None, xs, ys)


def iterate_indexed(action: Any, xs: IEnumerable[__A]) -> None:
    def arrow_162(i: int, x: __A, action: Any=action, xs: IEnumerable[__A]=xs) -> int:
        action(i, x)
        return i + 1

    ignore(fold(arrow_162, 0, xs))


def iterate_indexed2(action: Any, xs: IEnumerable[__A], ys: IEnumerable[__B]) -> None:
    def arrow_163(i: int, x: __A, y: __B, action: Any=action, xs: IEnumerable[__A]=xs, ys: IEnumerable[__B]=ys) -> int:
        action(i, x, y)
        return i + 1

    ignore(fold2(arrow_163, 0, xs, ys))


def try_last(xs: IEnumerable[_T]) -> Optional[_T]:
    with of_seq(xs) as e:
        def loop(acc_mut: Optional[_T]=None, xs: IEnumerable[_T]=xs) -> _T:
            while True:
                (acc,) = (acc_mut,)
                if not e.System_Collections_IEnumerator_MoveNext():
                    return acc

                else: 
                    acc_mut = e.System_Collections_Generic_IEnumerator_00601_get_Current()
                    continue

                break

        loop : Callable[[_T], _T] = loop
        if e.System_Collections_IEnumerator_MoveNext():
            return some(loop(e.System_Collections_Generic_IEnumerator_00601_get_Current()))

        else: 
            return None



def last(xs: IEnumerable[_T]) -> _T:
    match_value : Optional[_T] = try_last(xs)
    if match_value is None:
        raise Exception((SR_notEnoughElements + "\\nParameter name: ") + "source")

    else: 
        return value_1(match_value)



def length(xs: IEnumerable[_T]) -> int:
    if is_array_like(xs):
        return len(xs)

    elif isinstance(xs, FSharpList):
        return length_1(xs)

    else: 
        with of_seq(xs) as e:
            count : int = 0
            while e.System_Collections_IEnumerator_MoveNext():
                count = (count + 1) or 0
            return count



def map(mapping: Callable[[_T], _U], xs: IEnumerable[_T]) -> IEnumerable[_U]:
    def arrow_164(mapping: Callable[[_T], _U]=mapping, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_165(e: IEnumerator[_T], mapping: Callable[[_T], _U]=mapping, xs: IEnumerable[_T]=xs) -> Optional[_U]:
        return some(mapping(e.System_Collections_Generic_IEnumerator_00601_get_Current())) if e.System_Collections_IEnumerator_MoveNext() else None

    def arrow_166(e_1: IEnumerator[_T], mapping: Callable[[_T], _U]=mapping, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate(arrow_164, arrow_165, arrow_166)


def map_indexed(mapping: Any, xs: IEnumerable[_T]) -> IEnumerable[_U]:
    def arrow_167(mapping: Any=mapping, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_168(i: int, e: IEnumerator[_T], mapping: Any=mapping, xs: IEnumerable[_T]=xs) -> Optional[_U]:
        return some(mapping(i, e.System_Collections_Generic_IEnumerator_00601_get_Current())) if e.System_Collections_IEnumerator_MoveNext() else None

    def arrow_169(e_1: IEnumerator[_T], mapping: Any=mapping, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate_indexed(arrow_167, arrow_168, arrow_169)


def indexed(xs: IEnumerable[_T]) -> IEnumerable[Tuple[int, _T]]:
    def mapping(i: int, x: _T, xs: IEnumerable[_T]=xs) -> Tuple[int, _T]:
        return (i, x)

    return map_indexed(mapping, xs)


def map2(mapping: Any, xs: IEnumerable[_T1], ys: IEnumerable[_T2]) -> IEnumerable[_U]:
    def arrow_170(mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> Tuple[IEnumerator[_T1], IEnumerator[_T2]]:
        return (of_seq(xs), of_seq(ys))

    def arrow_171(tupled_arg: Tuple[IEnumerator[_T1], IEnumerator[_T2]], mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> Optional[_U]:
        e1 : IEnumerator[_T1] = tupled_arg[0]
        e2 : IEnumerator[_T2] = tupled_arg[1]
        return some(mapping(e1.System_Collections_Generic_IEnumerator_00601_get_Current(), e2.System_Collections_Generic_IEnumerator_00601_get_Current())) if (e2.System_Collections_IEnumerator_MoveNext() if e1.System_Collections_IEnumerator_MoveNext() else False) else None

    def arrow_172(tupled_arg_1: Tuple[IEnumerator[_T1], IEnumerator[_T2]], mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> None:
        try: 
            dispose_2(tupled_arg_1[0])

        finally: 
            dispose_2(tupled_arg_1[1])


    return generate(arrow_170, arrow_171, arrow_172)


def map_indexed2(mapping: Any, xs: IEnumerable[_T1], ys: IEnumerable[_T2]) -> IEnumerable[_U]:
    def arrow_173(mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> Tuple[IEnumerator[_T1], IEnumerator[_T2]]:
        return (of_seq(xs), of_seq(ys))

    def arrow_174(i: int, tupled_arg: Tuple[IEnumerator[_T1], IEnumerator[_T2]], mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> Optional[_U]:
        e1 : IEnumerator[_T1] = tupled_arg[0]
        e2 : IEnumerator[_T2] = tupled_arg[1]
        return some(mapping(i, e1.System_Collections_Generic_IEnumerator_00601_get_Current(), e2.System_Collections_Generic_IEnumerator_00601_get_Current())) if (e2.System_Collections_IEnumerator_MoveNext() if e1.System_Collections_IEnumerator_MoveNext() else False) else None

    def arrow_175(tupled_arg_1: Tuple[IEnumerator[_T1], IEnumerator[_T2]], mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> None:
        try: 
            dispose_2(tupled_arg_1[0])

        finally: 
            dispose_2(tupled_arg_1[1])


    return generate_indexed(arrow_173, arrow_174, arrow_175)


def map3(mapping: Any, xs: IEnumerable[_T1], ys: IEnumerable[_T2], zs: IEnumerable[_T3]) -> IEnumerable[_U]:
    def arrow_176(mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys, zs: IEnumerable[_T3]=zs) -> Tuple[IEnumerator[_T1], IEnumerator[_T2], IEnumerator[_T3]]:
        return (of_seq(xs), of_seq(ys), of_seq(zs))

    def arrow_177(tupled_arg: Tuple[IEnumerator[_T1], IEnumerator[_T2], IEnumerator[_T3]], mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys, zs: IEnumerable[_T3]=zs) -> Optional[_U]:
        e1 : IEnumerator[_T1] = tupled_arg[0]
        e2 : IEnumerator[_T2] = tupled_arg[1]
        e3 : IEnumerator[_T3] = tupled_arg[2]
        return some(mapping(e1.System_Collections_Generic_IEnumerator_00601_get_Current(), e2.System_Collections_Generic_IEnumerator_00601_get_Current(), e3.System_Collections_Generic_IEnumerator_00601_get_Current())) if (e3.System_Collections_IEnumerator_MoveNext() if (e2.System_Collections_IEnumerator_MoveNext() if e1.System_Collections_IEnumerator_MoveNext() else False) else False) else None

    def arrow_178(tupled_arg_1: Tuple[IEnumerator[_T1], IEnumerator[_T2], IEnumerator[_T3]], mapping: Any=mapping, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys, zs: IEnumerable[_T3]=zs) -> None:
        try: 
            dispose_2(tupled_arg_1[0])

        finally: 
            try: 
                dispose_2(tupled_arg_1[1])

            finally: 
                dispose_2(tupled_arg_1[2])



    return generate(arrow_176, arrow_177, arrow_178)


def read_only(xs: IEnumerable[_T]) -> IEnumerable[_T]:
    check_non_null("source", xs)
    def arrow_179(x: Optional[_T]=None, xs: IEnumerable[_T]=xs) -> _T:
        return x

    return map(arrow_179, xs)


def expr_180(gen0: TypeInfo) -> TypeInfo:
    return class_type("SeqModule.CachedSeq`1", [gen0], CachedSeq_1)


class CachedSeq_1(IDisposable, Generic[_T]):
    def __init__(self, cleanup: Callable[[], None], res: IEnumerable[_T]) -> None:
        self.cleanup = cleanup
        self.res = res

    def Dispose(self) -> None:
        _ : CachedSeq_1[_T] = self
        _.cleanup()

    def GetEnumerator(self) -> IEnumerator[_T]:
        _ : CachedSeq_1[_T] = self
        return get_enumerator(_.res)

    def __iter__(self) -> IEnumerator[_T]:
        return to_iterator(self.GetEnumerator())

    def System_Collections_IEnumerable_GetEnumerator(self) -> IEnumerator[Any]:
        _ : CachedSeq_1[_T] = self
        return get_enumerator(_.res)


CachedSeq_1_reflection = expr_180

def CachedSeq_1__ctor_Z7A8347D4(cleanup: Callable[[], None], res: IEnumerable[_T]) -> CachedSeq_1[_T]:
    return CachedSeq_1(cleanup, res)


def CachedSeq_1__Clear(_: CachedSeq_1[_T]) -> None:
    _.cleanup()


def cache(source: IEnumerable[_T]) -> IEnumerable[_T]:
    check_non_null("source", source)
    prefix : Array[_T] = []
    enumerator_r : Optional[Optional[IEnumerator[_T]]] = None
    def one_step_to(i: int, source: IEnumerable[_T]=source) -> None:
        nonlocal enumerator_r
        if i >= len(prefix):
            opt_enumerator_2 : Optional[IEnumerator[_T]]
            if enumerator_r is not None:
                opt_enumerator_2 = value_1(enumerator_r)

            else: 
                opt_enumerator : Optional[IEnumerator[_T]] = get_enumerator(source)
                enumerator_r = some(opt_enumerator)
                opt_enumerator_2 = opt_enumerator

            if opt_enumerator_2 is None:
                pass

            else: 
                enumerator : IEnumerator[_T] = opt_enumerator_2
                if enumerator.System_Collections_IEnumerator_MoveNext():
                    (prefix.append(enumerator.System_Collections_Generic_IEnumerator_00601_get_Current()))

                else: 
                    dispose_2(enumerator)
                    enumerator_r = some(None)




    def cleanup(source: IEnumerable[_T]=source) -> None:
        def arrow_181(__unit: Any=None) -> None:
            nonlocal enumerator_r
            clear(prefix)
            (pattern_matching_result, e) = (None, None)
            if enumerator_r is not None:
                if value_1(enumerator_r) is not None:
                    pattern_matching_result = 0
                    e = value_1(enumerator_r)

                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1

            if pattern_matching_result == 0:
                dispose_2(e)

            enumerator_r = None

        Operators_Lock(prefix, arrow_181)

    def arrow_183(i_1: int, source: IEnumerable[_T]=source) -> Optional[Tuple[_T, int]]:
        def arrow_182(__unit: Any=None) -> Optional[Tuple[_T, int]]:
            if i_1 < len(prefix):
                return (prefix[i_1], i_1 + 1)

            else: 
                one_step_to(i_1)
                return ((prefix[i_1], i_1 + 1)) if (i_1 < len(prefix)) else None


        return Operators_Lock(prefix, arrow_182)

    return CachedSeq_1__ctor_Z7A8347D4(cleanup, unfold(arrow_183, 0))


def all_pairs(xs: IEnumerable[_T1], ys: IEnumerable[_T2]) -> IEnumerable[Tuple[_T1, _T2]]:
    ys_cache : IEnumerable[_T2] = cache(ys)
    def arrow_184(xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> IEnumerable[Tuple[_T1, _T2]]:
        def mapping_1(x: Optional[__A]=None) -> IEnumerable[Tuple[__A, _T2]]:
            def mapping(y: Optional[_T2]=None, x: __A=x) -> Tuple[__A, _T2]:
                return (x, y)

            return map(mapping, ys_cache)

        return concat(map(mapping_1, xs))

    return delay(arrow_184)


def map_fold(mapping: Any, state: _STATE, xs: IEnumerable[_T]) -> Tuple[IEnumerable[_RESULT], _STATE]:
    pattern_input : Tuple[Array[_RESULT], _STATE] = map_fold_1(mapping, state, to_array(xs), None)
    return (read_only(pattern_input[0]), pattern_input[1])


def map_fold_back(mapping: Any, xs: IEnumerable[_T], state: _STATE) -> Tuple[IEnumerable[_RESULT], _STATE]:
    pattern_input : Tuple[Array[_RESULT], _STATE] = map_fold_back_1(mapping, to_array(xs), state, None)
    return (read_only(pattern_input[0]), pattern_input[1])


def try_pick(chooser: Callable[[_T], Optional[__A]], xs: IEnumerable[_T]) -> Optional[__A]:
    with of_seq(xs) as e:
        res : Optional[__A] = None
        while e.System_Collections_IEnumerator_MoveNext() if (res is None) else False:
            res = chooser(e.System_Collections_Generic_IEnumerator_00601_get_Current())
        return res


def pick(chooser: Callable[[_T], Optional[__A]], xs: IEnumerable[_T]) -> __A:
    match_value : Optional[__A] = try_pick(chooser, xs)
    if match_value is None:
        return index_not_found()

    else: 
        return value_1(match_value)



def reduce(folder: Any, xs: IEnumerable[_T]) -> _T:
    with of_seq(xs) as e:
        def loop(acc_mut: Optional[_T]=None, folder: Any=folder, xs: IEnumerable[_T]=xs) -> _T:
            while True:
                (acc,) = (acc_mut,)
                if e.System_Collections_IEnumerator_MoveNext():
                    acc_mut = folder(acc, e.System_Collections_Generic_IEnumerator_00601_get_Current())
                    continue

                else: 
                    return acc

                break

        loop : Callable[[_T], _T] = loop
        if e.System_Collections_IEnumerator_MoveNext():
            return loop(e.System_Collections_Generic_IEnumerator_00601_get_Current())

        else: 
            raise Exception(SR_inputSequenceEmpty)



def reduce_back(folder: Any, xs: IEnumerable[_T]) -> _T:
    arr : Array[_T] = to_array(xs)
    if len(arr) > 0:
        return reduce_back_1(folder, arr)

    else: 
        raise Exception(SR_inputSequenceEmpty)



def replicate(n: int, x: __A) -> IEnumerable[__A]:
    def arrow_185(_arg: int, n: int=n, x: __A=x) -> __A:
        return x

    return initialize(n, arrow_185)


def reverse(xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_186(xs: IEnumerable[_T]=xs) -> IEnumerable[_T]:
        return of_array(reverse_1(to_array(xs)))

    return delay(arrow_186)


def scan(folder: Any, state: _STATE, xs: IEnumerable[_T]) -> IEnumerable[_STATE]:
    def arrow_187(folder: Any=folder, state: _STATE=state, xs: IEnumerable[_T]=xs) -> IEnumerable[_STATE]:
        acc : _STATE = state
        def mapping(x: Optional[_T]=None) -> _STATE:
            nonlocal acc
            acc = folder(acc, x)
            return acc

        return concat([singleton(state), map(mapping, xs)])

    return delay(arrow_187)


def scan_back(folder: Any, xs: IEnumerable[_T], state: _STATE) -> IEnumerable[_STATE]:
    def arrow_188(folder: Any=folder, xs: IEnumerable[_T]=xs, state: _STATE=state) -> IEnumerable[_STATE]:
        return of_array(scan_back_1(folder, to_array(xs), state, None))

    return delay(arrow_188)


def skip(count: int, source: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_189(count: int=count, source: IEnumerable[_T]=source) -> IEnumerator[_T]:
        e : IEnumerator[_T] = of_seq(source)
        try: 
            for _ in range(1, count + 1, 1):
                if not e.System_Collections_IEnumerator_MoveNext():
                    raise Exception((SR_notEnoughElements + "\\nParameter name: ") + "source")

            def compensation(__unit: Any=None) -> None:
                pass

            return Enumerator_enumerateThenFinally(compensation, e)

        except Exception as match_value:
            dispose_2(e)
            raise match_value


    return mk_seq(arrow_189)


def skip_while(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_190(predicate: Callable[[_T], bool]=predicate, xs: IEnumerable[_T]=xs) -> IEnumerable[_T]:
        skipped : bool = True
        def f(x: Optional[_T]=None) -> bool:
            nonlocal skipped
            if skipped:
                skipped = predicate(x)

            return not skipped

        return filter(f, xs)

    return delay(arrow_190)


def tail(xs: IEnumerable[_T]) -> IEnumerable[_T]:
    return skip(1, xs)


def take(count: int, xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_191(count: int=count, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_192(i: int, e: IEnumerator[_T], count: int=count, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        if i < count:
            if e.System_Collections_IEnumerator_MoveNext():
                return some(e.System_Collections_Generic_IEnumerator_00601_get_Current())

            else: 
                raise Exception((SR_notEnoughElements + "\\nParameter name: ") + "source")


        else: 
            return None


    def arrow_193(e_1: IEnumerator[_T], count: int=count, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate_indexed(arrow_191, arrow_192, arrow_193)


def take_while(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_194(predicate: Callable[[_T], bool]=predicate, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_195(e: IEnumerator[_T], predicate: Callable[[_T], bool]=predicate, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        return some(e.System_Collections_Generic_IEnumerator_00601_get_Current()) if (predicate(e.System_Collections_Generic_IEnumerator_00601_get_Current()) if e.System_Collections_IEnumerator_MoveNext() else False) else None

    def arrow_196(e_1: IEnumerator[_T], predicate: Callable[[_T], bool]=predicate, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate(arrow_194, arrow_195, arrow_196)


def truncate(count: int, xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_197(count: int=count, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_198(i: int, e: IEnumerator[_T], count: int=count, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        return some(e.System_Collections_Generic_IEnumerator_00601_get_Current()) if (e.System_Collections_IEnumerator_MoveNext() if (i < count) else False) else None

    def arrow_199(e_1: IEnumerator[_T], count: int=count, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate_indexed(arrow_197, arrow_198, arrow_199)


def zip(xs: IEnumerable[_T1], ys: IEnumerable[_T2]) -> IEnumerable[Tuple[_T1, _T2]]:
    def arrow_200(x: _T1, y: _T2, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys) -> Tuple[_T1, _T2]:
        return (x, y)

    return map2(arrow_200, xs, ys)


def zip3(xs: IEnumerable[_T1], ys: IEnumerable[_T2], zs: IEnumerable[_T3]) -> IEnumerable[Tuple[_T1, _T2, _T3]]:
    def arrow_201(x: _T1, y: _T2, z: _T3, xs: IEnumerable[_T1]=xs, ys: IEnumerable[_T2]=ys, zs: IEnumerable[_T3]=zs) -> Tuple[_T1, _T2, _T3]:
        return (x, y, z)

    return map3(arrow_201, xs, ys, zs)


def collect(mapping: Callable[[_T], IEnumerable[_U]], xs: IEnumerable[_T]) -> IEnumerable[_U]:
    def arrow_202(mapping: Callable[[_T], IEnumerable[_U]]=mapping, xs: IEnumerable[_T]=xs) -> IEnumerable[_U]:
        return concat(map(mapping, xs))

    return delay(arrow_202)


def where(predicate: Callable[[_T], bool], xs: IEnumerable[_T]) -> IEnumerable[_T]:
    return filter(predicate, xs)


def pairwise(xs: IEnumerable[_T]) -> IEnumerable[Tuple[_T, _T]]:
    def arrow_203(xs: IEnumerable[_T]=xs) -> IEnumerable[Tuple[_T, _T]]:
        return of_array(pairwise_1(to_array(xs)))

    return delay(arrow_203)


def split_into(chunks: int, xs: IEnumerable[_T]) -> IEnumerable[IEnumerable[_T]]:
    def arrow_204(chunks: int=chunks, xs: IEnumerable[_T]=xs) -> IEnumerable[IEnumerable[_T]]:
        def mapping(arr: Array[_T]) -> IEnumerable[_T]:
            return of_array(arr)

        return of_array(map_1(mapping, split_into_1(chunks, to_array(xs)), None))

    return delay(arrow_204)


def windowed(window_size: int, xs: IEnumerable[_T]) -> IEnumerable[IEnumerable[_T]]:
    def arrow_205(window_size: int=window_size, xs: IEnumerable[_T]=xs) -> IEnumerable[IEnumerable[_T]]:
        def mapping(arr: Array[_T]) -> IEnumerable[_T]:
            return of_array(arr)

        return of_array(map_1(mapping, windowed_1(window_size, to_array(xs)), None))

    return delay(arrow_205)


def transpose(xss: IEnumerable[__A]) -> IEnumerable[IEnumerable[_T]]:
    def arrow_206(xss: IEnumerable[__A]=xss) -> IEnumerable[IEnumerable[_T]]:
        def mapping_1(arr: Array[_T]) -> IEnumerable[_T]:
            return of_array(arr)

        def mapping(xs_1: Optional[__A]=None) -> Array[_T]:
            return to_array(xs_1)

        return of_array(map_1(mapping_1, transpose_1(map_1(mapping, to_array(xss), None), None), None))

    return delay(arrow_206)


def sort_with(comparer: Any, xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_207(comparer: Any=comparer, xs: IEnumerable[_T]=xs) -> IEnumerable[_T]:
        arr : Array[_T] = to_array(xs)
        arr.sort()
        return of_array(arr)

    return delay(arrow_207)


def sort(xs: IEnumerable[_T], comparer: IComparer[_T]) -> IEnumerable[_T]:
    def arrow_208(x: _T, y: _T, xs: IEnumerable[_T]=xs, comparer: IComparer[_T]=comparer) -> int:
        return comparer.Compare(x, y)

    return sort_with(arrow_208, xs)


def sort_by(projection: Callable[[_T], _U], xs: IEnumerable[_T], comparer: IComparer[_U]) -> IEnumerable[_T]:
    def arrow_209(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: IEnumerable[_T]=xs, comparer: IComparer[_U]=comparer) -> int:
        return comparer.Compare(projection(x), projection(y))

    return sort_with(arrow_209, xs)


def sort_descending(xs: IEnumerable[_T], comparer: IComparer[_T]) -> IEnumerable[_T]:
    def arrow_210(x: _T, y: _T, xs: IEnumerable[_T]=xs, comparer: IComparer[_T]=comparer) -> int:
        return comparer.Compare(x, y) * -1

    return sort_with(arrow_210, xs)


def sort_by_descending(projection: Callable[[_T], _U], xs: IEnumerable[_T], comparer: IComparer[_U]) -> IEnumerable[_T]:
    def arrow_211(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: IEnumerable[_T]=xs, comparer: IComparer[_U]=comparer) -> int:
        return comparer.Compare(projection(x), projection(y)) * -1

    return sort_with(arrow_211, xs)


def sum(xs: IEnumerable[_T], adder: IGenericAdder_1[_T]) -> _T:
    def arrow_212(acc: _T, x: _T, xs: IEnumerable[_T]=xs, adder: IGenericAdder_1[_T]=adder) -> _T:
        return adder.Add(acc, x)

    return fold(arrow_212, adder.GetZero(), xs)


def sum_by(f: Callable[[_T], _U], xs: IEnumerable[_T], adder: IGenericAdder_1[_U]) -> _U:
    def arrow_213(acc: _U, x: _T, f: Callable[[_T], _U]=f, xs: IEnumerable[_T]=xs, adder: IGenericAdder_1[_U]=adder) -> _U:
        return adder.Add(acc, f(x))

    return fold(arrow_213, adder.GetZero(), xs)


def max_by(projection: Callable[[_T], _U], xs: IEnumerable[_T], comparer: IComparer[_U]) -> _T:
    def arrow_214(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: IEnumerable[_T]=xs, comparer: IComparer[_U]=comparer) -> _T:
        return y if (comparer.Compare(projection(y), projection(x)) > 0) else x

    return reduce(arrow_214, xs)


def max(xs: IEnumerable[_T], comparer: IComparer[_T]) -> _T:
    def arrow_215(x: _T, y: _T, xs: IEnumerable[_T]=xs, comparer: IComparer[_T]=comparer) -> _T:
        return y if (comparer.Compare(y, x) > 0) else x

    return reduce(arrow_215, xs)


def min_by(projection: Callable[[_T], _U], xs: IEnumerable[_T], comparer: IComparer[_U]) -> _T:
    def arrow_216(x: _T, y: _T, projection: Callable[[_T], _U]=projection, xs: IEnumerable[_T]=xs, comparer: IComparer[_U]=comparer) -> _T:
        return x if (comparer.Compare(projection(y), projection(x)) > 0) else y

    return reduce(arrow_216, xs)


def min(xs: IEnumerable[_T], comparer: IComparer[_T]) -> _T:
    def arrow_217(x: _T, y: _T, xs: IEnumerable[_T]=xs, comparer: IComparer[_T]=comparer) -> _T:
        return x if (comparer.Compare(y, x) > 0) else y

    return reduce(arrow_217, xs)


def average(xs: IEnumerable[_T], averager: IGenericAverager_1[_T]) -> _T:
    count : int = 0
    def folder(acc: _T, x: _T, xs: IEnumerable[_T]=xs, averager: IGenericAverager_1[_T]=averager) -> _T:
        nonlocal count
        count = (count + 1) or 0
        return averager.Add(acc, x)

    total : _T = fold(folder, averager.GetZero(), xs)
    if count == 0:
        raise Exception((SR_inputSequenceEmpty + "\\nParameter name: ") + "source")

    else: 
        return averager.DivideByInt(total, count)



def average_by(f: Callable[[_T], _U], xs: IEnumerable[_T], averager: IGenericAverager_1[_U]) -> _U:
    count : int = 0
    def arrow_218(acc: _U, x: _T, f: Callable[[_T], _U]=f, xs: IEnumerable[_T]=xs, averager: IGenericAverager_1[_U]=averager) -> _U:
        nonlocal count
        count = (count + 1) or 0
        return averager.Add(acc, f(x))

    total : _U = fold(arrow_218, averager.GetZero(), xs)
    if count == 0:
        raise Exception((SR_inputSequenceEmpty + "\\nParameter name: ") + "source")

    else: 
        return averager.DivideByInt(total, count)



def permute(f: Callable[[int], int], xs: IEnumerable[_T]) -> IEnumerable[_T]:
    def arrow_219(f: Callable[[int], int]=f, xs: IEnumerable[_T]=xs) -> IEnumerable[_T]:
        return of_array(permute_1(f, to_array(xs)))

    return delay(arrow_219)


def chunk_by_size(chunk_size: int, xs: IEnumerable[_T]) -> IEnumerable[IEnumerable[_T]]:
    def arrow_220(chunk_size: int=chunk_size, xs: IEnumerable[_T]=xs) -> IEnumerable[IEnumerable[_T]]:
        def mapping(arr: Array[_T]) -> IEnumerable[_T]:
            return of_array(arr)

        return of_array(map_1(mapping, chunk_by_size_1(chunk_size, to_array(xs)), None))

    return delay(arrow_220)


def insert_at(index: int, y: _T, xs: IEnumerable[_T]) -> IEnumerable[_T]:
    is_done : bool = False
    if index < 0:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    def arrow_221(index: int=index, y: _T=y, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_222(i: int, e: IEnumerator[_T], index: int=index, y: _T=y, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        nonlocal is_done
        if e.System_Collections_IEnumerator_MoveNext() if (True if is_done else (i < index)) else False:
            return some(e.System_Collections_Generic_IEnumerator_00601_get_Current())

        elif i == index:
            is_done = True
            return some(y)

        else: 
            if not is_done:
                raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

            return None


    def arrow_223(e_1: IEnumerator[_T], index: int=index, y: _T=y, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate_indexed(arrow_221, arrow_222, arrow_223)


def insert_many_at(index: int, ys: IEnumerable[_T], xs: IEnumerable[_T]) -> IEnumerable[_T]:
    status : int = -1
    if index < 0:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    def arrow_224(index: int=index, ys: IEnumerable[_T]=ys, xs: IEnumerable[_T]=xs) -> Tuple[IEnumerator[_T], IEnumerator[_T]]:
        return (of_seq(xs), of_seq(ys))

    def arrow_225(i: int, tupled_arg: Tuple[IEnumerator[_T], IEnumerator[_T]], index: int=index, ys: IEnumerable[_T]=ys, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        nonlocal status
        e1 : IEnumerator[_T] = tupled_arg[0]
        e2 : IEnumerator[_T] = tupled_arg[1]
        if i == index:
            status = 0

        inserted : Optional[_T]
        if status == 0:
            if e2.System_Collections_IEnumerator_MoveNext():
                inserted = some(e2.System_Collections_Generic_IEnumerator_00601_get_Current())

            else: 
                status = 1
                inserted = None


        else: 
            inserted = None

        if inserted is None:
            if e1.System_Collections_IEnumerator_MoveNext():
                return some(e1.System_Collections_Generic_IEnumerator_00601_get_Current())

            else: 
                if status < 1:
                    raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

                return None


        else: 
            return some(value_1(inserted))


    def arrow_226(tupled_arg_1: Tuple[IEnumerator[_T], IEnumerator[_T]], index: int=index, ys: IEnumerable[_T]=ys, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(tupled_arg_1[0])
        dispose_2(tupled_arg_1[1])

    return generate_indexed(arrow_224, arrow_225, arrow_226)


def remove_at(index: int, xs: IEnumerable[_T]) -> IEnumerable[_T]:
    is_done : bool = False
    if index < 0:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    def arrow_227(index: int=index, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_228(i: int, e: IEnumerator[_T], index: int=index, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        nonlocal is_done
        if e.System_Collections_IEnumerator_MoveNext() if (True if is_done else (i < index)) else False:
            return some(e.System_Collections_Generic_IEnumerator_00601_get_Current())

        elif e.System_Collections_IEnumerator_MoveNext() if (i == index) else False:
            is_done = True
            return some(e.System_Collections_Generic_IEnumerator_00601_get_Current()) if e.System_Collections_IEnumerator_MoveNext() else None

        else: 
            if not is_done:
                raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

            return None


    def arrow_229(e_1: IEnumerator[_T], index: int=index, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate_indexed(arrow_227, arrow_228, arrow_229)


def remove_many_at(index: int, count: int, xs: IEnumerable[_T]) -> IEnumerable[_T]:
    if index < 0:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    def arrow_230(index: int=index, count: int=count, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_231(i: int, e: IEnumerator[_T], index: int=index, count: int=count, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        if i < index:
            if e.System_Collections_IEnumerator_MoveNext():
                return some(e.System_Collections_Generic_IEnumerator_00601_get_Current())

            else: 
                raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")


        else: 
            if i == index:
                for _ in range(1, count + 1, 1):
                    if not e.System_Collections_IEnumerator_MoveNext():
                        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "count")


            return some(e.System_Collections_Generic_IEnumerator_00601_get_Current()) if e.System_Collections_IEnumerator_MoveNext() else None


    def arrow_232(e_1: IEnumerator[_T], index: int=index, count: int=count, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate_indexed(arrow_230, arrow_231, arrow_232)


def update_at(index: int, y: _T, xs: IEnumerable[_T]) -> IEnumerable[_T]:
    is_done : bool = False
    if index < 0:
        raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

    def arrow_233(index: int=index, y: _T=y, xs: IEnumerable[_T]=xs) -> IEnumerator[_T]:
        return of_seq(xs)

    def arrow_234(i: int, e: IEnumerator[_T], index: int=index, y: _T=y, xs: IEnumerable[_T]=xs) -> Optional[_T]:
        nonlocal is_done
        if e.System_Collections_IEnumerator_MoveNext() if (True if is_done else (i < index)) else False:
            return some(e.System_Collections_Generic_IEnumerator_00601_get_Current())

        elif e.System_Collections_IEnumerator_MoveNext() if (i == index) else False:
            is_done = True
            return some(y)

        else: 
            if not is_done:
                raise Exception((SR_indexOutOfBounds + "\\nParameter name: ") + "index")

            return None


    def arrow_235(e_1: IEnumerator[_T], index: int=index, y: _T=y, xs: IEnumerable[_T]=xs) -> None:
        dispose_2(e_1)

    return generate_indexed(arrow_233, arrow_234, arrow_235)


