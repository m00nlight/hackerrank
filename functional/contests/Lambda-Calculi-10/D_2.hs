{-|
  Using Persistent Segment Tree to solve the median query problem. In fact,
  this methods benefit from the persistent datastructure of functional
  languages to achieve time and space complexity.
  Time complexity : O(N logN + Q logN)
  Space complexity: O(N logN) since the structure in functional language
  are persistent(in other words, they share unchanged memory if they can)
  This method is a around 2 times faster than the partition tree version.
 -}
import           Control.Applicative
import           Data.List
import qualified Data.List           as L
import qualified Data.Vector         as V
import           Text.Printf

-- data Tree = Node Int Int Int Tree Tree
--           | Leaf Int Int deriving (Show)

data Tree =
    Node { startVal :: Int    -- start value of array in segment tree
         , endVal   :: Int    -- end value of array in segment tree
         , cc       :: Int    -- count how many values in range
         , left     :: Tree   -- left sub tree
         , right    :: Tree   -- right sub tree
         } |
    Leaf { val :: Int           --
         , cc  :: Int
         } deriving (Show)



initTree :: V.Vector Int -> Tree
initTree vs = build 0 (n - 1)
  where
  n = V.length vs
  build a b
    | a == b    = Leaf (vs V.! a) 0
    | otherwise = Node (vs V.! a) (vs V.! b) 0 lt rt
      where
        mid = (a + b) `div` 2
        lt = build a mid
        rt = build (mid + 1) b

insertNum :: Tree -> Int -> Tree
insertNum tree x = inner tree
  where
  inner leaf@(Leaf a cc) = if a == x then Leaf x (cc + 1) else leaf
  inner node@(Node a b cc lt rt)
    | a <= x && x <= b  = Node a b (cc + 1) (inner lt) (inner rt)
    | otherwise         = node


buildTrees :: [Int] -> Tree -> V.Vector Tree
buildTrees xs initval =
    V.fromList $! reverse $
     L.foldl' (\ acc@(t:_) x -> (insertNum t x):acc) [initval] xs



queryKth :: Tree -> Tree -> Tree -> Tree -> Int -> Double
queryKth (Leaf x _) _ _ _ _ = fromIntegral x
queryKth (Node _ _ _ ly ry) (Node _ _ _ lx rx)
         (Node _ _ _ lw rw) (Node _ _ _ lz rz) k =
  if k <= th
    then queryKth ly lx lw lz k
    else queryKth ry rx rw rz $! k - th
      where
      th = getCC ly - getCC lx + getCC lw - getCC lz
      getCC (Leaf _ cc) = cc
      getCC (Node _ _ cc _ _) = cc

solveQuery :: V.Vector Tree -> V.Vector Tree -> [[Int]] -> IO ()
solveQuery ts1 ts2 qs = innerSolve qs
  where
  innerSolve :: [[Int]] -> IO ()
  innerSolve []             = return ()
  innerSolve ([x,y,z,w]:qs) = do
    let n   = y - x + w - z + 2
        m   = (n + 1) `div` 2
        qk  = queryKth (ts1 V.! y) (ts1 V.! (x - 1))
                       (ts2 V.! w) (ts2 V.! (z - 1))
        r1  = qk m
        r2  = if n `mod` 2 == 1 then r1 else qk (m + 1)
    printf "%.1f\n" $! (r1 + r2) / 2.0
    innerSolve qs

main = do
  contents <- lines <$> getContents
  let xs  = map read . words $! contents !! 1
      ys  = map read . words $! contents !! 2
      vs  = V.fromList $! map head $! group $! sort $! xs ++ ys
      it  = initTree vs
      ts1 = buildTrees xs it
      ts2 = buildTrees ys it
      qs  = map (map read . words) $! drop 4 contents
  solveQuery ts1 ts2 qs
