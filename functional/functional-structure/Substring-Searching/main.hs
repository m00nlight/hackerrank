-- | KMP algorithm in haskell
import Data.List.Split


data KMP a = KMP { done :: Bool
                 , next :: (a -> KMP a)
                 }

makeTable :: Eq a => [a] -> KMP a
makeTable xs = table
   where table = makeTable' xs (const table)

makeTable' []     failure = KMP True failure
makeTable' (x:xs) failure = KMP False test
   where  test  c = if c == x then succ else failure c
          succ = makeTable' xs (next (failure x))

-- | 'kmp' take two Eq list in and produce an boolean result, 
--   indicate whehter the first list is a sublist of the second
kmp :: Eq a => [a] -> [a] -> Bool
kmp pattern text = match (makeTable pattern) text
    where
      match state [] = if done state then True else False
      match state (x:xs) = if done state then
                               True
                           else match ((next state) x) xs

main = do
  _ <- getLine
  contents <- getContents
  mapM_ (\ [x, y] -> if kmp y x then putStrLn "YES" else putStrLn "NO")
        (chunksOf 2 (words contents))
