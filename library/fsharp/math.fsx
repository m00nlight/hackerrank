open System.Numerics
open System
open System.Collections

exception InnerError of string
exception OuterError of string

let rec gcd (a : int64) (b : int64) = 
    if b = 0L then abs a
    else gcd b (a % b)
    
let rec lcm (a : int64) (b : int64) = 
    a * b / gcd a b


let rec powMod (a : int64) (b : int64) (c : int64) (acc : int64) =
    if b = 0L then acc
    elif b % 2L = 0L then
        powMod (a * a % c) (b / 2L) c acc
    else powMod (a * a % c) (b / 2L) c (a * acc % c)
    

let rec exGcd (a : int64) (b : int64) = 
    if b = 0L then
        (a, 1L, 0L)
    else
        let (g, x, y) = exGcd b (a % b)
        (g, y, x - (a / b) * y)
        
let modInv (a : int64) (m : int64) = 
    if gcd a m <> 1L then
        raise (InnerError("Not coprime"))
    else
        let (_, x, y) = exGcd a m
        (m + x % m) % m
        
    

let calcMobius upBound =
    let ret : int64 array = Array.zeroCreate (upBound + 1)
    Array.set ret 1 1L
    for i in 1..upBound do
        for j in (2 * i)..i.. upBound do
            Array.set ret j (ret.[j] - ret.[i])
    ret
    

/// sieve of primes
let primesTo n = 
    let isPrime = new BitArray(n + 1, true)
    let last = Math.Sqrt(float n) |> int

    isPrime.[0] <- false
    isPrime.[1] <- false
    for p in 4 .. 2 .. n do 
        isPrime.[p] <- false
    for p in 3 .. 2 .. last + 1 do
        if isPrime.[p] then
            for pm in p * p .. p .. n do
                isPrime.[pm] <- false
    seq {for i in 2 .. n do if isPrime.[i] then yield i}



let _ = 
    printfn "%A" (exGcd 3L 12L)
    printfn "%A" (exGcd 4L 6L)
    printfn "%A" (exGcd 2L 3L)
    printfn "%A" (modInv 2L 3L)
    (*printfn "%A" (modInv 4L 6L)*) 
