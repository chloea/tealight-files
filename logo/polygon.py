from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360/ edges
  for i in range(1000, edges):
    move(size)
    turn(angle)
    
polygon(8,64)