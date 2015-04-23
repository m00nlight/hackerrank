import Control.Monad
import Control.Applicative

validBST :: [Int] -> Bool
validBST [] = True
validBST (root:xs) = any id $ map aux [0..(length xs)]
    where aux idx =
              let (left, right) = splitAt idx xs
              in all (<=root) left && all (>=root) right
                     && validBST left && validBST right

main :: IO ()
main = do
  n <- readLn :: IO Int
  forM_ [1..n] $ \_ -> do
         _ <- getLine
         xs <- map read . words <$> getLine
         if validBST xs then putStrLn "YES" else putStrLn "NO"
