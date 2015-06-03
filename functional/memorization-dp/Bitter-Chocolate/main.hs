import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as BS
import           Data.List
import qualified Data.Map              as M
import           Data.Maybe

dp :: Int -> Int -> Int -> M.Map (Int, Int, Int) Bool
dp r1 r2 r3 =
    foldl' (\ acc (x,y,z) -> M.insert (x, y, z) (isWin x y z acc) acc)
           M.empty
           [(x, y, z) | x <- [0..r1], y <- [0..r2], z <- [0..r3]]
        where
          fd = M.findWithDefault
          isWin 0 0 0 _   = True
          isWin 1 0 0 _   = False
          isWin x y z acc = flag1 || flag2 || flag3
              where
                flag1 = any not [fd True (x, y, zz) acc |
                                 zz <- [0..(z - 1)]]
                flag2 = any not [fd True (x,yy, min yy z) acc |
                                 yy <- [0..(y - 1)]]
                flag3 = any not [fd True (xx, min xx y, min xx z) acc |
                                 xx <- [0..(x - 1)]]


solve :: Int -> Int -> Int -> String
solve r1 r2 r3 =
    let ans = dp r1 r2 r3
    in if fromJust $ M.lookup (r1, r2, r3) ans then
           "WIN"
       else
           "LOSE"

readInt' = fst . fromJust . BS.readInt

main :: IO ()
main = do
  tc <- readLn :: IO Int
  forM_ [1..tc] $ \i -> do
         [r1, r2, r3] <- map (\ x -> read x :: Int) . words <$> getLine
         putStrLn $ solve r1 r2 r3
