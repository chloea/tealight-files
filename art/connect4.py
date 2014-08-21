from tealight.art import (color, line,circle, spot, box, image, text, background)
turn = 2





def handle_mousedown(x,y,button):
  global turn 
  if button == "left" and turn ==1:
    color("red")
    spot(x,y,40)
    turn =2
  elif button == "left" and turn ==2:
    color("yellow")
    spot (x,y,40)
    turn =1
    
    



