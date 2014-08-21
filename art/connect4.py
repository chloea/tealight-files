from tealight.art import (color, line,circle, spot, box, image, text, background)
turn = 2

def add_counter(col):
  print "Adding counter to column " + str(col)
  

def handle_mousedown(x,y,button):
  global turn 
  if button == "left" and turn ==1:
    color("red")
    spot(x,y,45)
    turn =2
  elif button == "left" and turn ==2:
    color("yellow")
    spot (x,y,45)
    turn =1
    
#while add_counter(col):
  #if x < 150
   
    
    
    
color("green")    
line(145,0,145,100)
line(90,0,90,100)



#board
color("blue")
box(20,80,850,840)

x = 95
y = 150

width = 20
height = 8

for i in range(0,8):
  for j in range(0,8):
    if (i + j)%4 ==0:
      color("white")
      spot(x + i * 100, y + j * 100, 40)
    else:
      spot(x + i * 100, y + j * 100, 40)