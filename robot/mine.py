from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def go():
  moved=0
  while touch () == "fruit":
    move ()
    moved=moved +1

turn (1)
if touch ()== "fruit":
  go()

turn (1)
if touch () == "fruit":
  for n in range (4):
    move()

turn (1)
if touch ()== "fruit":
  for n in range (8):
   move ()

turn (-1)
while smell ()== "fruit":
    move ()

if touch ()== "wall":
  turn (1)
  if touch ()=="wall":


    

    
go ()
