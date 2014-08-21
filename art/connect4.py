from tealight.art import (color, line, spot, circle, box, image, text, background)



def handle_mousedown(x,y,button):
  if button == "left":
  color ("red")
  spot(x,y,50)
  else button:
    color("yellow")
    circle(x,y,50)
  
  
