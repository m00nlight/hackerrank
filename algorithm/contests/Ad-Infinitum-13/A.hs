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

f1 :: (t, t1, t2) -> t
f1 (x, _, _) = x

f3 :: (t, t1, t2) -> t2
f3 (_, _, x) = x

solve :: Int -> Int -> String
solve a b
    | a == 0 || b == 0 = "First"
    | otherwise =
        if ((max a b) - (min a b) + 1) `mod` 2 == 0
        then "First"
        else "Second"

main :: IO ()
main = do
  n <- BS.getLine
  forM_ [1..(readInt' n)] $ \_ -> do
         ab <- BS.getLine
         let tmp = map readInt' $ BS.words ab
             res = solve (tmp !! 0) (tmp !! 1)
         putStrLn res
