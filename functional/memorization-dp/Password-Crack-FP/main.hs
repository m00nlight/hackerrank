import           Control.Applicative
import           Control.Monad
import qualified Data.ByteString.Char8 as B
import           Data.List
import qualified Data.Map              as M

subs ss x y = B.drop (x - y) (B.take x ss)

-- solve :: [String] -> String -> String
dp :: [String] -> String -> M.Map Int Int
dp words pss =
    foldl' (\ acc x -> f acc x ws) (M.singleton 0 (-1)) [1..(B.length ps)]
        where
          ps = B.pack pss
          ws = map B.pack words
          f map _ []      = map
          f map x (w:ws') =
              if (subs ps x (B.length w)) == w && M.member (x - B.length w) map
              then M.insert x (x - B.length w) map
              else f map x ws'

path _ _ 0 acc    = acc
path ans ss n acc =
    let nn = M.findWithDefault (-1) n ans
    in path ans ss nn ((subs ss n (n - nn)):acc)


solve :: [String] -> String -> [B.ByteString]
solve words pss =
    let l = length pss
        ans = dp words pss
    in if not $ M.member l ans then
           []
       else
           path ans (B.pack pss) l []


main :: IO ()
main = do
  n <- readLn :: IO Int
  forM_ [1..n] $ \ i -> do
         _  <- getLine
         ws <- words <$> getLine
         ps <- getLine
         let ans = map B.unpack $ solve ws ps
         if null ans then
             putStrLn "WRONG PASSWORD"
         else
             putStrLn $ intercalate " " ans
