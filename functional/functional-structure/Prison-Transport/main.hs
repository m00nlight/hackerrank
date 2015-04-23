import qualified Data.Map as M
import Control.Monad
import Data.List (foldl', group, sort)

type UnionFind = M.Map Int Int

-- |The 'path' function return root and path to the root as a pair
path :: UnionFind -> Int -> (Int, [Int])
path ufset a = aux a []
    where aux idx acc
              | idx == ufset M.! idx = (idx, acc)
              | otherwise = aux (ufset M.! idx) (idx:acc)

-- |The 'union' function union two node and do path compression
union :: UnionFind -> Int -> Int -> UnionFind
union ufset a b = M.insert fa fb ufset'
    where (fa, ps) = path ufset a
          (fb, _ ) = path ufset b
          ufset' = foldl' (\acc x -> M.insert x fa acc) ufset ps


solve :: Integral a => Int -> [(Int, Int)] -> a
solve n qs = sum $ map (\x -> ceiling (sqrt (fromIntegral x))) res
    where ufset = M.fromList $ zip [1..n] [1..n]
          ufset' = foldl' (\ acc (x, y) -> union acc x y) ufset qs
          tmp = group . sort $ map (\x -> fst $ path ufset' x) [1..n]
          res = map length tmp


main :: IO ()
main = do
  n <- readLn :: IO Int
  q <- readLn :: IO Int
  c <- replicateM q $ do (a:b:_) <- readLnInts
                         return (a,b)
  print $ solve n c
      where readLnInts = liftM (map (read::String->Int) . words) getLine
