from tealight.art import (color, line, spot, circle, box, image, text, background)

def handle_mousedown(x,y):
  color("yellow")
  spot(x,y,200)
  
def handle_mousemove(x,y,button):
  if button == "left":
    color("green")
    circle(x,y,200)