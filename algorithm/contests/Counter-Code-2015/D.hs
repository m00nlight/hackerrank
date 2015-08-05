import           Control.Applicative
import qualified Data.ByteString.Char8 as BS
import           Data.Maybe


solve :: (Ord a1, Ord a, Num a) => [a1] -> [(a1, a)] -> a -> a
solve [] _  ans = ans
solve (x:xs) [] ans = solve xs [(x,0)] ans
solve (x:xs) ((p,q):ss) ans
    | x > p = solve xs ((x, 1):(p,q):ss) (max ans 1)
    | otherwise =
        let
            pr = maximum $ map snd (takeWhile (\ (m, _) ->  m >= x) ((p,q):ss))
            nstack = dropWhile (\ (m, _) -> m >= x) ((p,q):ss)
        in if null nstack
           then solve xs [(x, 0)] ans
           else solve xs ((x, pr + 1):nstack) (max ans (pr + 1))

readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt


main :: IO ()
main = do
  _ <- BS.getLine
  content <- BS.words <$> BS.getLine
  let arr = map readInt' content
  print $  solve arr [] 0
