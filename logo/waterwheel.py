from tealight.logo import move, turn


def triangle(side):
  for i in range(0,3):
    move(side)
    turn(125)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size /3
  for i in range(0, edges):
    move(size)
    triangle(decoration)
    turn(angle)

turn(-90)
waterwheel(35,90)
