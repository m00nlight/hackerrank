import           Control.Monad
import qualified Data.Map                               as M
import           Text.ParserCombinators.Parsec
import           Text.ParserCombinators.Parsec.Expr
import           Text.ParserCombinators.Parsec.Language
import qualified Text.ParserCombinators.Parsec.Token    as Token



data BExpr = BoolConst Bool
           | Not BExpr
           | BBinary BBinOp BExpr BExpr
           | RBinary RBinOp AExpr AExpr
             deriving (Show)

data BBinOp = And | Or deriving (Show)

data AExpr = Var String
           | IntConst Integer
           | Neg AExpr
           | ABinary ABinOp AExpr AExpr
             deriving (Show)

data ABinOp = Add | Subtract | Multiply | Divide deriving (Show)

data RBinOp = Greater | Less deriving (Show)

data Stmt = Seq [Stmt]
          | Assign String AExpr
          | If BExpr Stmt Stmt
          | While BExpr Stmt
          | Skip
            deriving (Show)

type Env = M.Map String Integer

evalA :: AExpr -> Env -> Integer
evalA (Var v) env = M.findWithDefault 0 v env
evalA (IntConst n) _ = n
evalA (Neg e) env = -(evalA e env)
evalA (ABinary op e1 e2) env =
    case op of
      Add -> evalA e1 env + evalA e2 env
      Subtract -> evalA e1 env - evalA e2 env
      Multiply -> evalA e1 env * evalA e2 env
      Divide -> (evalA e1 env) `div` (evalA e2 env)

evalB :: BExpr -> Env -> Bool
evalB (BoolConst b) _ = b
evalB (Not e) env = not $ evalB e env
evalB (BBinary op e1 e2) env =
    case op of
      And -> evalB e1 env && evalB e2 env
      _ -> evalB e1 env || evalB e2 env
evalB (RBinary op e1 e2) env =
    case op of
      Greater -> evalA e1 env > evalA e2 env
      _ -> evalA e1 env < evalA e2 env

interpreter :: Stmt -> Env -> Env
interpreter (Assign v expr) env = M.insert v (evalA expr env) env
interpreter (Seq []) env = env
interpreter (Seq (x:xs)) env = interpreter (Seq xs) (interpreter x env)
interpreter (If e st1 st2) env
    | evalB e env = interpreter st1 env
    | otherwise = interpreter st2 env
interpreter (While e st) env
    | not (evalB e env) = env
    | otherwise = interpreter (While e st) newEnv
    where
      newEnv = interpreter st env

languageDef =
    emptyDef { Token.commentStart = "{-"
             , Token.commentEnd = "-}"
             , Token.commentLine = "//"
             , Token.identStart = letter
             , Token.identLetter = alphaNum
             , Token.reservedNames = [ "if"
                                     , "then"
                                     , "else"
                                     , "while"
                                     , "do"
                                     , "skip"
                                     , "true"
                                     , "false"
                                     , "not"
                                     , "and"
                                     , "or"
                                     ]
             , Token.reservedOpNames = [ "+", "-", "*", "/", ":="
                                       , "<", ">", "and", "or", "not"
                                       ]
             }

lexer = Token.makeTokenParser languageDef

identifier = Token.identifier lexer
reserved = Token.reserved lexer
reservedOp = Token.reservedOp lexer
parens = Token.parens lexer
braces = Token.braces lexer
integer = Token.integer lexer
semi = Token.semi lexer
whiteSpace = Token.whiteSpace lexer

whileParser :: Parser Stmt
whileParser = whiteSpace >> statement

statement :: Parser Stmt
statement = braces statement
           <|> sequenceOfStmt

sequenceOfStmt =
    do list <- (sepBy1 statment' semi)
       return $ if length list == 1 then head list else Seq list

statment' :: Parser Stmt
statment' = ifStmt
            <|> whileStmt
            <|> skipStmt
            <|> assignStmt

ifStmt :: Parser Stmt
ifStmt =
    do reserved "if"
       cond <- bExpression
       reserved "then"
       stmt1 <- statement
       reserved "else"
       stmt2 <- statement
       return $ If cond stmt1 stmt2

whileStmt :: Parser Stmt
whileStmt =
    do reserved "while"
       cond <- bExpression
       reserved "do"
       stmt <- statement
       return $ While cond stmt

assignStmt :: Parser Stmt
assignStmt =
    do var <- identifier
       reservedOp ":="
       expr <- aExpression
       return $ Assign var expr

skipStmt :: Parser Stmt
skipStmt = reserved "skip" >> return Skip

aExpression :: Parser AExpr
aExpression = buildExpressionParser aOperators aTerm

bExpression :: Parser BExpr
bExpression = buildExpressionParser bOperators bTerm

aOperators = [ [Prefix (reservedOp "-" >> return (Neg ))]
            , [Infix (reservedOp "/" >> return (ABinary Divide )) AssocLeft,
               Infix (reservedOp "*" >> return (ABinary Multiply )) AssocLeft]
            , [Infix (reservedOp "+" >> return (ABinary Add )) AssocLeft,
               Infix (reservedOp "-" >> return (ABinary Subtract )) AssocLeft]
            ]


bOperators = [ [Prefix (reservedOp "not" >> return (Not  )) ]
             , [Infix (reservedOp "and" >> return (BBinary And )) AssocLeft,
                Infix (reservedOp "or" >> return (BBinary Or )) AssocLeft]
             ]


aTerm = parens aExpression
        <|> liftM Var identifier
        <|> liftM IntConst integer


bTerm = parens bExpression
        <|> (reserved "true" >> return (BoolConst True))
        <|> (reserved "false" >> return (BoolConst False))
        <|> rExpression

rExpression =
    do a1 <- aExpression
       op <- relation
       a2 <- aExpression
       return $ RBinary op a1 a2

relation = (reservedOp ">" >> return Greater)
           <|> (reservedOp "<" >> return Less)

parseString :: String -> Stmt
parseString str =
    case parse whileParser "" str of
      Left e -> error $ show e
      Right r -> r

parseFile :: String -> IO Stmt
parseFile file =
    do program <- readFile file
       case parse whileParser "" program of
         Left e -> print e >> fail "parser error"
         Right r -> return r


main = do
  program <- getContents
  let ast = parseString program
      res = M.toList $ interpreter ast M.empty
  mapM_ (\(x, y) -> putStrLn $ x ++ " " ++ (show y)) res
