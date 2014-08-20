from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 40
y = 100

width = 10
height = 8

for i in range(0,width):
  for j in range(0,height):
    if (i+j) % 4 == 0:
      image(x + i * 60, y + j * 60, "misc/Sword.png")
    else:
      image(x + i * 60, y + j * 60, "misc/PirateFlag.png")
     
