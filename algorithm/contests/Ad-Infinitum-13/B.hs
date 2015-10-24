import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe
import qualified Data.Set              as S
import qualified Data.Tuple            as T

type Point = (Int, Int)

readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

solve ptr1@(x1, y1) ptr2@(x2, y2) ptr3@(x3, y3) =
    let twoArea = getTwoArea ptr1 ptr2 ptr3
        i1 = getPointInLine ptr1 ptr2
        i2 = getPointInLine ptr2 ptr3
        i3 = getPointInLine ptr1 ptr3
        b = i1 + i2 + i3 - 3
    in (twoArea + 2 - b) `div` 2

getPointInLine (x1, y1) (x2, y2) =
    gcd (abs $ x1 - x2) (abs $ y1 - y2) + 1

getTwoArea (x1, y1) (x2, y2) (x3, y3) =
    abs $ (x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)

main :: IO ()
main = do
  n <- BS.getLine
  forM_ [1..(readInt' n)] $ \_ -> do
         infoStr <- BS.getLine
         let info = map readInt' (BS.words infoStr)
             res = solve (info !! 0, info !! 1) (info !! 2, info !! 3)
                   (info !! 4, info !! 5)
         putStrLn $ show res
