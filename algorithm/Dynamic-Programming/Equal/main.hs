import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as BS
import           Data.Maybe

solve :: [Int] -> Int
solve arr =
    let minValue = minimum arr
    in minimum [f x | x <- [(minValue - 5)..minValue]]
        where f i = sum $ map (\x -> c i x) arr
              c i x = (x - i) `div` 5 + (x - i) `mod` 5 `div` 2 +
                      (x - i) `mod` 5 `mod` 2

readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

main :: IO ()
main = do
  t <- readLn :: IO Int
  forM_ [1..t] $ \_ -> do
         _ <- BS.getLine
         arr <- map readInt' . BS.words <$> BS.getLine
         putStrLn $ show $ solve arr
