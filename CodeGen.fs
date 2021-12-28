module Fable.CodeGen

open System.Text

module A =
    let x =1




type Doc =
| Concat of Doc * Doc
| VSep of Doc list
| Align of Doc
| Indent of int * Doc
| Word of string
     
     static member ( * ) (a, b) = Concat(a, b)
     static member (+) (a, b) = a * Word " " * b

     static member (<<<) (a, b) = Indent(-b, a)
     static member (>>>) (a, b) = Indent(b, a)




type DocPrimitive =
| DP_PopIndent
| DP_PushCurrentIndent
| DP_PushIndent of int
| DP_Word of string


module Array =
    let drop (i: int) arr =
        Array.take (Array.length arr - i) arr

let rec compileToPrims : Doc -> DocPrimitive array array = fun doc ->
    match doc with
    | Concat(l ,r) ->
        let l = compileToPrims l
        let r = compileToPrims r
        if Array.isEmpty l then r
        elif Array.isEmpty r then l
        else
        Array.concat [|
            Array.drop 1 l;
            [| Array.append (Array.last l) (Array.head r) |]
            Array.skip 1 r
            |]
    | Align(seg) ->
        let it = compileToPrims seg
        if Array.isEmpty it then it
        else
        it.[0] <- Array.append [|DP_PushCurrentIndent|] it.[0]
        it.[it.Length - 1] <- [| DP_PopIndent |]
        it
    | Indent(i, doc) ->
        let prefix = [|DP_PushIndent i|]
        let it = compileToPrims doc
        if Array.isEmpty it then it
        else
        it.[0] <- Array.append prefix it.[0]
        it.[it.Length - 1] <- Array.append it.[it.Length - 1] [|DP_PopIndent|]
        it
    | VSep(segs) ->
        Array.concat <| Seq.map compileToPrims segs
    | Word s -> [|[|DP_Word s|]|]

type Stack<'a>(?init: 'a seq) =
    let mutable _content =
        match init with
        | None -> []
        | Some xs -> Seq.toList xs 
    
    member __.Push a =
        _content <- a :: _content 

    member __.Pop() =
        match _content  with
        | hd::tl ->
            _content <- tl; hd
        | _ -> raise <| System.IndexOutOfRangeException("negative stacksize")
    
    member __.Last =
        match _content  with
        | hd::_ -> hd
        | _ -> raise <| System.IndexOutOfRangeException("negative stacksize")
    



let render(setences: DocPrimitive array array) (write: string -> unit) =
    let levels = Stack<int>([0])
    if Array.isEmpty setences then
        ()
    else
    for words in setences do
        let mutable col = 0
        let mutable initialized = false
        
        let line_init() =
            if not initialized then
                col <- levels.Last + col
                write(String.replicate col " ")
                initialized <- true
        for word in words do
            match word with
            | DP_Word s ->
                line_init()
                write(s)
                col <- col + s.Length
            | DP_PushCurrentIndent ->
                levels.Push(col)
            | DP_PopIndent ->
                ignore (levels.Pop())
            | DP_PushIndent i ->
                levels.Push(levels.Last + i)
        write("\n")
    

let word s = Word s
let vsep lines = VSep lines
let align seg = Align seg
let indent i x = Indent(i, x)
let concat a b = Concat(a, b)

let showDoc (doc: Doc) =
    let sb = new StringBuilder()
    render (compileToPrims doc) (fun x -> ignore(sb.Append(x)))
    sb.ToString()