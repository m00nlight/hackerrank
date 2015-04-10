import           Control.Applicative
import           Data.List

modulo :: Integer
modulo = 10^9 + 7


processQueries
  :: [(Char, Int, Int)] -> SegTree -> [Integer] -> [Integer]
processQueries [] _ acc = reverse acc
processQueries (('Q', l, r):q) root acc =
    let ans = (query (l, r) root) `mod` modulo
    in processQueries q root (ans : acc)
processQueries ((_, idx, value):q) root acc =
    let oldVal = query (idx, idx) root
        newVal = oldVal * (fromIntegral value)
        nroot = update idx newVal root
    in processQueries q nroot acc

solve :: Int -> [Integer] -> [(Char, Int, Int)] -> [Integer]
solve n arr queries = processQueries queries tree []
    where
      tree = foldl' (\ root (idx, v) -> update idx v root)
             (initSegTree n)
             (zip [0..] arr)

main :: IO ()
main = do
  n <- (read :: String -> Int) <$> getLine
  arr <- map (read :: String -> Integer) . words <$> getLine
  _ <- (read :: String -> Int) <$> getLine
  queryString <- lines <$> getContents
  let queries = map (\ x -> (\ [[p], q, r] ->(p, read q :: Int, read r :: Int))
                            (words x)) queryString
  mapM_ print $ solve n arr queries


-- | The following code is related with segment tree

data SegTree =
    Node {
      val                   :: Integer
    , left, right           :: Int
    , leftChild, rightChild :: SegTree
    } |
    Leaf {
      val         :: Integer
    , left, right :: Int
    }

initSegTree :: Int -> SegTree
initSegTree n = aux 0 (n - 1)
    where aux l r
              | l == r = Leaf {val = -1, left = l, right = r}
              | otherwise =
                  let mid = (l + r) `div` 2
                  in Node { val = -1, left = l, right = r
                          , leftChild = aux l mid
                          , rightChild = aux (succ mid) r
                          }


query :: (Int, Int) -> SegTree -> Integer
query range@(l, r) root
    | r < left root = 1
    | l > right root = 1
    | l <= left root && right root <= r = val root
    | otherwise =
        lcm (query range (leftChild root)) (query range (rightChild root))


update :: Int -> Integer -> SegTree -> SegTree
update idx newVal root
    | left root <= idx && idx <= right root =
      case root of
        Leaf {} -> root {val = newVal }
        _ -> root {val = lcm newVal (val root),
                 leftChild = lChild, rightChild = rChild }
    | otherwise = root
    where
      lChild = update idx newVal $ leftChild root
      rChild = update idx newVal $ rightChild root
