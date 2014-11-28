from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "balck", "blue", "black"]

for i in range(0,550):
  move(i)
  turn(8)
  color(colors[i%3])