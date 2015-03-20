import qualified Data.Vector as V

p = 100000007

comb n = comb' n [[1]]
    where
      comb' 0 acc = reverse acc
      comb' n acc =
          let lr = head acc
              cr = zipWith (\x y -> (x + y) `mod` p) (lr ++ [0]) (0:lr)
          in comb' (n - 1) (cr:acc)

combinations = V.fromList (map V.fromList $ comb 1005)

solve n k = (combinations V.! n) V.! k

main = do
  _ <- getLine
  contents <- getContents
  let args = map (\x -> map (read :: String -> Int) (words x)) (lines contents)
  mapM_ (\ [n, k] -> putStrLn $ show $ solve n k) args
