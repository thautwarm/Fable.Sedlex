module Main

open Fable.Sedlex

[<EntryPoint>]
let main _ =
    let cu = build([|(pstring "123",  Lexer_tokenize 2 )|], "error msg")
    let parse = compile_inline_thread cu
    let buf = from_ustring "123"
    printf "%A" <| parse buf
    0