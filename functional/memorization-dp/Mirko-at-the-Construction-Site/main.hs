import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as BS
import           Data.List
import qualified Data.Map              as M
import           Data.Maybe

type Point = (Int, Int)
type Line = (Point, Int)

eval :: Line -> Int -> Int
eval line t =
    let (slope, h) = fst line
    in slope * t + h

ccw :: Point -> Point -> Point -> Int
ccw p1@(x1, y1) p2@(x2, y2) p3@(x3, y3) =
    (y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)

bad :: Line -> Line -> Line -> Bool
bad l1@(p1, _) l2@(p2, _) l3@(p3, _) = aux c
    where c = ccw p1 p2 p3
          aux c | c == 0    = snd p2 < snd p3
                | otherwise = c < 0


add :: Line -> [Line] -> [Line]
add l []       = [l]
add l [x]      = [l, x]
add l (x:y:ls) =
    if bad y x l then
        add l (y:ls)
    else (l:x:y:ls)


rPop :: [Line] -> Int -> Bool
rPop [] _       = False
rPop [_] _      = False
rPop (x:y:_) t  =
    let a = eval y t
        b = eval x t
    in (a > b || a == b && snd y > snd x)


solve :: [(Int, Int)] -> [Line] -> M.Map Int Int -> M.Map Int Int
solve [] _ acc                = acc
solve ((q, idx):qs) stack acc =
    let nstack = until (\x -> not $ rPop x q) tail stack
    in solve qs nstack (M.insert idx (snd $ head nstack) acc)

readInt' = fst . fromJust . BS.readInt

main :: IO ()
main = do
  [n, q] <- map (\x -> read x :: Int) . words <$> getLine
  hs <- map readInt' . BS.words <$> BS.getLine
  ss <- map readInt'  . BS.words <$> BS.getLine
  qs <- map readInt' . BS.lines <$> BS.getContents
  let ls = sort $  zip (zip ss hs) [1..n]
      stack = foldl' (\ acc x -> add x acc) [] ls
      rstack = reverse stack
      ans = solve (sort $ zip qs [1..]) rstack  M.empty
  forM_ [1..q] $ \i ->
      do
        putStrLn $ show $ M.findWithDefault (-1) i ans
