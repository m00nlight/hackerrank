
primesTo :: Int -> [Int]
primesTo m = eratos [2..m] where
    eratos []     = []
    eratos (p:ps) = p : (eratos (filter (\x -> x `mod` p /= 0) ps))

primes = primesTo 1010 :: [Int]

isPrime :: Int -> Bool
isPrime n = isPrime' n primes
    where
      isPrime' 1 _      = False
      isPrime' 2 _      = True
      isPrime' n []     = True
      isPrime' n (p:ps) = if p * p > n then
                              True
                          else if n `mod` p == 0 then
                                   False
                               else isPrime' n ps

digitAccumulate :: (String -> String) -> String -> [Int]
digitAccumulate f ns = aux ns []
    where
      aux [] acc = acc
      aux ns acc = aux (f ns) ((read ns :: Int ):acc)


solve :: String -> String
solve digits =
    let n      = read digits :: Int
        left   = init $ digitAccumulate tail digits
        right  = tail $ reverse $ digitAccumulate init digits
    in if '0' `elem` digits || not (isPrime n) then
           "DEAD"
       else case ((all isPrime left), (all isPrime right)) of
              (True, True)  -> "CENTRAL"
              (True, False) -> "LEFT"
              (False, True) -> "RIGHT"
              (_, _)        -> "DEAD"


main = do
  _ <- getLine
  contents <- getContents
  mapM_ (putStrLn . solve) (lines contents)
