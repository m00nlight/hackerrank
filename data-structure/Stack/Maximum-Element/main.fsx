open System

let rec solve xs stack ans =
    match xs with
    | (1, num) :: xs' -> solve xs' ((num, max num (snd (List.head stack)))::stack) ans
    | (2, _) :: xs' -> solve xs' (List.tail stack) ans
    | (3, _) :: xs' -> solve xs' stack ((stack |> List.head |> snd)::ans)
    | _ -> List.rev ans


let transform (line : string) = 
    line.Split [|' '|] 
    |> Seq.map int 
    |> List.ofSeq
    |> (fun xs -> match xs with
                  | op :: [] -> (op, -1)
                  | op :: num :: [] -> (op, num)
                  | _ -> raise(Exception("transform")))

[<EntryPoint>]
let main argv = 
    let _ = int(System.Console.ReadLine())
    let input = Seq.initInfinite (fun _ -> System.Console.ReadLine())
                |> Seq.takeWhile (fun line -> line <> null)
                |> Seq.map transform
                |> List.ofSeq
    let result = solve input [(-1, -1)] []
    result |> Seq.iter (printfn "%d")
    0