import Text.Printf
import Data.Maybe
import qualified Data.List as L


type Stack a = [a]

isEmpty = null

push = (:)

pop = tail

top = head

eps = 1e-10

doubleCmp :: Double -> Double -> Ordering
doubleCmp a b
    | a - b < -eps = LT
    | abs (a - b) < eps = EQ
    | True = GT

data Point = Point Double Double deriving (Show, Eq)
data Driection = Straight | TurnLeft | TurnRight deriving (Show, Eq)

instance Num Point where
    (Point x1 y1) + (Point x2 y2) = (Point (x1 + x2) (y1 + y2))
    (Point x1 y1) - (Point x2 y2) = (Point (x1 - x2) (y1 - y2))
    abs (Point x1 y1) = Point (abs x1) (abs y1)
    fromInteger = undefined
    (*) = undefined
    signum = undefined
    
dist :: Point -> Point -> Double
dist (Point x1 y1) (Point x2 y2) = sqrt $ (x1 - x2) ** 2 + (y1 - y2) ** 2

-- | This function calculate cross product of vector V1 and V2
cross :: Point -> Point -> Double
cross (Point x1 y1) (Point x2 y2) = x1 * y2 - x2 * y1

-- | This function judge whether the vector P1P2 P2P3 is counter-clock-wise
ccw :: Point -> Point -> Point -> Bool
ccw p1 p2 p3 = (doubleCmp (cross (p2 - p1) (p3 - p2)) (fromIntegral 0)) /= LT

-- | Compare two point by their y coordinate, if they're equal than calculat
--   THen compare their x coordinate
compareY :: Point -> Point -> Ordering
compareY (Point x1 y1) (Point x2 y2) = 
    if (doubleCmp y1 y2) == EQ then doubleCmp x1 x2 else doubleCmp y1 y2
    
-- | Return ordering of the two points' angles with the first one as origin
--   If the two points are of the same angles, compare between their distance
--   to the point pvt, and place the one with longer distance first.
compareAngle :: Point -> Point -> Point -> Ordering
compareAngle pvt@(Point x y) p1@(Point x1 y1) p2@(Point x2 y2) = 
    if angle == EQ then distance else angle
    where
        angle = doubleCmp (cross (p1 - pvt) (p2 - pvt)) 0
        distance = doubleCmp (dist pvt p2) (dist pvt p1)
        

grahamScan :: [Point] -> [Point]
grahamScan ps = aux (drop 2 points8Angle) (reverse $ take 2 points8Angle)
    where
        aux [] stack = stack
        aux (x:xs) [s] = aux xs [x, s]
        aux (x:xs) stack = if ccw x (top stack) (top (pop stack)) then
                                aux xs (push x stack)
                           else aux (x:xs) (pop stack)
        p = L.minimumBy compareY ps
        points8Angle = p : L.sortBy (compareAngle p) (L.delete p (L.nub ps))

solve :: [(Double, Double)] -> Double
solve points = 
    let ps = map (uncurry Point) points
        convex = grahamScan ps
    in sum $ (map (\(p1, p2) -> dist p1 p2) 
        (zip convex (drop 1 (cycle convex))))


main :: IO ()
main = do
  n <- readLn :: IO Int
  content <- getContents
  let
    points = map (\[x, y] -> (x, y)).
             map (map (read::String->Double)). map words. lines $ content
    ans = solve points
  printf "%.1f\n" ans
