-- advent2015_01.hs

module Advent201501 where

move :: Char -> Int
move '(' = 1
move ')' = (-1)

santa :: String -> Int
santa "" = 0
santa x = 
  santa y + move h
  where y =
          tail x
        h = 
          head x

santa1 :: (String, Int, Int) -> (String, Int, Int)
santa1 ("",fl,steps) = ("",fl,steps)
santa1 (x,fl,steps)=
  if fl==(-1)
    then ("ok",fl,steps)
  else
    santa1 (a,b,c)
    where a=
            tail x
          b=
            fl + move (head x)
          c=
            steps + 1