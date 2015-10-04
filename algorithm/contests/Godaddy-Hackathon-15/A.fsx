let solve n d =
  n - (n / 2 - d)
  
let _ = 
  let nd = System.Console.ReadLine().Trim().Split([|' '|])
  let n = System.Int32.Parse(nd.[0])
  let d = System.Int32.Parse(nd.[1])
  printfn "%d" (solve n d)