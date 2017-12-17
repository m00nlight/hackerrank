open System

(* rightHeight * heapSize * value * leftHeap * rightHeap *)
type 'a heap =
    | EmptyHeap
    | HeapNode of int * int * 'a * 'a heap * 'a heap

module Heap =
    let height = function
        | EmptyHeap -> 0
        | HeapNode(h, _, _, _, _) -> h

    let size = function
        | EmptyHeap -> 0
        | HeapNode(_, s, _, _, _) -> s

    let leftist v left right =
        if height left >= height right then HeapNode(height right + 1, size left + size right + 1, v, left, right)
        else HeapNode(height left + 1, size left + size right + 1, v, right, left)

    let rec merge compare = function
        | x, EmptyHeap -> x
        | EmptyHeap, y -> y
        | (HeapNode(_, s1, x, l1, r1) as h1), (HeapNode(_, s2, y, l2, r2) as h2) ->
            if compare x y <= 0 then leftist x l1 (merge compare (r1, h2))
            else leftist y l2 (merge compare (r2, h1))

    let hd = function
        | EmptyHeap -> failwith "Empty heap"
        | HeapNode(_, _, v, _, _) -> v

    let tl compare = function
        | EmptyHeap -> failwith "Empty heap"
        | HeapNode(_, _, _, l, r) -> merge compare (l, r)

    let rec to_seq compare = function
        | EmptyHeap -> Seq.empty
        | HeapNode(_, _, x, l, r) as node -> seq {yield x; yield! to_seq compare (tl compare node)}


type 'a LeftistHeap(comparer : 'a -> 'a -> int, inner : 'a heap) =
    (* private *)
    member this.inner = inner

    (* public *)
    member this.size = Heap.size inner
    member this.hd = Heap.hd inner
    member this.tl = LeftistHeap(comparer, Heap.tl comparer inner)
    member this.merge (other : LeftistHeap<_>) = LeftistHeap(comparer, Heap.merge comparer (inner, other.inner))
    member this.insert x = LeftistHeap(comparer, Heap.merge comparer (inner,(HeapNode(1, 1, x, EmptyHeap, EmptyHeap))))

    interface System.Collections.Generic.IEnumerable<'a> with
        member this.GetEnumerator() = (Heap.to_seq comparer inner).GetEnumerator()

    interface System.Collections.IEnumerable with
        member this.GetEnumerator() = (Heap.to_seq comparer inner :> System.Collections.IEnumerable).GetEnumerator()

    static member make(comparer) = LeftistHeap<_>(comparer, EmptyHeap)


type 'a State = 'a LeftistHeap * 'a LeftistHeap

let insert v ((s1, s2) as state : 'a State) =
    if s1.size = 0 && s2.size = 0 then
        (s1.insert v, s2)
    else
        match s1.size > s2.size with
        | true -> match v > s1.hd with
                  | true -> (s1, s2.insert v)
                  | _ -> (s1.tl.insert(v), s2.insert(s1.hd))
        | false -> match v <= s2.hd with
                   | true -> (s1.insert(v), s2)
                   | _ -> (s1.insert(s2.hd), s2.tl.insert(v))

let getRunningMedian ((s1, _) as state : 'a State) = s1.hd


[<EntryPoint>]
let main argv =
    let state0 = (LeftistHeap<_>.make(fun x y -> y - x), LeftistHeap<_>.make(-) )
    let n = Console.ReadLine() |> int
    let tracking = [| for i in 0 .. n -> None |]
    tracking.[0] <- Some(state0)
    for i in 1 .. n do
        let v = Console.ReadLine() |> int
        if v > 0 then
            tracking.[i] <- Some(insert v  (Option.get tracking.[i - 1]))
        else
            tracking.[i] <- tracking.[i + v]  

    for i in 1 .. n do
        printfn "%d" (getRunningMedian (Option.get tracking.[i]))
    0

