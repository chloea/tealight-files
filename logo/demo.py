from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue", "purple"]

for i in range(0,550):
  move(i)
  turn(600)
  color(colors[i%3])