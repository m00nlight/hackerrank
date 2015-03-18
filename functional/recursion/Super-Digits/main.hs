import Data.Char
import qualified Data.List as L

superDigit :: Int -> Int
superDigit n = 
    if n `div` 10 == 0 then 
        n
    else superDigit  $ sum $ map (\x -> ord x - ord '0') $ show n
               
               
main = do
    line <- getLine
    let [num,times] =  (words line)
        n = (read times) :: Int
        tmp = sum $ map (\x -> ord x - ord '0') num
    putStrLn $ show $ 
        superDigit $ tmp * n