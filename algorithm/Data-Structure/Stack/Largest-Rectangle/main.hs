import           Control.Applicative
import qualified Data.ByteString.Char8 as BS
import           Data.Maybe


solve :: [Int] -> Int
solve xs = maximum $ map (\ (x, y, z) -> x * (z - y)) (zip3 xs left right)
    where
      aux [] _ ans                    = reverse ans
      aux xs@(x:xs') stack@(s:ss) ans =
          if fst x > fst s
          then aux xs' (x:stack) (snd s:ans)
          else aux xs ss ans
      left = aux (zip xs [1..]) [(0, 0)] []
      right = reverse $ aux (reverse $ zip xs [0..]) [(0, length xs)] []


readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

main :: IO ()
main = do
  n <- BS.getLine
  tmp <- BS.words <$> BS.getLine
  let content = map readInt' tmp
  print $ solve content
