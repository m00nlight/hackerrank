import           Control.Applicative
import qualified Data.ByteString.Char8 as BS
import           Data.Maybe

solve :: [Int] -> Int
solve xs = aux xs [] 0
    where
      aux [] _ ans = ans
      aux (x:xs') [] ans = aux xs' [(x, 0)] ans
      aux xs@(x:xs') ss@(s:ss') ans =
          if x > fst s
          then aux xs' ((x, 1):ss) (max ans 1)
          else let pr = maximum $ map snd (takeWhile (\ y -> fst y >= x) ss)
                   ns = dropWhile (\ y -> fst y >= x) ss
               in case ns of
                    [] -> aux xs' [(x, 0)] ans
                    _  -> aux xs' ((x, pr + 1):ns) (max ans (pr + 1))


readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

main :: IO ()
main = do
  _ <- BS.getLine
  tmp <- BS.words <$> BS.getLine
  let content = map readInt' tmp
  print $ solve content
