from tealight.art import (color, line, spot, circle, box, image, text, background)

for x in range(0,54):
  for y in range(0,39):

    if y > x*x:
      color("red")
    elif y > x:
      color("green")
    elif y*y < x:
      color("orange")
    else:
      color("blue")
    
    box(x*20,y*15,10,10)
    
for x in range(55,100):
  for y in range(40,80):
    
    if y>x*x:
      image(x,y,"animals/Pterodactyl.png")
    elif y> x:
      image(x,y,"misc/Bomb.png") 
    elif y*y<x:
      image (x,y,"misc/RedBalloon.png")
    else:
      image(x,y,"food/CandyCane.png")
      
  
