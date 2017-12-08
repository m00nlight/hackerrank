open System

type 'a path = 
    | Top
    | PathNode of ('a path list) * ('a path)  * ('a path list) * 'a * ('a path list)

let goLeft p = 
    match p with
    | PathNode([], _, _, _, _) -> failwith "left of leftmost element"
    | PathNode((PathNode(_, _, _, value, sons) as l) :: ls, up, rs, _, _) -> 
        PathNode(ls, up, p :: rs, value, sons)
    | _ -> failwith "should not happen"


let goRight p = 
    match p with
    | PathNode(_, _, [], _, _) -> failwith "right of rightimost element"
    | PathNode(ls, up, (PathNode(_, _, _, value, sons) as r) :: rs, _, _) -> 
        PathNode( p :: ls, up, rs, value, sons)
    | _ -> failwith "this should not happen"


let goUp p = 
    match p with 
    | Top -> failwith "up of top element"
    | PathNode(left, up, right, _, _) -> 
        match up with
        | Top -> failwith "up with top"
        | PathNode(left', up', right', value, _) -> 
            PathNode(left', up', right', value, (List.rev left) @ (p :: right))


let goDown p = 
    match p with
    | Top -> failwith "go down of top node"
    | PathNode(_, _, _, _, []) -> failwith "no son of current node"
    | PathNode(_, _, _, _, (PathNode(_, _, _, value, sons) as s) :: ss) -> 
        PathNode([], p, ss, value,  sons)
    | _ -> failwith "should not happen"
                               
let rec nth p = function
    | 1 -> goDown p
    | n when n > 0 -> goRight (nth p (n - 1))
    | _ -> failwith "n must be greater or equal to zero"


let changeValue p newValue = 
    match p with
    | Top -> failwith "change value of top node"
    | PathNode(left, up, right, _, sons) -> PathNode(left, up, right, newValue, sons)

let makeNode parent value = PathNode([], parent, [], value, [])

let insertRight p newValue = 
    match p with
    | Top -> failwith "insert right of top"
    | PathNode(left, up, right, curValue, sons) -> 
        PathNode(left, up, (makeNode p newValue) :: right, curValue, sons)

let insertLeft p newValue = 
    match p with 
    | Top -> failwith "insert left of top"
    | PathNode(left, up, right, curValue, sons) -> 
        PathNode((makeNode p newValue) :: left, up,  right, curValue, sons)

let insertDown p newValue = 
    match p with
    | Top -> failwith "insert down of top node"
    | PathNode(left, up, right, curValue, sons) -> 
        PathNode(left, up, right, curValue, (makeNode p newValue) :: sons)

let delete p = 
    match p with
    | Top -> failwith "delete of path top"
    | PathNode(left, up, right, _, _) -> 
        match up with
        | Top -> failwith "delete the root node"
        | PathNode(left', up', right', curValue, _) -> 
            PathNode(left', up', right', curValue, (List.rev left) @ right)

let getCurrentValue p =
    match p with 
    | Top -> failwith "get value of top node"
    | PathNode(_, _, _, value, _) -> value

let doOp op p = 
    match op with
    | [|"change"; value |] -> (None, changeValue p (value |> int))
    | [|"print" |] -> (Some(getCurrentValue p), p)
    | [|"visit"; "left"|] -> (None, goLeft p)
    | [|"visit"; "right"|] -> (None, goRight p)
    | [|"visit"; "parent"|] -> (None, goUp p)
    | [|"visit"; "child"; n|] -> (None, nth p (n |> int))
    | [|"insert"; "left"; x|] -> (None, insertLeft p (x |> int))
    | [|"insert"; "right"; x|] -> (None, insertRight p (x |> int))
    | [|"insert"; "child"; x|] -> (None, insertDown p (x |> int))
    | [|"delete" |] -> (None, delete p)
    | _ -> failwith "unsupported operation"

let solve ops = 
    let p = PathNode([], Top, [], 0, [])
    let (ans, _) = List.fold (fun (acc, loc) op ->
                                match doOp op loc with
                                | (None, nloc) -> (acc, nloc)
                                | (Some v, nloc) -> (v :: acc, nloc))
                        ([], p) ops
    List.rev ans

[<EntryPoint>]
let main argv = 
    let n = Console.ReadLine() |> int 
    let read _ = Console.ReadLine().Trim()
    let ops = Seq.init n read 
              |> Seq.toList
              |> List.map (fun (x : string) -> x.Split([|' '|]))
    let ans = solve ops
    for a in ans do
        printfn "%d" a
    //Console.Read()
    0 // return an integer exit code
