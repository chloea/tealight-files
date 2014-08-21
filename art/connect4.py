from tealight.art import (color, line, spot, circle, box, image, text, background)



def handle_mousedown(x,y,button):
  color("red")
  spot(x,y,50)