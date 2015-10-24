import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe
import qualified Data.Set              as S
import qualified Data.Tuple            as T

mmod = 1000000007 :: Int

readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt


exGcd :: Integral t => t -> t -> (t, t, t)
exGcd a b =
    if b == 0 then (a, 1, 0)
    else let (g, x, y) = exGcd b (a `mod` b)
         in (g, y, x - (a `div` b) * y)

modInv :: Integral a => a -> a -> Maybe a
modInv a m =
    if gcd a m /= 1 then Nothing
    else let (_, x, y) = exGcd a m
         in Just $ (m + x `mod` m) `mod` m

powMod :: (Integral a1, Integral a) => a1 -> a -> a1 -> a1
powMod a b c = powMod' a b c 1
    where
      powMod' a b c acc
          | b == 0 = acc
          | b `mod` 2 == 0 = powMod' (a * a `mod` c) (b `div` 2) c acc
          | otherwise = powMod' (a * a `mod` c) (b `div` 2) c (a * acc `mod` c)

solve d k h =
    if k <= h then
        (powMod d (k + 1) mmod + mmod - 1)
        `mod` mmod * (fromJust $ modInv (d - 1) mmod) `mod` mmod
    else
        let diff = k - h
            res1 = (powMod d (k + 1) mmod - powMod d diff mmod + mmod)
                   `mod` mmod * (fromJust $ modInv (d - 1) mmod) `mod` mmod
            res2 = if diff `mod` 2 == 1
                   then (powMod d diff mmod + mmod - d) *
                        (fromJust $ modInv (d * d - 1) mmod) `mod` mmod
                   else (powMod d diff mmod + mmod - 1) *
                        (fromJust $ modInv (d * d - 1) mmod) `mod` mmod
        in (res1 + res2) `mod` mmod


main :: IO ()
main = do
  n <- BS.getLine
  forM_ [1..(readInt' n)] $ \_ -> do
         dkhStr <- BS.getLine
         let dkh = map readInt' (BS.words dkhStr)
             res = solve (dkh !! 0) (dkh !! 1) (dkh !! 2)
         putStrLn $ show res
