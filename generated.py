from fable_sedlex.sedlex import *
import typing
import typing_extensions
import dataclasses
_sedlex_rnd_39 = [ None, 1, 2, 3, 4, 4, 0 ]  # token_ids

def _sedlex_st_15(lexerbuf: lexbuf):
    result = -1
    mark(lexerbuf, 2)
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_38[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_rnd_37(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_15(lexerbuf)
    return result

def _sedlex_st_14(lexerbuf: lexbuf):
    result = -1
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_36[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_rnd_35(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_15(lexerbuf)
    return result

def _sedlex_st_13(lexerbuf: lexbuf):
    result = -1
    mark(lexerbuf, 2)
    state_id = _sedlex_decide_6(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_34[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_decide_6(c: int):
    if c <= 45:
        return -1
    else:
        if c <= 101:
            return _sedlex_DT_table_4[c - 46] - 1
        else:
            return -1

def _sedlex_rnd_33(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_14(lexerbuf)
    return result

def _sedlex_rnd_32(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_13(lexerbuf)
    return result

def _sedlex_rnd_31(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_9(lexerbuf)
    return result

def _sedlex_st_12(lexerbuf: lexbuf):
    result = -1
    mark(lexerbuf, 1)
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_30[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_rnd_29(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_12(lexerbuf)
    return result

def _sedlex_st_11(lexerbuf: lexbuf):
    result = -1
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_28[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_rnd_27(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_12(lexerbuf)
    return result

def _sedlex_st_10(lexerbuf: lexbuf):
    result = -1
    mark(lexerbuf, 1)
    state_id = _sedlex_decide_5(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_26[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_decide_5(c: int):
    if c <= 47:
        return -1
    else:
        if c <= 101:
            return _sedlex_DT_table_3[c - 48] - 1
        else:
            return -1

def _sedlex_rnd_25(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_11(lexerbuf)
    return result

def _sedlex_rnd_24(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_10(lexerbuf)
    return result

def _sedlex_st_9(lexerbuf: lexbuf):
    result = -1
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_23[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_decide_4(c: int):
    if c <= 47:
        return -1
    else:
        if c <= 57:
            return 0
        else:
            return -1

def _sedlex_rnd_22(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_10(lexerbuf)
    return result

def _sedlex_st_7(lexerbuf: lexbuf):
    result = -1
    mark(lexerbuf, 4)
    state_id = _sedlex_decide_3(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_21[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_decide_3(c: int):
    if c <= 60:
        return -1
    else:
        if c <= 61:
            return 0
        else:
            return -1

def _sedlex_rnd_20(lexerbuf: lexbuf):
    result = -1
    result = 5
    return result

def _sedlex_st_6(lexerbuf: lexbuf):
    result = -1
    mark(lexerbuf, 3)
    state_id = _sedlex_decide_2(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_19[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_rnd_18(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_5(lexerbuf)
    return result

def _sedlex_rnd_17(lexerbuf: lexbuf):
    result = -1
    result = 3
    return result

def _sedlex_rnd_16(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_3(lexerbuf)
    return result

def _sedlex_st_5(lexerbuf: lexbuf):
    result = -1
    state_id = _sedlex_decide_2(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_15[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_rnd_14(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_5(lexerbuf)
    return result

def _sedlex_rnd_13(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_6(lexerbuf)
    return result

def _sedlex_rnd_12(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_3(lexerbuf)
    return result

def _sedlex_st_3(lexerbuf: lexbuf):
    result = -1
    state_id = _sedlex_decide_2(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_11[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_decide_2(c: int):
    if c <= -1:
        return -1
    else:
        if c <= 92:
            return _sedlex_DT_table_2[c - 0] - 1
        else:
            return 0

def _sedlex_rnd_10(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_5(lexerbuf)
    return result

def _sedlex_rnd_9(lexerbuf: lexbuf):
    result = -1
    result = 3
    return result

def _sedlex_rnd_8(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_3(lexerbuf)
    return result

def _sedlex_st_0(lexerbuf: lexbuf):
    result = -1
    state_id = _sedlex_decide_1(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_7[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_decide_1(c: int):
    if c <= 57:
        return _sedlex_DT_table_1[c - -1] - 1
    else:
        return -1

def _sedlex_rnd_6(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_13(lexerbuf)
    return result

def _sedlex_rnd_5(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_9(lexerbuf)
    return result

def _sedlex_rnd_4(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_7(lexerbuf)
    return result

def _sedlex_rnd_3(lexerbuf: lexbuf):
    result = -1
    result = _sedlex_st_3(lexerbuf)
    return result

def _sedlex_rnd_2(lexerbuf: lexbuf):
    result = -1
    result = 0
    return result

def _sedlex_rnd_1(lexerbuf: lexbuf):
    result = -1
    result = 6
    return result


@dataclasses.dataclass
class Token:
    token_id: int
    lexeme : str
    line: int
    col: int
    span: int
    offset: int
    file: str

_Token = typing.TypeVar("_Token")

class TokenConstructor(typing_extensions.Protocol[_Token]):
    def __call__(self, token_id: int, lexeme: str, line: int, col: int, span: int, offset: int, file: str) -> _Token: ...

def lex(lexerbuf: lexbuf ,  construct_token: TokenConstructor[_Token]=Token):
    start(lexerbuf)
    case_id = _sedlex_st_0(lexerbuf)
    if case_id < 0: raise Exception("my error")
    token_id = _sedlex_rnd_39[case_id]
    if token_id is not None:
        return construct_token(token_id, lexeme(lexerbuf), lexerbuf.start_line, lexerbuf.pos - lexerbuf.curr_bol, lexerbuf.pos - lexerbuf.start_pos, lexerbuf.start_pos, lexerbuf.filename)
    return None
def lexall(buf: lexbuf, construct: TokenConstructor[_Token], is_eof: Callable[[_Token], bool]):
    while True:
        token = lex(buf, construct)
        if token is None: continue
        if is_eof(token): break
        yield token
_sedlex_rnd_38 = [_sedlex_rnd_37]

_sedlex_rnd_36 = [_sedlex_rnd_35]

_sedlex_DT_table_4 = [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]

_sedlex_rnd_34 = [_sedlex_rnd_31, _sedlex_rnd_32, _sedlex_rnd_33]

_sedlex_rnd_30 = [_sedlex_rnd_29]

_sedlex_rnd_28 = [_sedlex_rnd_27]

_sedlex_DT_table_3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]

_sedlex_rnd_26 = [_sedlex_rnd_24, _sedlex_rnd_25]

_sedlex_rnd_23 = [_sedlex_rnd_22]

_sedlex_rnd_21 = [_sedlex_rnd_20]

_sedlex_rnd_19 = [_sedlex_rnd_16, _sedlex_rnd_17, _sedlex_rnd_18]

_sedlex_rnd_15 = [_sedlex_rnd_12, _sedlex_rnd_13, _sedlex_rnd_14]

_sedlex_DT_table_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]

_sedlex_rnd_11 = [_sedlex_rnd_8, _sedlex_rnd_9, _sedlex_rnd_10]

_sedlex_DT_table_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

_sedlex_rnd_7 = [_sedlex_rnd_1, _sedlex_rnd_2, _sedlex_rnd_3, _sedlex_rnd_4, _sedlex_rnd_5, _sedlex_rnd_6]

