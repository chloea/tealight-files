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
  turn(1)
  move()
  
  if touch() == "wall":
    turn(2)
    
