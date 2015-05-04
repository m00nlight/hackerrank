import Data.Array.ST
import Data.Array.Unboxed
import Control.Monad (forM_, when)

-- | The 'sieveTo' run esteranto sieve method up to n
sieveTo :: Int -> UArray Int Bool
sieveTo n = runSTUArray $ do
              let r = floor . sqrt $ fromIntegral n + 1
              sieve <- newArray (1, n) True
              writeArray sieve 1 False
              forM_ [4,6..n] $ \i -> do
                            writeArray sieve i False
              forM_ [3,5..r] $ \i -> do
                            isPrime <- readArray sieve i
                            when isPrime $ do
                                       forM_ [i*i,i*i+i..n] $ \j -> do
                                             writeArray sieve j False
              return sieve

-- | The 'primeTo' get primes up to n, and return the prime numbers as list
primeTo :: Int -> [Int]
primeTo n = [i | (i, True) <- assocs $ sieveTo n]


main :: IO ()
main = undefined
