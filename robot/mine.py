from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def go():
  moved=0
  while touch () == "wall":
    move ()
    moved=moved +1

turn (1)
if touch ()== "wall":
  go()

turn (1)
if touch () == "wall":
  for n in range (4):
    move()

turn (1)
move ()


 

    
go ()
