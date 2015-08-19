import           Control.Applicative
import qualified Data.ByteString.Char8 as BS
import qualified Data.List             as L
import qualified Data.Map              as M
import           Data.Maybe
import           Text.Printf

{-
  Multiple set implement using tree in haskell. It is guarantee that the
  msInsert, msErase, msContains operaion run in O(n log n) time complexity.
 -}

-- | The first map is used as storage, and the second Int record the number
-- | in the multiset
type MS k = (M.Map k Int ,Int)

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


main :: IO ()
main = putStrLn "hello world"
