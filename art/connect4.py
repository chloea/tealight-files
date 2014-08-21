from tealight.art import (color, line,circle, spot, box, image, text, background)

n=0

 
def handle_mousedown(x,y,button):
  if button == "left":
    color("red")
    spot(x,y,40)
  elif button == "right":
    color("yellow")
    spot (x,y,40)
  


while n<64:
 def handle_mousemove(x,y,button):
  if button == 'right':
    turn = 2
    color("red")
    spot(x,y,40)
  elif button == 'left':
    color("yellow")
    spot(x,y,40)
    turn = 1
  n=n+1
  
#if turn = 1:


