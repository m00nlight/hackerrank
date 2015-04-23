import qualified Data.Map as M
import Control.Monad
import Data.List (intercalate)

data Tree a = Node a (Tree a) (Tree a) | Null

instance Show a => Show (Tree a) where
    show x = intercalate " " (map show $ helper x)
        where helper Null            = []
              helper (Node root l r) = helper l ++ [root] ++ helper r

swapNode :: Tree a -> Int -> Tree a
swapNode root k = aux 1 root
    where
      aux _ Null = Null
      aux d (Node x lt rt)
          | d `rem` k == 0 = Node x (aux (d + 1) rt) (aux (d + 1) lt)
          | otherwise = Node x (aux (d + 1) lt) (aux (d + 1) rt)

buildTree :: Int -> M.Map Int (Int, Int) -> Tree Int
buildTree (-1) _  = Null
buildTree root ms = let (l, r) = ms M.! root
                 in Node root (buildTree l ms) (buildTree r ms)

main :: IO ()
main = do
  n <- readLnInt
  c <- replicateM n $ do (a:b:_) <- readLnInts
                         return (a,b)
  let m = M.fromList $ zip [1..n] c
      m' = buildTree 1 m
  t <- readLnInt
  hs <- replicateM t readLnInt
  mapM_ (putStrLn . show) $ tail (scanl swapNode m' hs)
    where readLnInt = readLn :: IO Int
          readLnInts = liftM (map (read::String->Int) . words) getLine
