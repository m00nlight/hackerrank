import Control.Monad (forM_, when)
import Control.Monad.ST
import Data.Array.ST
import Data.Array.Unboxed
import qualified Data.Vector as V
import qualified Data.Set as S
import qualified Data.List as L

sieveUO :: Int -> UArray Int Bool
sieveUO top = runSTUArray $ do
    let m = (top-1) `div` 2
        r = floor . sqrt $ fromIntegral top + 1
    sieve <- newArray (1,m) True          -- :: ST s (STUArray s Int Bool)
    forM_ [1..r `div` 2] $ \i -> do       -- prime(i) = 2i+1
      isPrime <- readArray sieve i        -- ((2i+1)^2-1)`div`2 = 2i(i+1)
      when isPrime $ do
        forM_ [2*i*(i+1), 2*i*(i+2)+1..m] $ \j -> do
          writeArray sieve j False
    return sieve

primesToUO :: Int -> [Int]
primesToUO top | top > 1   = 2 : [2*i + 1 | (i,True) <- assocs $ sieveUO top]
               | otherwise = []

modulo = 10^9 + 7

primes = primesToUO 1000100
primeSet = S.fromList primes

isPrime :: Int -> Bool
isPrime num = S.member num primeSet

compNum num
    | odd num = if (isPrime (num - 2)) && 2 /= (num - 2)
                then 2 * (num - 2) else 1
    | otherwise = aux (tail primes)
    where aux [] = 1
          aux (p:ps)
              | p >= (num - p) = 1
              | isPrime (num - p) = p * (num - p) `mod` modulo
              | otherwise = aux ps
solve a b =
    let tmp = map compNum [a..b]
        ans = filter (/=1) tmp
        ret = L.foldl' (\ acc x -> acc * x `mod` modulo) 1 ans
    in (show $ length ans) ++ " " ++ (show (ret `mod` modulo))


main :: IO ()
main = do
  _ <- getLine
  cs <- getContents
  let qs = map (\ x -> map (read :: String -> Int) (words x)) (lines cs)
  mapM_ (\ [x, y] -> putStrLn $ solve x y) qs
