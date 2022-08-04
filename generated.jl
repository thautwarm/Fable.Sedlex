
include("rts/sedlex_julia_rt.jl")
is_eof(x) = x.token_id == 0

const _sedlex_rnd_39 = [ nothing, Int32(1), Int32(2), Int32(3), Int32(4), Int32(4), Int32(0) ]  # token_ids
function _sedlex_st_15(lexerbuf::lexbuf)
    result = Int32(-1)
    mark(lexerbuf, 2)
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_38, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_rnd_37(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_15(lexerbuf)
    return result
end
function _sedlex_st_14(lexerbuf::lexbuf)
    result = Int32(-1)
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_36, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_rnd_35(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_15(lexerbuf)
    return result
end
function _sedlex_st_13(lexerbuf::lexbuf)
    result = Int32(-1)
    mark(lexerbuf, 2)
    state_id = _sedlex_decide_6(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_34, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_decide_6(c::Int32)
    if c <= 45
        return -1
    else
        if c <= 101
            return _sedlex_DT_table_4[c - 46] - 1
        else
            return -1
        end
    end
end
function _sedlex_rnd_33(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_14(lexerbuf)
    return result
end
function _sedlex_rnd_32(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_13(lexerbuf)
    return result
end
function _sedlex_rnd_31(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_9(lexerbuf)
    return result
end
function _sedlex_st_12(lexerbuf::lexbuf)
    result = Int32(-1)
    mark(lexerbuf, 1)
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_30, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_rnd_29(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_12(lexerbuf)
    return result
end
function _sedlex_st_11(lexerbuf::lexbuf)
    result = Int32(-1)
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_28, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_rnd_27(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_12(lexerbuf)
    return result
end
function _sedlex_st_10(lexerbuf::lexbuf)
    result = Int32(-1)
    mark(lexerbuf, 1)
    state_id = _sedlex_decide_5(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_26, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_decide_5(c::Int32)
    if c <= 47
        return -1
    else
        if c <= 101
            return _sedlex_DT_table_3[c - 48] - 1
        else
            return -1
        end
    end
end
function _sedlex_rnd_25(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_11(lexerbuf)
    return result
end
function _sedlex_rnd_24(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_10(lexerbuf)
    return result
end
function _sedlex_st_9(lexerbuf::lexbuf)
    result = Int32(-1)
    state_id = _sedlex_decide_4(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_23, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_decide_4(c::Int32)
    if c <= 47
        return -1
    else
        if c <= 57
            return 0
        else
            return -1
        end
    end
end
function _sedlex_rnd_22(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_10(lexerbuf)
    return result
end
function _sedlex_st_7(lexerbuf::lexbuf)
    result = Int32(-1)
    mark(lexerbuf, 4)
    state_id = _sedlex_decide_3(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_21, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_decide_3(c::Int32)
    if c <= 60
        return -1
    else
        if c <= 61
            return 0
        else
            return -1
        end
    end
end
function _sedlex_rnd_20(lexerbuf::lexbuf)
    result = Int32(-1)
    result = Int32(5)
    return result
end
function _sedlex_st_6(lexerbuf::lexbuf)
    result = Int32(-1)
    mark(lexerbuf, 3)
    state_id = _sedlex_decide_2(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_19, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_rnd_18(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_5(lexerbuf)
    return result
end
function _sedlex_rnd_17(lexerbuf::lexbuf)
    result = Int32(-1)
    result = Int32(3)
    return result
end
function _sedlex_rnd_16(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_3(lexerbuf)
    return result
end
function _sedlex_st_5(lexerbuf::lexbuf)
    result = Int32(-1)
    state_id = _sedlex_decide_2(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_15, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_rnd_14(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_5(lexerbuf)
    return result
end
function _sedlex_rnd_13(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_6(lexerbuf)
    return result
end
function _sedlex_rnd_12(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_3(lexerbuf)
    return result
end
function _sedlex_st_3(lexerbuf::lexbuf)
    result = Int32(-1)
    state_id = _sedlex_decide_2(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_11, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_decide_2(c::Int32)
    if c <= -1
        return -1
    else
        if c <= 92
            return _sedlex_DT_table_2[c - 0] - 1
        else
            return 0
        end
    end
end
function _sedlex_rnd_10(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_5(lexerbuf)
    return result
end
function _sedlex_rnd_9(lexerbuf::lexbuf)
    result = Int32(-1)
    result = Int32(3)
    return result
end
function _sedlex_rnd_8(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_3(lexerbuf)
    return result
end
function _sedlex_st_0(lexerbuf::lexbuf)
    result = Int32(-1)
    state_id = _sedlex_decide_1(public_next_int(lexerbuf))
    if state_id >= 0
        result = call_state(_sedlex_rnd_7, state_id, lexerbuf)
    else
        result = backtrack(lexerbuf)
    end
    return result
end
function _sedlex_decide_1(c::Int32)
    if c <= 57
        return _sedlex_DT_table_1[c - -1] - 1
    else
        return -1
    end
end
function _sedlex_rnd_6(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_13(lexerbuf)
    return result
end
function _sedlex_rnd_5(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_9(lexerbuf)
    return result
end
function _sedlex_rnd_4(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_7(lexerbuf)
    return result
end
function _sedlex_rnd_3(lexerbuf::lexbuf)
    result = Int32(-1)
    result = _sedlex_st_3(lexerbuf)
    return result
end
function _sedlex_rnd_2(lexerbuf::lexbuf)
    result = Int32(-1)
    result = Int32(0)
    return result
end
function _sedlex_rnd_1(lexerbuf::lexbuf)
    result = Int32(-1)
    result = Int32(6)
    return result
end
struct Token
    token_id::Int32
    lexeme::String
    line::Int32
    col::Int32
    span::Int32
    offset::Int32
    file::String
end
function lex(lexerbuf::lexbuf,  construct_token=Token)
    start(lexerbuf)
    case_id = _sedlex_st_0(lexerbuf)
        case_id < 0 && error("my error")
    token_id = _sedlex_rnd_39[case_id]
    token_id == nothing && return nothing
    return construct_token(token_id, lexeme(lexerbuf), lexerbuf.start_line, lexerbuf.pos - lexerbuf.curr_bol, lexerbuf.pos - lexerbuf.start_pos, lexerbuf.start_pos, lexerbuf.filename)
end
function lexall(buf::lexbuf, construct_token, is_eof #= Token -> Bool =#)
    Channel{Token}() do coro
        while true
            token = lex(buf, construct_token)
            token === nothing && continue
            is_eof(token) && break
            put!(coro, token)
        end
    end
end
const _sedlex_rnd_38 = (_sedlex_rnd_37,)
const _sedlex_rnd_36 = (_sedlex_rnd_35,)
const _sedlex_DT_table_4 = [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
const _sedlex_rnd_34 = (_sedlex_rnd_31, _sedlex_rnd_32, _sedlex_rnd_33,)
const _sedlex_rnd_30 = (_sedlex_rnd_29,)
const _sedlex_rnd_28 = (_sedlex_rnd_27,)
const _sedlex_DT_table_3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
const _sedlex_rnd_26 = (_sedlex_rnd_24, _sedlex_rnd_25,)
const _sedlex_rnd_23 = (_sedlex_rnd_22,)
const _sedlex_rnd_21 = (_sedlex_rnd_20,)
const _sedlex_rnd_19 = (_sedlex_rnd_16, _sedlex_rnd_17, _sedlex_rnd_18,)
const _sedlex_rnd_15 = (_sedlex_rnd_12, _sedlex_rnd_13, _sedlex_rnd_14,)
const _sedlex_DT_table_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
const _sedlex_rnd_11 = (_sedlex_rnd_8, _sedlex_rnd_9, _sedlex_rnd_10,)
const _sedlex_DT_table_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
const _sedlex_rnd_7 = (_sedlex_rnd_1, _sedlex_rnd_2, _sedlex_rnd_3, _sedlex_rnd_4, _sedlex_rnd_5, _sedlex_rnd_6,)
