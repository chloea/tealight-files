from tealight.logo import (move, 
                           turn, 
                           color)
colours= ("blue", "red")

def square(edges, size, colour):
   angle = 360 / edges
   for i in range(0, edges):
     move(size)
     turn(angle)
      
square(4, 200, "blue")
square(2,100,"red")


