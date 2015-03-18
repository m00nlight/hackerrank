solve :: Int -> Int -> Int -> Int
solve num n start = sum $ map aux [start..upper]
    where
        upper = ceiling $ (fromIntegral num) ** (1 /  (fromIntegral n))
        aux x 
            | num - x^n == 0 = 1
            | num - x^n < 0 = 0
            | otherwise = solve (num - x^n) n (x + 1)

main = do
    contents <- getContents
    let [num, n] = map (read :: String -> Int) (lines contents)
    putStrLn $ show $ solve num n 1