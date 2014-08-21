from tealight.art import (color, line, spot, circle, box, image, text, background)


def handle_mousedown(x,y):
  color("red")
  spot(x,y,10)
  
def handle_mousemove(x,y,right):
  if button == "right":
    color("red")
    circle(x,y,10)
 
