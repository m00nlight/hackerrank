import           Data.Char
import qualified Data.Map    as M
import qualified Data.Vector as V

clean :: String -> String
clean = filter (\x -> x `elem` "><+-.,[]")

mapBracket :: String -> [(Int, Int)]
mapBracket prog = aux prog 0 [] []
    where aux [] _ _ ret             = ret
          aux ('[':ps) cur stack ret = aux ps (cur + 1) (('[',cur):stack) ret
          aux (']':ps) cur stack ret =
              let (_, idx) = head stack
              in aux ps (cur + 1) (tail stack) ((cur, idx):(idx,cur):ret)
          aux (_:ps) cur stack ret   = aux ps (cur + 1) stack ret



runProgram :: String -> String -> (Int, [Int])
runProgram prog input = aux progv (map ord input) memo 0 0 0 []
    where memo   = V.fromList $ replicate 200 0
          bmap   = M.fromList $ mapBracket prog
          progv  = V.fromList prog
          inc  x = (x + 1) `mod` 256
          dec  x = (x - 1 + 256) `mod` 256
          aux pv input memo pp dp step out
              | pp >= V.length pv  =  (step, reverse out)
              | step >= 100000     =  (step + 1, reverse out)
              | otherwise =
                  case (pv V.! pp) of
                    '>' -> aux pv input memo (pp + 1) (dp + 1) (step + 1) out
                    '<' -> aux pv input memo (pp + 1) (dp - 1) (step + 1) out
                    '+' -> (aux pv input (memo V.// [(dp, inc $ memo V.! dp)])
                            (pp + 1) dp (step + 1) out)
                    '-' ->  aux pv input (memo V.// [(dp, dec $ memo V.! dp)])
                            (pp + 1) dp (step + 1) out
                    ',' -> aux pv (tail input) (memo V.// [(dp, head input)])
                           (pp + 1) dp (step + 1) out
                    '.' -> aux pv input memo (pp + 1) dp (step + 1)
                           ((memo V.! dp):out)
                    '[' -> if (memo V.! dp) == 0 then
                               aux pv input memo (bmap M.! pp) dp
                                   (step + 1) out
                           else aux pv input memo (pp + 1) dp (step + 1) out
                    ']' -> if (memo V.! dp) /= 0 then
                               aux pv input memo (bmap M.! pp) dp
                                   (step + 1) out
                           else aux pv input memo (pp + 1) dp (step + 1) out


getResult :: (Int, [Int]) -> [[Char]]
getResult (step, output) =
    if step > 100000 then
        [map chr output, "PROCESS TIME OUT. KILLED!!!"]
    else
        [map chr output]

main :: IO ()
main = do
  _ <- getLine
  input <- getLine
  progStr <- getContents
  let prog    = clean progStr
      bmap    = mapBracket prog
      res     = runProgram prog input
      result  = getResult $ res
  putStrLn $ show res
  mapM_ putStrLn result
