import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe
import qualified Data.Set              as S
import qualified Data.Tuple            as T


readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

solve :: Integral a => a -> a -> String
solve n k
    | k > n * (n + 1) `div` 2 || k < (-n * (n + 1) `div` 2 + 2) = "NO"
    | (abs k) `mod` 2 == n * (n + 1) `div` 2 `mod` 2 = "YES"
    | otherwise = "NO"

main :: IO ()
main = do
  n <- BS.getLine
  forM_ [1..(readInt' n)] $ \_ -> do
         nk <- BS.getLine
         let arr = map readInt' (BS.words nk)
         putStrLn $ solve (arr !! 0) (arr !! 1)
