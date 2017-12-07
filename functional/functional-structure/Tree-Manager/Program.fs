open System

type 'a tree = TreeNode of 'a * ('a tree list)

(* 
 A path is either a Top or a node of it's left sibling list in reverse order
 its parent path, and its right sibling list.
*)
type 'a path = 
    | Top
    | PathNode of ('a tree list) * ('a path) * ('a tree list) * 'a

type 'a location = Loc of ('a tree) * ('a path)


let goLeft (Loc(t, p)) = 
    match p with
    | Top -> failwith "left of top"
    | PathNode((TreeNode(value, _) as l):: left, up, right, _) -> Loc(l, PathNode(left, up, t :: right, value))
    | PathNode([], _, _, _) -> failwith "left of the first"


let goRight (Loc(t, p)) = 
    match p with
    | Top -> failwith "right of top"
    | PathNode(left, up, (TreeNode(value, _) as r) :: right, _) -> Loc(r, PathNode(t :: left, up, right, value))
    | PathNode(_, _, [], _) -> failwith "right of the last"


let goUp (Loc(t, p)) = 
    match p with 
    | Top -> failwith "up of top"
    | PathNode(left, up, right, _) -> 
        match up with
        | Top -> failwith "up with top"
        | PathNode(_, _, _, value) -> Loc(TreeNode(value, (List.rev left) @ [t] @ right), up)


let goDown (Loc(t, p)) = 
    match t with
    | TreeNode(_, (TreeNode(value, _) as t') :: ts) -> Loc(t', PathNode([], p, ts, value))
    | TreeNode(_, []) -> failwith "empty children to go down"
                               
let rec nth loc = function
    | 1 -> goDown loc
    | n when n > 0 -> goRight (nth loc (n - 1))
    | _ -> failwith "n must be greater or equal to zero"


let changeValue (Loc(TreeNode(_, cs), p)) newValue = 
    match p with
    | Top -> failwith "change value of top node"
    | PathNode(left, up, right, _) -> Loc(TreeNode(newValue, cs), PathNode(left, up, right, newValue))

let insertRight (Loc(t, p)) newValue = 
    match p with
    | Top -> failwith "insert right of top"
    | PathNode(left, up, right, curValue) -> Loc(t, PathNode(left, up, TreeNode(newValue, []) :: right, curValue))

let insertLeft (Loc(t, p)) newValue = 
    match p with 
    | Top -> failwith "insert left of top"
    | PathNode(left, up, right, curValue) -> Loc(t, PathNode(TreeNode(newValue, []) :: left, up, right, curValue))

let insertDown (Loc(TreeNode(curValue, sons), p)) newValue = 
    Loc(TreeNode(curValue, TreeNode(newValue, []) :: sons), p)

let delete (Loc(t, p)) = 
    match p with
    | Top -> failwith "delete of path top"
    | PathNode(left, up, right, _) -> 
        match up with
        | Top -> failwith "delete the root node"
        | PathNode(_, _, _, curValue) -> Loc(TreeNode(curValue, (List.rev left) @ right), up)

let getCurrentValue (Loc(t, p)) =
    match t with 
    | TreeNode(currValue, _) -> currValue

let doOp op loc = 
    match op with
    | [|"change"; value |] -> (None, changeValue loc (value |> int))
    | [|"print" |] -> (Some(getCurrentValue loc), loc)
    | [|"visit"; "left"|] -> (None, goLeft loc)
    | [|"visit"; "right"|] -> (None, goRight loc)
    | [|"visit"; "parent"|] -> (None, goUp loc)
    | [|"visit"; "child"; n|] -> (None, nth loc (n |> int))
    | [|"insert"; "left"; x|] -> (None, insertLeft loc (x |> int))
    | [|"insert"; "right"; x|] -> (None, insertRight loc (x |> int))
    | [|"insert"; "child"; x|] -> (None, insertDown loc (x |> int))
    | [|"delete" |] -> (None, delete loc)
    | _ -> failwith "unsupported operation"

let solve ops = 
    let tree = TreeNode(0, [])
    let loc = Loc(tree, PathNode([], Top, [], 0))
    let (ans, _) = List.fold (fun (acc, loc) op ->
                                match doOp op loc with
                                | (None, nloc) -> (acc, nloc)
                                | (Some v, nloc) -> (v :: acc, nloc))
                        ([], loc) ops
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
