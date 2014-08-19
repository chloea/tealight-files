from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue", "orange"]

for i in range(0,550):
  move(i)
  turn(100)
  color(colors[i%3])