import qualified Data.Vector as V
import qualified Data.List as L


accSum :: Num t => [t] -> [t]
accSum xs = aux xs 0
    where aux [] a = []
          aux (x:xs') a = (a + x) : aux xs' (a + x)

lowerBound :: (Num a, Ord a) => V.Vector a -> a -> Int
lowerBound vec target = aux 0 ((V.length vec) - 1)
    where
      aux l r = if l > r then l
                else let mid = (l + r) `div` 2
                     in if vec V.! mid >= target then
                            aux l (mid - 1)
                        else aux (mid + 1) r

upperBound :: (Num a, Ord a) => V.Vector a -> a -> Int
upperBound vec target = aux 0 ((V.length vec) - 1)
    where
      aux l r = if l > r then l
                else let mid = (l + r) `div` 2
                     in if vec V.! mid > target then
                            aux l (mid - 1)
                        else aux (mid + 1) r


solve :: (Num a, Ord a) => [a] -> [a] -> [Int]
solve xs queries =
    let vec = V.fromList $ accSum $ reverse (L.sort xs)
        f x = if x <= V.length vec then x else -1
    in map (\x -> f $ lowerBound vec x + 1) queries


main = do
  _ <- getLine
  arr <- getLine
  _ <- getLine
  queries <- getContents
  let xs = map (read :: String -> Int) (words arr)
      qs = map (read :: String -> Int) (lines queries)
  mapM_ (putStrLn . show) $ solve xs qs
