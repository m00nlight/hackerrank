import           Control.Applicative
import           Data.List
import qualified Data.Map            as Map

type Pair = (Int, Int)

modulo :: Int
modulo = 10^(9::Int) + 7

isPrime :: Int -> Bool
isPrime n = not . any (\ x -> n `rem` x == 0) $ [2..(n - 1)]

primes :: [Int]
primes = (filter isPrime [2..100])

factors :: Int -> [Pair]
factors n = map (\ x -> (head x, length x)) $ group $ aux n primes []
    where
      aux n' [] acc     = if n' /= 1 then reverse $ (n':acc) else reverse acc
      aux n' (p:ps) acc = if n' `rem` p == 0
                          then aux (n' `div` p) (p:ps) (p : acc)
                          else aux n' ps acc

primeFactors :: Map.Map Int [Pair]
primeFactors = Map.fromList $ map (\x -> (x, factors x)) [1..100]

powerHelp :: (Int -> Int -> Int) -> [Pair] -> [Pair] -> [Pair]
powerHelp _ [] ys = ys
powerHelp _ xs [] = xs
powerHelp f xxs@((a1, b1):xs) yys@((a2,b2):ys)
    | a1 == a2  = (a1, b1 `f` b2) : powerHelp f xs ys
    | a1 < a2   = (a1, b1) : powerHelp f xs yys
    | otherwise = (a2, b2) : powerHelp f xxs ys

lcmFactors :: [Pair] -> [Pair] -> [Pair]
lcmFactors = powerHelp max

mergeFactors :: [Pair] -> [Pair] -> [Pair]
mergeFactors = powerHelp (+)


getFactors :: Int -> SegTree -> Map.Map Int Int
getFactors _ (Leaf {factor = f}) = f
getFactors idx root
    | idx <= right (leftChild root) = getFactors idx (leftChild root)
    | otherwise                     = getFactors idx (rightChild root)


processQueries :: [(Char, Int, Int)] -> SegTree -> [Int] -> [Int]
processQueries [] _  acc = reverse acc
processQueries (('Q', l, r):q) root acc =
    let ans = factor2Value $ rangeQuery (l, r) root
    in processQueries q root (ans : acc)
processQueries (('U', idx, val):q) root  acc =
    let originFactor = Map.toList $ getFactors idx root
        newFactor = mergeFactors originFactor (primeFactors Map.! val)
        newRoot = updateTree idx newFactor root
    in processQueries q newRoot acc

solve :: Int -> [Int] -> [(Char, Int, Int)] -> [Int]
solve n arr queries = processQueries queries tree []
    where
      tree = foldl' (\ root (idx, val)-> updateTree idx
                                         (primeFactors Map.! val) root)
             (initSegTree n)
             (zip [0..] arr)

updatePower :: Int -> Int -> Map.Map Int Int -> Map.Map Int Int
updatePower base p_new fact =
  let p_old = Map.findWithDefault 0 base fact
  in  if p_new > p_old then Map.insert base p_new fact
      else fact

factor2Value :: [(Int, Int)] -> Int
factor2Value = foldr (\(b, p) acc -> acc * b^p `mod` modulo) 1


{-|
  Code Related with segment tree in haskell
 -}

data SegTree =
    Node {
      factor                :: Map.Map Int Int
    , left, right           :: Int
    , leftChild, rightChild :: SegTree
    } |
    Leaf {
      factor      :: Map.Map Int Int
    , left, right :: Int
    }


initSegTree :: Int -> SegTree
initSegTree n = aux 0 (n - 1)
    where aux l r
              | l == r = Leaf {factor = Map.empty, left = l, right = l}
              | otherwise =
                  let mid = (l + r) `div` 2
                  in Node { factor = Map.empty, left = l, right = r
                          , leftChild = aux l mid
                          , rightChild = aux (succ mid) r
                          }

rangeQuery :: (Int, Int) -> SegTree -> [(Int, Int)]
rangeQuery range@(l, r) root
    | r < left root  = []
    | l > right root = []
    | l <= left root && right root <= r = Map.toList (factor root)
    | otherwise = lcmFactors
                  (rangeQuery range (leftChild root))
                  (rangeQuery range (rightChild root))



-- |^  The 'updateTree' function update element in segment tree by multiply
-- value val. So the new value in the node is a * val, val is represented
-- in Pair form.
updateTree :: Int -> [Pair] -> SegTree -> SegTree
updateTree idx facts root
    | left root <= idx && idx <= right root =
        case root of
          Leaf {} -> root {factor = nFactors }
          _ -> root {factor = nFactors,
                     leftChild = lChild, rightChild = rChild}
    | otherwise = root
    where
      lChild = updateTree idx facts (leftChild root)
      rChild = updateTree idx facts (rightChild root)
      nFactors = foldr (\(base, p_new) fact -> updatePower base p_new fact)
                 (factor root) facts


main :: IO ()
main = do
  n <- (read :: String -> Int) <$> getLine
  arr <- map (read :: String -> Int) . words <$> getLine
  _ <- (read :: String -> Int) <$> getLine
  queryString <- lines <$> getContents
  let queries = map (\ x -> (\ [[p], q, r] ->(p, read q :: Int, read r :: Int))
                            (words x)) queryString
  mapM_ print $ solve n arr queries
