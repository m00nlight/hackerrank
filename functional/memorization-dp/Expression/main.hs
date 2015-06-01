import Control.Applicative
import qualified Data.Map as M
import Data.List


-- DP approach, dp[i][j] means whether the first i number
-- can produce number j(j <= 101). The following is a very nice
-- approach to do the dp process by reading @tanakh's solution

main :: IO ()
main = do
    n <- readLn :: IO Int
    ns <- map read . words <$> getLine
    let result = foldl' f (M.fromList [(head ns, [show $ head ns])]) (tail ns)
        f  m n = M.fromList $
                    concatMap (\(val, ops) ->
                        [ ((val+n)`mod`101, (show n):"+":ops)
                        , ((val-n)`mod`101, (show n):"-":ops)
                        , ((val*n)`mod`101, (show n):"*":ops)
                        ]) $
                    M.toList m
        ans = intercalate "" $ reverse $ result M.! 0
    putStrLn ans
