from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue", "purple", "yellow"]

for i in range(0,500):
  move(i)
  turn(91)
  color(colors[i%3])