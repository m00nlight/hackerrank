import Text.Parsec
import Text.Parsec.Expr
import Text.Parsec.Combinator
import Data.Functor

data Exp = Num Int
         | Add Exp Exp
         | Sub Exp Exp
         | Mul Exp Exp
         | Div Exp Exp
         | Pos Exp
         | Neg Exp

expr = buildExpressionParser table factor <?> "expr"


table = [[prefix "-" (Neg), prefix "+" (Pos)]
        ,[op "*" (Mul) AssocRight, op "/" (Div) AssocRight]
        ,[op "+" (Add) AssocRight, op "-" (Sub) AssocRight]]
    where op s f assoc = Infix (f <$ string s) assoc
          prefix s f = Prefix (f <$ string s)


factor = between (char '(') (char ')') expr
         <|> (Num . read <$> many1 digit) <?> "factor"

-- propMod :: Integral a => a -> a -> a
propMod a m = (a `mod` m + m) `mod` m

-- evaluate a^b % m fastly
powMod a b m
      | b == 0     = 1
      | b == 1     = propMod a m
      | otherwise  =
          let
              tmp         = powMod a (b `div` 2) m
          in if b `mod` 2 == 0
             then propMod (tmp * tmp) m
             else propMod (tmp * tmp * a) m

modinv a p = powMod a (p - 2) p

modulo = 1000000007 :: Integer

-- eval :: (Num a, Integral a) => Exp -> a
eval e = case e of
    Num x   -> propMod (fromIntegral x) modulo
    Pos a   -> propMod (eval a) modulo
    Neg a   -> propMod (negate $ eval a) modulo
    Add a b -> propMod (eval a + eval b) modulo
    Sub a b -> propMod (eval a - eval b) modulo
    Mul a b -> propMod (eval a * eval b) modulo
    Div a b -> propMod ((eval a) * (modinv (eval b) modulo)) modulo

-- solution :: (Num a, Integral a) => String -> a
solution = either (error . show) eval . parse expr ""


main = do
  line <- getLine
  putStrLn $ show $ solution (filter (/=' ') line)
