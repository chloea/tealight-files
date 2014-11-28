from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# This is a fairly useless algorithm!

while True:
  move()
  turn(right_side)
  
  if touch() == "wall":
    turn(2)
    
