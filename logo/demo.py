from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue", "purple"]

for i in range(0,500):
  move(i)
  turn(666)
  color(colors[i%3])