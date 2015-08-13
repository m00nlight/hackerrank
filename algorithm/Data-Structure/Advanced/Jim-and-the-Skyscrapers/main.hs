{-# LANGUAGE BangPatterns #-}
import           Control.Applicative
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe
import qualified Data.Vector           as V


data RMQ a =
    Leaf {
      val         :: a
    , left, right :: Int
    } |
    Node {
      leftChild        :: RMQ a
    , rightChild       :: RMQ a
    , left, right, mid :: Int
    , val              :: a
    } deriving (Show, Eq, Ord)

buildRMQ :: [Int] -> RMQ Int
buildRMQ vs = build 1 n
    where
      n = until (>= length vs) (*2) 1
      vvs = V.fromList $ vs ++ (take (n - length vs)
                                (repeat (minBound :: Int)))
      build l r
          | l == r = Leaf { val = vvs V.! (l - 1)
                          , left = l
                          , right = r}
          | otherwise =
              let m   = (l + r) `div` 2
                  lc  = build l m
                  rc  = build (m + 1) r
              in Node { val = max (val lc) (val rc)
                      , leftChild = lc
                      , rightChild = rc
                      , left = l
                      , right = r
                      , mid = m
                      }


queryRMQ :: RMQ Int -> Int -> Int -> Int
queryRMQ root l r
    | (left root) >= l && (right root) <= r  = val root
    | r <= mid root = queryRMQ (leftChild root) l r
    | l > mid root  = queryRMQ (rightChild root) l r
    | otherwise =
        max (queryRMQ (leftChild root) l r) (queryRMQ (rightChild root) l r)


solve :: [Int] -> Int
solve hs = ret
    where
      !rmq = buildRMQ hs
      f (ans, cmap, lmap) (h, idx) =
          let lh = M.findWithDefault (-1) h lmap
              cc = if lh == (-1) || queryRMQ rmq lh idx > h
                   then 0
                   else M.findWithDefault 0 h cmap
          in ((ans + cc), M.insert h (cc + 1) cmap, M.insert h idx lmap)
      !(ret, _, _) = L.foldl f (0, M.empty, M.empty) (zip hs [1..])



readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

main :: IO ()
main = do
  _ <- BS.getLine
  input <- BS.words <$> BS.getLine
  let hs = map readInt' input
      res = solve hs
  print (res * 2)
