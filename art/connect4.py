from tealight.art import (color, line,circle, spot, box, image, text, background)
turn = 2

def add_counter(col):
  print "Adding counter to column " + str(col)
  

def handle_mousedown(x,y,button):
  global turn 
  
  add_counter(x)
  
  
  
  if button == "left" and turn ==1:
    color("red")
    spot(x,y,40)
    turn =2
  elif button == "left" and turn ==2:
    color("yellow")
    spot (x,y,40)
    turn =1
    
    



