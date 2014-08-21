from tealight.art import (color, line,circle, spot, box, image, text, background)
turn = 2
def n(int):
  if n/2 != int:
    turn=1
  elif n/2 == int:
    turn=2
 
def handle_mousedown(x,y,button):
  if button == "left" and turn ==1:
    color("red")
    spot(x,y,40)
  elif button == "left" and turn ==2:
    color("yellow")
    spot (x,y,40)
    
    
#def do_stuff(turn):
 # if n =
  


#while n<64:
 #def handle_mousemove(x,y,button):
  #if button == 'right':
   # turn = 2
    #color("red")
    #spot(x,y,40)
  #elif button == 'left':
    #color("yellow")
    #spot(x,y,40)
    #turn = 1
  #n=n+1
  
#if turn = 1:


