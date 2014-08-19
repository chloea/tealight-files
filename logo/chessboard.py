from tealight.logo import (move, 
                           turn, 
                           color)
def square (edges, size)
   angle = 360 / edges
   for i in range(0, edges):
     move(size)
     turn(angle)
      
polygon(4, 50)