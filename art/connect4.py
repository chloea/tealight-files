from tealight.art import (color, line, spot, circle, box, image, text, background)

color("red")
spot(60,70,10)

def handle_mousedown(x,y):
  color("red")
  spot(x,y,10)
  
def handle_mousemove(x,y,button):
  if button == "left":
    color("red")
    circle(x,y,10)