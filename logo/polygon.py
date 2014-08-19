from tealight.logo import move, turn

def circle(edges, size):
  angle = 360/ edges
  for i in range(3, edges):
    move(size)
    turn(angle)
    
circle(8,64)