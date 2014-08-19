from tealight.logo import move, turn


def triangle(side):
  for i in range(0,6):
    move(side)
    turn(90)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size /6
  for i in range(0, edges):
    move(size)
    triangle(decoration)
    turn(angle)

turn(-90)
waterwheel(30,100)
