import           Control.Applicative
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe
import           Text.Printf

-- use map to store data, and the occurance of each elements, and the
-- second element of the tuple is the size of the multiset
type MS k = (M.Map k Int ,Int)

type MedianMS k = (MS k , MS k )

getSize :: (Eq k, Ord k) => MS k -> Int
getSize = snd

msInsert :: (Eq k, Ord k) => k -> MS k -> MS k
msInsert e (storage, size) =
    case M.lookup e storage of
      Nothing -> (M.insert e 1 storage, size + 1)
      Just v  -> (M.insert e (v + 1) storage, size + 1)

msErase :: (Eq k, Ord k) => k -> MS k -> MS k
msErase e (storage, size) =
    case M.lookup e storage of
      Nothing -> (storage, size)
      Just v  -> if v == 1
                 then (M.delete e storage, size - 1)
                 else (M.insert e (v - 1) storage, size - 1)

msContains :: (Eq k, Ord k) => k -> MS k-> Bool
msContains e (storage, size) = M.member e storage


msGetMin :: (Eq k) => MS k-> k
msGetMin (storage, size) = fst $ M.findMin storage

msGetMax :: (Eq k) => MS k-> k
msGetMax (storage, size) = fst $ M.findMax storage



addElement :: (Eq k, Ord k) =>  k -> MedianMS k-> MedianMS k
addElement e (small, big)
    | getSize small == 0 &&  getSize big == 0 =
        (msInsert e small, big)
    | getSize small == getSize big =
        if e >= msGetMax small
        then (small, msInsert e big)
        else (msInsert e small, big)
    | getSize small >  getSize big =
        let ee = msGetMax small
        in if e >= ee
           then (small, msInsert e big)
           else (msInsert e (msErase ee small), msInsert ee big)
    | otherwise                    =
        let ee = msGetMin big
        in if e <= ee
           then (msInsert e small, big)
           else (msInsert ee small, msInsert e (msErase ee big))

delElement :: (Eq k, Ord k) => k -> MedianMS k -> MedianMS k
delElement e (small, big)
    | not (msContains e small) &&
      not (msContains e big)       = (small, big)
    | getSize small == getSize big =
        if msContains e small
        then (msErase e small, big)
        else (small, msErase e big)
    | getSize small >  getSize big =
        let ee = msGetMax small
        in if msContains e small
           then (msErase e small, big)
           else (msErase ee small, msInsert ee (msErase e big))
    | otherwise                    =
        let ee = msGetMin big
        in if msContains e big
           then (small, msErase e big)
           else (msInsert ee (msErase e small), msErase ee big)

queryMedian :: MedianMS Int-> String
queryMedian (small, big)
    | getSize small == 0 && getSize big == 0 = "Wrong!"
    | getSize small >  getSize big           = show $ msGetMax small
    | getSize small <  getSize big           = show $ msGetMin big
    | otherwise                              =
        let s1 = msGetMax small
            s2 = msGetMin big
        in if (s1 + s2) `mod` 2 == 0
           then show $ (s1 + s2) `div` 2
           else printf "%.1f" (fromIntegral (s1 + s2) / 2 :: Double)

solve :: [(String, Int)] -> [String]
solve xs = aux xs ((M.empty, 0), (M.empty, 0)) []
    where
      aux :: [(String, Int)] -> MedianMS Int -> [String] -> [String]
      aux [] _ acc = reverse acc
      aux ((op, v):xs') mms acc =
          if op == "a"
          then let nmms = addElement v mms
                   val  = queryMedian nmms
               in aux xs' nmms (val : acc)
          else if not (msContains v (fst mms)) && not (msContains v (snd mms))
               then aux xs' mms ("Wrong!" : acc)
               else let nmms   = delElement v mms
                        median = queryMedian nmms
                    in aux xs' nmms (median : acc)


readInt' :: BS.ByteString -> Int
readInt' = fst . fromJust . BS.readInt

main = do
  _ <- BS.getLine
  content <- lines <$> getContents
  let qs  = map ((\ [x, y] -> (x, read y :: Int)). words) content
      res = solve qs
  putStrLn $ L.intercalate "\n" res
