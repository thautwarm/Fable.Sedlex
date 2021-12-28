module Main

open Fable.Sedlex.Compiler
open Fable.CodeGen
[<EntryPoint>]
let main _ =
    let cu = build([|(pstring "123",  Lexer_tokenize 2 )|], "error msg")
    let parse = compile_inline_thread cu
    let buf = from_ustring "123"
    printfn "%A" <| parse buf
    
    let doc = 
        word "class" + vsep [
            word "def";
            vsep [
                word "123"
                word "var" + word "x" + word "=" + word "z" * word ";"
            ] >>> 3
        ] >>> 2

    printfn "%s" (showDoc doc)
    0
