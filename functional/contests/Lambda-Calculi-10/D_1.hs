{-|
  Using Partition tree to solve the median query problem. Build partition
  tree of the two sequence, then find largest i such that X_i <= Y_j, and
  i + j = k. We can use binary search (upper bound) to do the search for
  value of i.
  Time complexity : O(N logN + Q logN logN), where N is the maximum size
  of the input sequence, and Q is the number of query.
 -}

import           Control.Applicative
import qualified Data.List           as L
import qualified Data.Vector         as V
import           Text.Printf

data Tree = Tree (V.Vector Int) Tree Tree
          | Leaf Int deriving (Show)

type Struct = (Tree, V.Vector Int)

-- |The 'buildTree' build the partition tree of the sequence
buildTree :: [Int] -> Tree
buildTree xs = aux 0 (n - 1) xs
    where
      vs = V.fromList . L.sort $! xs
      n = V.length vs
      toleft pivot ns = tail. reverse $ L.foldl'
                        (\ acc x -> if x <= pivot then (head acc + 1):acc
                                    else (head acc):acc) [0] ns
      aux a b ns
          | a == b = Leaf a
          | otherwise = Tree toLeft left right
          where mid = (a + b) `div` 2
                pivot = vs V.! mid
                toLeft = V.fromList $! toleft pivot ns
                left = aux a mid ls
                right = aux (mid + 1) b rs
                (ls, rs) = L.partition (<= pivot) ns

buildStruct :: [Int] -> Struct
buildStruct xs = (buildTree xs, V.fromList . L.sort $! xs)

-- |The 'queryRangeKth' function return the kth smallest elements in an range
queryRangeKth :: Struct -> Int -> Int -> Int -> Int
queryRangeKth (tree, vs) x y k = query tree x y k
    where
      query (Leaf a) _ _ _ = vs V.! a
      query (Tree toLeft left right) x y k
          | ly - lx < k = query right (x - lx) (y - ly) (k - (ly - lx))
          | otherwise = query left lx (ly - 1) k
          where lx = if x > 0 then toLeft V.! (x - 1) else 0
                ly = toLeft V.! y

inf = 2 * 10 ^9 :: Int

queryMedian :: Struct -> Struct -> Int -> Int -> Int -> Int -> Double
queryMedian s1 s2 x y z w = fromIntegral (r1 + r2) / 2.0
    where
      total = (y - x + w - z + 2)
      p = (total + 1) `div` 2
      getKth s x y k
          | k == 0 = 0
          | k > y - x + 1 = inf
          | otherwise = queryRangeKth s x y k
      i = binaryS 0 (min (y - x + 2) (p + 1))
      j = p - i
      -- | invariaient l = True, and r = False
      binaryS l r = if l + 1 == r then l
                    else if getKth s1 x y mid <= getKth s2 z w (p - mid + 1)
                         then binaryS mid r else binaryS l mid
                             where mid = (l + r) `div` 2
      r1 = max (getKth s1 x y i) (getKth s2 z w j)
      r2 = if total `mod` 2 == 1 then r1
           else min (getKth s1 x y (i + 1)) (getKth s2 z w (j + 1))


solveQuery :: Struct -> Struct -> [[Int]] -> IO ()
solveQuery s1 s2 qs = aux qs
    where
      aux :: [[Int]] -> IO ()
      aux [] = return ()
      aux ([x, y, z, w]:qs) = do
        printf "%.1f\n" $! queryMedian s1 s2 (x - 1) (y - 1) (z - 1) (w - 1)
        aux qs

main :: IO ()
main = do
  _ <- getLine
  xs <- map read . words <$> getLine
  ys <- map read . words <$> getLine
  _ <- getLine
  qs <- map (map read . words) . lines <$> getContents
  let s1 = buildStruct xs
      s2 = buildStruct ys
  solveQuery s1 s2 qs
