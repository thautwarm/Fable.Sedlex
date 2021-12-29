module Bug

type Test(l: int, r: int) =
    let mutable f = 0

    let call() =
        f <- l
        r

    member __.Run() =
        let x = call()
        f + x
    
let test() =
    printfn "%d" <| Test(1, 2).Run()


