import           Control.Monad
import           Data.Bits
import           Data.List
import qualified Data.Map      as M

fw :: a -> Int -> M.Map Int a -> a
fw = M.findWithDefault

grundy :: Int -> M.Map Int Int
grundy n =
    foldl' (\ acc x -> M.insert x (help x acc) acc) (M.singleton 0 0) [1..n]
        where
          minFree xs = head $ [0..] \\ (sort xs)
          help x acc = minFree $ sort . nub $
                       [(fw 0 k acc) `xor` (fw 0 (x - k - 1) acc) |
                        k <- [0..(x - 1)]] ++
                       [(fw 0 k acc) `xor` (fw 0 (x - k - 2) acc) |
                        k <- [0..(x - 2)]]

grundyNumbers :: M.Map Int Int
grundyNumbers = grundy 305


solve :: String -> String
solve states =
    let gs = filter (\ x -> head x == 'I') (group states)
        ls = map length gs
        gn = foldl' (\ acc x -> acc `xor` (fw 0 x grundyNumbers)) 0 ls
    in if gn == 0 then "LOSE" else "WIN"


main :: IO ()
main = do
  t <- readLn :: IO Int
  forM_ [1..t] $ \_ -> do
         _ <- getLine
         states <- getLine
         putStrLn $ solve states
