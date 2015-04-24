solve :: [String] -> String
solve xs = map head xs

main :: IO ()
main = do
  c <- getLine
  putStrLn $ solve (words c)
