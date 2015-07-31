import           Control.Applicative
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe

type UnionFind = M.Map Int Int

initUnionFindSet :: Int -> UnionFind
initUnionFindSet n =
    M.fromList [(i, i) | i <- [0..(n - 1)]]

find :: UnionFind -> Int -> (Int, UnionFind)
find ufset node = (root, ufset')
    where
      root = until (\ x -> M.findWithDefault (-1) x ufset == x)
             (\ x -> M.findWithDefault (-1) x ufset) node
      path = getPath ufset node
      ufset' = compressPath ufset root path

addToMap :: Ord k => M.Map k a -> [(k, a)] -> M.Map k a
addToMap m xs = L.foldl' (\ acc (x, d) -> M.insert x d acc) m xs

getPath :: UnionFind -> Int -> [Int]
getPath ufset node = until (\ (x:_) -> M.findWithDefault (-1) x ufset == x)
                     (\ xs -> (M.findWithDefault (-1) (head xs) ufset) : xs)
                     [node]

compressPath :: UnionFind
             -> Int             -- ^ root
             -> [Int]           -- ^ nodes on the path
             -> UnionFind
compressPath ufset root xs =
    addToMap ufset (map (\ x -> (x, root)) xs)

union :: UnionFind -> Int -> Int -> UnionFind
union ufset x y = if fx == fy then ufset'' else M.insert fx fy ufset''
    where
      (fx, ufset') = find ufset x
      (fy, ufset'') = find ufset' y


readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

solve :: [(Int, Int, Int)] -> UnionFind -> [Int] -> [Int]
solve [] _ acc = reverse acc
solve ((op, x, y):xs) ufset acc
    | op == 0 = solve xs (union ufset x y) acc
    | otherwise = if fx == fy
                  then solve xs ufset'' (1:acc)
                  else solve xs ufset'' (0:acc)
    where (fx, ufset')  = find ufset x
          (fy, ufset'') = find ufset' y


main :: IO ()
main = do
  [n, _] <- map readInt'. BS.words <$> BS.getLine
  contents <- (map (\ x -> map readInt' (BS.words x)) .
                   BS.lines <$> BS.getContents)
  let res = solve (map (\ [x, y, z] -> (x, y, z)) contents)
            (initUnionFindSet n) []
  putStrLn (L.intercalate "\n" (map show res))
