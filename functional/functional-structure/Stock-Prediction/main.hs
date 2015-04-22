{-# LANGUAGE BangPatterns        #-}
{-# LANGUAGE ScopedTypeVariables #-}

import           Control.Applicative
import           Control.Monad
import           Data.Vector.Generic ((!))
import qualified Data.Vector.Unboxed as U

data SegTree = SegTree
    { start  :: !Int
    , end    :: !Int
    , minMax :: !(Int, Int)
    , left   :: SegTree
    , right  :: SegTree
    } | Leaf deriving (Show)

merge :: (Int, Int) -> (Int, Int) -> (Int, Int)
merge (a, b) (c, d) = (min a c, max b d)

build :: [Int] -> SegTree
build as = go 0 (length as) as where
  go l r as
    | r - l == 1 =
      SegTree l r (head as, head as) Leaf Leaf
    | otherwise =
      let m        = (l + r) `div` 2
          (ls, rs) = splitAt (m - l) as
          cl       = go l m ls
          cr       = go m r rs
      in SegTree l r (merge (minMax cl) (minMax cr)) cl cr

query :: Int -> Int -> SegTree -> (Int, Int)
query s e st = go st where
  go st@(SegTree l r val cl cr)
    | s <= l && r <= e = val
    | e <= l           = (10^9, -10^9)
    | s >= r           = (10^9, -10^9)
    | otherwise        = merge (go cl) (go cr)

f :: Int -> Int -> Int -> (Int, Int) -> SegTree -> Int
f l h d (mi, ma) st
    | h - l <= 1 = l
    | otherwise =
      let m = (l + h) `div` 2
          (a, b) = query d (m + 1) st
      in if a >= mi && b <= ma then
             f m h d (mi, ma) st
         else f l m d (mi, ma) st

g :: Int -> Int -> Int -> (Int, Int) -> SegTree -> Int
g l h d (mi, ma) st
    | h - l <= 1 = h
    | otherwise =
        let m = (l + h) `div` 2
            (a, b) = query m (d + 1) st
        in if a >= mi && b <= ma then
               g l m d (mi, ma) st
           else g m h d (mi, ma) st

main :: IO ()
main = do
  n  <- readLn
  as <- map read . words <$> getLine
  q  <- readLn
  qs <- replicateM q readInts

  let !st = build as
      !v  = U.fromList as
  forM_ qs $ \[d, m] -> do
         let mi = v ! d
             ma = mi + m
             hi = f d n d (mi, ma) st
             lo = g (-1) d d (mi, ma) st
         print (hi - lo + 1)
  where readInts = return . map (read :: String -> Int) . words =<< getLine
