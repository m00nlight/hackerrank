open System.Numerics

let mmod = 1000000007L

let calcMobius upBound =
  let ret : int64 array = Array.zeroCreate (upBound + 1)
  Array.set ret 1 1L
  for i in 1..upBound do
    for j in (2 * i)..i.. upBound do
      Array.set ret j (ret.[j] - ret.[i])
  ret

let rec powMod (a : int64) (b : int64) (c : int64) =
  if b = 0L then 
    1L
  else
    let tmp = powMod a (b / 2L) c
    if b % 2L = 0L then 
      tmp * tmp % c
    else tmp * tmp % c * a % c

let calcFactMod upBound = 
  let ret : int64 array = Array.zeroCreate (upBound + 1)
  Array.set ret 0 1L
  for i in 1..upBound do
    Array.set ret i (ret.[i - 1] * (int64)(i) % mmod)
  ret
  
let mu = calcMobius 100010
let fact = calcFactMod 200010

let func n r = 
  let ret = fact.[n + r - 1]
  let ret = ret * powMod fact.[r] (mmod - 2L) mmod % mmod
  let ret = ret * powMod fact.[n - 1] (mmod - 2L) mmod % mmod
  ret
  
let _ = 
    let testCases = System.Int32.Parse(System.Console.ReadLine()) 
    for t in 1..testCases do
      let nk = System.Console.ReadLine().Trim().Split([|' '|]) 
               |> Seq.toList 
               |> List.map (fun x -> System.Int32.Parse(x))
      let n = nk.[0]
      let k = nk.[1]
      let ans = List.fold
                  (fun acc i -> 
                    (acc + mmod + (func (n / i) k) * mu.[i]) % mmod)
                  0L 
                  [1..n]
      printfn "%d" ans