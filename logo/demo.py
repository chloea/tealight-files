from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue", "purple"]

for i in range(0,750):
  move(i)
  turn(450)
  color(colors[i%3])