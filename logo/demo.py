from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue", "pink"]

for i in range(0,550):
  move(i)
  turn(180)
  color(colors[i%3])