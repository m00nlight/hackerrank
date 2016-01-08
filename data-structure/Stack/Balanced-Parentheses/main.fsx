open System

let m = dict [(')', '('); (']', '['); ('}', '{')]

let rec solve xs stack =
    match xs with
    | [] -> if List.isEmpty stack then "YES" else "NO"
    | ch :: xs' -> if m.ContainsKey(ch) then
                        if List.isEmpty stack || List.head stack <> m.Item(ch) then
                            "NO"
                        else
                            solve xs' (List.tail stack)
                    else
                        solve xs' (ch :: stack)

[<EntryPoint>]
let main argv = 
    let n = int(System.Console.ReadLine())
    for _ in 1..n do
        let input = System.Console.ReadLine()
        (solve (List.ofSeq input) []) |> (printfn "%s")
    0