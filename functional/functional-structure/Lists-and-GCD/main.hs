import qualified Data.List as L
import qualified Data.Map as M

solve :: [[Int]] -> [(Int, Int)]
solve xs = M.toList $ foldr (\x a -> M.intersectionWith min a x) (head ys) ys
    where zs = map group xs
          ys = map M.fromList zs

group :: [Int] -> [(Int, Int)]
group [] = []
group (x:y:xs) = (x, y): group xs


main :: IO ()
main = do
  _ <- getLine
  content <- getContents
  let d = map (\x -> map (read :: String -> Int) (words x)) (lines content)
      tmp = solve d
      res = foldr (\ (x, y) acc -> x:y:acc) [] tmp
  putStrLn $ L.intercalate " " $ map show res
