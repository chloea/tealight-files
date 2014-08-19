from tealight.logo import (move, 
                           turn, 
                           color)
def square(edges, size, colour):
   angle = 360 / edges
   for i in range(0, edges):
     move(size)
     turn(angle)
      
square(4, 200, blue)


