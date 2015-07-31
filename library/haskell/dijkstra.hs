import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe
import qualified Data.Set              as S
import qualified Data.Tuple            as T

addToSet :: (Num a, Ord a) => S.Set (a, Int) -> [(Int, a)] -> S.Set (a, Int)
addToSet set xs = L.foldl' (\ acc x -> S.insert (T.swap x) acc) set xs


addToMap :: Ord k => M.Map k a -> [(k, a)] -> M.Map k a
addToMap m xs = L.foldl' (\ acc (x, d) -> M.insert x d acc) m xs


-- ^ O(n log^2 n) dijkstra algorithm by using the set structure
dijkstra :: (Num a, Ord a) =>
            M.Map Int [(Int, a)]        -- ^ graph structure
         -> Int                         -- ^ source node
         -> M.Map Int a                 -- ^ result
dijkstra graph source = dijkstra' graph (S.singleton (0, source))
                        (M.singleton source 0)


dijkstra' :: (Ord t, Num t) =>
             M.Map Int [(Int, t)]       -- ^ graph structure
          -> S.Set (t, Int)             -- ^ priority queue
          -> M.Map Int t
          -> M.Map Int t
dijkstra' graph pq res
    | S.null pq = res
    | otherwise = dijkstra' graph (addToSet pq' info) (addToMap res info)
    where
      fwd = M.findWithDefault
      ((dis, node), pq') = S.deleteFindMin pq
      nodes = fwd [] node graph
      update = filter (\ (x, e) -> (fwd (-1) x res) == (-1) ||
                                   dis + e < (fwd (-1) x res)) nodes
      info = map (\ (x, e) -> (x, dis + e)) update


buildGraph :: Ord t => [(t, t1, t2)] -> M.Map t [(t1, t2)]
buildGraph edges =
    let g = L.groupBy (\ (x, _, _) (y, _, _) -> x == y) edges
    in M.fromList (map (\ x -> (f1 $ head x, map (\ (_, y, z) -> (y, z)) x)) g)

readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

f1 :: (t, t1, t2) -> t
f1 (x, _, _) = x

f3 :: (t, t1, t2) -> t2
f3 (_, _, x) = x

main :: IO ()
main = do
  contents <- BS.lines <$> BS.getContents
  let edges = map (\ [x, y, z] -> (x, y, z))
              (map (\ x -> map readInt' (BS.words x)) contents)
      n = f1 $ head edges
      res = dijkstra (buildGraph $ L.sort $ tail edges)  (f3 $ head edges)
  forM_ [0..(n - 1)] $ \i -> do
         if M.member i res
         then print $ M.findWithDefault (-1) i res
         else putStrLn "INF"
