{-|
  Haskell pure style solution from ZhouYuChen. I change some name and add
  some comments to make the program more meaningful.
 -}

import           Control.Applicative
import           Control.Monad
import           Data.List


-- | The 'minFree' return the minimum natural number not in xs
minFree :: [Int] -> Int
minFree xs = head $ [0..] \\ sort xs


-- | Knight grundy value
k :: [[Int]]
k = [[grundy x y|x<-[0..y]]|y<-[0..]]
  where
    grundy 0 _ = 0
    grundy _ 1 = 0
    grundy 1 _ = 1
    grundy a b = if a<b then
                     minFree [k !!(b-2) !! (a-1), k !! (b-1) !! (a-2)]
                 else minFree [k !! (b-1) !! (a-2)]

ksg :: Int -> Int -> Int
ksg x y=if x<y then k !! y !! x else k !! x !! y


-- | Queen grundy value
q :: [[Int]]
q = [[grundy x y|x<-[0..]]|y<-[0..]]
  where
    grundy a b= minFree ( take a (q!!b) ++ take b (q!!a) ++
                          [q!!(a-i)!!(b-i)|i<-[1..(min a b)]])

main :: IO ()
main=do
  t <- readLn
  replicateM_ t $ do
    [a,b,x,y] <- map read . words <$> getLine
    putStrLn $ if (ksg a b)==(q!!x!!y) then "LOSE" else "WIN"
