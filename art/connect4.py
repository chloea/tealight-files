from tealight.art import (color, line, spot, box, image, text, background)



 
def handle_mousedown(x,y):
  color("red")
  spot(x,y,50)
  
def handle_mousemove(x,y,button):
  if button == "right":
    color("yellow")
    spot(x,y,50)
  
  
