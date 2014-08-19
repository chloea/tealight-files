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
    
go ()

