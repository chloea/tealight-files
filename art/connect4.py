from tealight.art import (color, line, spot, circle, box, image, text, background)



 
def handle_mousedown(x,y):
  color("red")
  spot(x,y,50)
  
def handle_mousemove(x,y,button):
  if button == "right":
    color("yellow")
    circle(x,y,50)
  
  
