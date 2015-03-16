{-# Language UnicodeSyntax #-}
import Prelude.Unicode
import Text.Printf (printf)

-- This function should return a list [area, volume].
solve :: (RealFrac t, Floating t) => t -> t -> [t] -> [t] -> [t]
solve l r a b = [area, volume]
    where
      gap = 0.001
      -- calculate a0 * x^b0 + a1 * x^b1, ..., + an-1 * x^bn-1
      f x = sum $ map (\(p,q) -> p * (x ** q)) (zip a b)
      n = round $ (r - l) / gap :: Int
      area = sum $ map (\i -> (f (l + gap * (fromIntegral i))) * gap) [1..n]
      volume = sum $ map
               (\i -> π * (f (l + gap * (fromIntegral i))) ** 2 * gap) [1..n]

--Input/Output.
main :: IO ()
main = getContents >>= mapM_ (printf "%.1f\n").
       (\[a, b, [l, r]] -> (solve l r a b) :: [Double]).
       map (map read. words). lines
