#maths mechanism
#head

from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send

from github.mauriceyap.art.check_winner import check_winner

#1The board

boardArray =[[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]] 
turn=1

def drop_counter(col,turn):
  for i in range (7,-1,-1):
    if boardArray [i][col]==0:
      boardArray [i][col] = turn
      return

print check_winner(boardArray)

#check winner
from tealight.art import *
def check_winner(boardArray):
  global winnerRed, winnerYellow
  
  winnerRed=0
  winnerYellow=0

  #1winnerchecker
  row = 0
  col = 0
  
  
  
  #2verticals
  for i in range (0,5):
    for i in range (0,8):
      if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==2:
        winnerYellow = 1
      col = col + 1
    col=0
    row = row+1
  
  row = 0
  col = 0
  
  #2horizontals
  for i in range (0,5):
    for i in range (0,8):
      if boardArray [row][col] ==boardArray [row][col+1]==boardArray [row][col+2]==boardArray [row][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row][col+1]==boardArray [row][col+2]==boardArray [row][col+3]==2:
        winnerYellow = 1
      row = row + 1
    row=0
    col=col+1
  
  row = 0
  col = 0
  
  #2diagonals positive
  
  row=3
  col=0
  
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
    
  row=4	
  col=0
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=5	
  col=0
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=6	
  col=0
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=7	
  col=0
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=3	
  col=1
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=4	
  col=1
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=5	
  col=1
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=6	
  col=1
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=7	
  col=1
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=3	
  col=2
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=4	
  col=2
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=5	
  col=2
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=6	
  col=2
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=7	
  col=2
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=3	
  col=3
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=4	
  col=3
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=5	
  col=3
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=6	
  col=3
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=7	
  col=3
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=3	
  col=4
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=4	
  col=4
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=5	
  col=4
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=6	
  col=4
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  row=7	
  col=4
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  #2diag neg
  
  row=0
  col=4
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=1
  col=4
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=2
  col=4
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=3
  col=4
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=4
  col=4
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=0
  col=3
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=1
  col=3
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=2
  col=3
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=3
  col=3
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=4
  col=3
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=0
  col=2
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=1
  col=2
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=2
  col=2
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=3
  col=2
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=4
  col=2
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=0
  col=1
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=1
  col=1
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=2
  col=1
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=3
  col=1
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=4
  col=1
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=0
  col=0
  
  for i in range (0,5):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=1
  col=0
  
  for i in range (0,4):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=2
  col=0
  
  for i in range (0,3):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=3
  col=0
  
  for i in range (0,2):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  row=4
  col=0
  
  for i in range (0,1):
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
        winnerRed = 1
  
      if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
        winnerYellow = 1
      row = row + 1
  
  
    
  
  
  row = 0
  col = 0
  
  
  
  
  #2declaration  
  if winnerRed == 1:
    print 'Red is the winner'
    color("red")
    spot(445,500,150)
  
    color("black")
    text(390,480,"Red Wins!!!")
    image(310,490,"misc/WhiteBalloon.png")
    image(325,400,"misc/BlackBalloon.png")
    image(375,360,"misc/BlueBalloon.png")
    image(450,360,"misc/GreenBalloon.png")
    image(375,540,"misc/OrangeBalloon.png")
    image(450,540,"misc/PinkBalloon.png")
    image(510,400,"misc/RedBalloon.png")
    image(510,510,"misc/YellowBalloon.png")
    return "red"
  if winnerYellow == 1:
    print 'Yellow is the winner'
    color("yellow")
    spot(445,500,150)

  
    color("black")
    text(390,480,"Yellow Wins!!!")
    image(310,490,"misc/WhiteBalloon.png")
    image(325,400,"misc/BlackBalloon.png")
    image(375,360,"misc/BlueBalloon.png")
    image(450,360,"misc/GreenBalloon.png")
    image(375,540,"misc/OrangeBalloon.png")
    image(450,540,"misc/PinkBalloon.png")
    image(510,400,"misc/RedBalloon.png")
    image(510,510,"misc/YellowBalloon.png")
    return "yellow"
  
  return None

#counters
from tealight.art import (color, line, spot, circle, box, image, text, background)

from github.mauriceyap.art.maths_mechanism import *


turn = 0
cell_size = 100

cells_x = 8
cells_y = 8

offset_x = 20
offset_y = 80

def handle_mousedown(x,y,button):
  global turn
  
  col = (x-offset_x) / cell_size
  
  if 0 <= col < 8:
    
    drop_counter(col,turn+1)
    
    turn = (turn + 1) % 2
    
    draw()
    
    
    
def draw():
  color("blue")
  box(offset_x,offset_y,cell_size * cells_x,cell_size * cells_y)
  
  width = 20
  height = 8
  
  for i in range(0,cells_x):
    for j in range(0,cells_y):
  
      if boardArray [j][i] == 0:
        color("white")
      elif boardArray[j][i] == 1:
        color("red")
      elif boardArray[j][i] == 2:
        color("yellow")
      
      spot(offset_x + i * cell_size + cell_size/2, offset_y + j * cell_size + cell_size/2, cell_size *0.4)
  
  check_winner(boardArray)

draw()