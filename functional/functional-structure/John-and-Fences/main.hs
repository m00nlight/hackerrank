

maxRectangle hs = maximum $ zipWith3 (\ x l r -> x * (r - l)) hs left right
    where
      go [] _ ans _                  = reverse ans
      go (h:hs') [] ans idx          = go hs' [(h,idx)] (0:ans) (idx + 1)
      go (h:hs') ((h',j):ss) ans idx =
          if h <= h' then
              go (h:hs') ss ans idx
          else
              go hs' ((h,idx):(h',j):ss) ((j+1):ans) (idx + 1)
      n     = length hs
      left  = go hs [] [] 0
      right = reverse $ map (\x -> n - x) (go (reverse hs) [] [] 0)


main = do
  n <- getLine
  content <- getContents
  let hs = map (read :: String -> Int) (words content)
  putStrLn $ show $ maxRectangle hs
