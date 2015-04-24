import Data.Char (isNumber)

getWord :: String -> Char
getWord str =
    let idxs = takeWhile isNumber str
        word = dropWhile isNumber str
        idx = read idxs :: Int
    in if idx >= length word then ' ' else word !! idx
--    in if idx >= length word then ' ' else word !! idx

solve :: [String] -> String
solve xs = map getWord xs

main :: IO ()
main = do
  c <- getLine
  putStrLn $ solve (words c)
