open System

(* rightHeight * value * leftHeap * rightHeap *)
type 'a heap =
    | EmptyHeap
    | HeapNode of int * 'a * 'a heap * 'a heap

module Heap =
    let height = function
        | EmptyHeap -> 0
        | HeapNode(h, _, _, _) -> h

    let leftist v left right =
        if height left >= height right then HeapNode(height right + 1, v, left, right)
        else HeapNode(height left + 1, v, right, left)

    let rec merge compare = function
        | x, EmptyHeap -> x
        | EmptyHeap, y -> y
        | (HeapNode(_, x, l1, r1) as h1), (HeapNode(_, y, l2, r2) as h2) ->
            if compare x y <= 0 then leftist x l1 (merge compare (r1, h2))
            else leftist y l2 (merge compare (r2, h1))

    let hd = function
        | EmptyHeap -> failwith "Empty heap"
        | HeapNode(_, v, _, _) -> v

    let tl compare = function
        | EmptyHeap -> failwith "Empty heap"
        | HeapNode(_, _, l, r) -> merge compare (l, r)

    let rec to_seq compare = function
        | EmptyHeap -> Seq.empty
        | HeapNode(_, x, l, r) as node -> seq {yield x; yield! to_seq compare (tl compare node)}


type 'a LeftistHeap(comparer : 'a -> 'a -> int, inner : 'a heap) =
    (* private *)
    member this.inner = inner

    (* public *)
    member this.hd = Heap.hd inner
    member this.tl = LeftistHeap(comparer, Heap.tl comparer inner)
    member this.merge (other : LeftistHeap<_>) = LeftistHeap(comparer, Heap.merge comparer (inner, other.inner))
    member this.insert x = LeftistHeap(comparer, Heap.merge comparer (inner,(HeapNode(1, x, EmptyHeap, EmptyHeap))))

    interface System.Collections.Generic.IEnumerable<'a> with
        member this.GetEnumerator() = (Heap.to_seq comparer inner).GetEnumerator()

    interface System.Collections.IEnumerable with
        member this.GetEnumerator() = (Heap.to_seq comparer inner :> System.Collections.IEnumerable).GetEnumerator()

    static member make(comparer) = LeftistHeap<_>(comparer, EmptyHeap)

let compare a b = b - a

let findStrongest (h : LeftistHeap<int>) = h.hd

let strongestDie (h : LeftistHeap<int>) = h.tl

let recruit (h : LeftistHeap<int>) c =
    h.merge(LeftistHeap<int>(compare, HeapNode(1, c, EmptyHeap, EmptyHeap)))

let merge (h1 : LeftistHeap<int>) (h2 : LeftistHeap<int>) =
    h1.merge(h2)


[<EntryPoint>]
let main argv =
    let [|n; q|] = Console.ReadLine().Split([|' '|]) |> Array.map int
    let armies = [| for _ in 0 .. n -> LeftistHeap<int>.make(compare)|]
    for i in 1..q do
        let ops = Console.ReadLine().Trim().Split([|' '|])
        match ops with
        | [|"1"; i |] -> printfn "%d" (findStrongest armies.[i |> int])
        | [|"2"; i |] -> armies.[i |> int] <- strongestDie armies.[i |> int]
        | [|"3"; i; c |] -> armies.[i |> int] <- recruit armies.[i |> int] (c |> int)
        | [|"4"; i; j |] ->
            armies.[i |> int] <- merge armies.[i |> int] armies.[j |> int]
            armies.[j |> int] <- LeftistHeap<int>.make(compare)
        | _ -> failwith "unsupport operation"
    0