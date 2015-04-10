import qualified Data.List as L
import Control.Applicative

solve :: [Int] -> [Int] -> Int -> Int -> Int
solve as hs n m = aux 0 n
    -- in fact, an upper bound problem binary search answer
    -- problem
    where aux l r
              | l > r = r
              | otherwise =
                  let mid = (l + r) `div` 2
                      tmp = sum $ take mid
                            (L.sort (map (\(x, y) -> x + (mid -1) * y)
                                             (zip as hs)))
                  in if tmp > m then aux l (mid - 1)
                     else aux (mid + 1) r

main = do
  [n,m] <- map (read :: String -> Int) . words <$> getLine
  as <- map (read :: String -> Int) . words <$> getLine
  hs <- map (read :: String -> Int) . words <$> getLine
  print $ solve as hs n m
