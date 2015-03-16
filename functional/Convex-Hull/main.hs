import Text.Printf


eps = 1e-10

add :: Double -> Double -> Double
add a b =
    if abs (a - b) < eps * (abs a + abs b) then
        0
    else a + b


doubleCmp :: Double -> Double -> Ordering
doubleCmp a b
    | a - b < -eps = LT
    | abs (a - b) < eps = EQ
    | True = GT


vectorAdd :: (Double, Double) -> (Double, Double) -> (Double, Double)
vectorAdd (x1, y1) (x2, y2) = (add x1 x2, add y1 y2)

vectorSub :: (Double, Double) -> (Double, Double) -> (Double, Double)
vectorSub (x1, y1) (x2, y2) = (add x1 (-x2), add y1 (-y2))


vectorMul :: Num t => (t, t) -> t -> (t, t)
vectorMul (x, y) d = (x * d, y * d)

-- dot product of two vector
vectorDot :: (Num a) => (a, a) -> (a, a) -> a
vectorDot (x1, y1) (x2, y2) = x1 * x2 + y1 * y2

-- det product of two vector
vectorDet :: (Double, Double) -> (Double, Double) -> Double
vectorDet (x1, y1) (x2, y2) =
    add (x1 * y2) ((-y1) * x2)

graham :: (Num a) => [(a, a)] -> [(a, a)]
graham ps = aux (drop 2 ps) (take 2 ps)
    where
      aux [] stack = stack
      aux (p:ps') stack = []


solve :: [(Int, Int)] -> Double
solve points = 0.0 --Complete this function


main :: IO ()
main = do
  n <- readLn :: IO Int
  content <- getContents
  let
    points = map (\[x, y] -> (x, y)).
             map (map (read::String->Int)). map words. lines $ content
    ans = solve points
  printf "%.1f\n" ans
