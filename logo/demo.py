from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "pink", "blue", "pink"]

for i in range(0,550):
  move(i)
  turn(360)
  color(colors[i%3])