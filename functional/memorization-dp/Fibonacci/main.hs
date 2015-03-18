import qualified Data.Vector as V

modNumber = 100000007

fibs = 0:1: zipWith (\x y -> (x + y) `mod` modNumber) fibs (tail fibs)


fibsArray = V.fromList $ take 10010 fibs


main = do
    _ <- getLine
    nums <- getContents
    mapM_ (putStrLn . show) 
        (map (\x -> fibsArray V.! (read x :: Int)) (words nums))