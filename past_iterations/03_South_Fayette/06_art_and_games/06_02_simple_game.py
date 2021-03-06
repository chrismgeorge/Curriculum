from tkinter import *
from random import randint

# the game data for the initial game state
def init():
  data.playerX = 400
  data.playerY = 300
  data.winSpotX = 450
  data.winSpotY = 450
  data.gameOver = False

# events updating the game data
def keyPressed(event):
  key = event.keysym
  if key == "Right":
    data.playerX += 5
  elif key == "Left":
    data.playerX -= 5
  elif key == "Up":
    data.playerY -= 5
  elif key == "Down":
    data.playerY += 5

# the game data updating the game state
def timerFired():
  if playerAtWinSpot():
    data.gameOver = True

def playerAtWinSpot():
  xDist = data.playerX - data.winSpotX
  yDist = data.playerY - data.winSpotY
  distApart = (xDist**2 + yDist**2)**0.5
  closeDist = 50
  return distApart < closeDist

# the game state updating what is drawn
def redrawAll(canvas):
  canvas.create_oval(data.playerX - 10, data.playerY - 10, 
                     data.playerX + 10, data.playerY + 10,
                     fill="red")
  if (data.gameOver):
    winSpotText = "YOU WIN"
  else:
    winSpotText = "Move here"
  canvas.create_text(data.winSpotX, data.winSpotY,
                     text=winSpotText, font="Arial 20",
                     anchor="center")


# Challenge 2.1 - Run the file to get an idea of what it does.
#    Then, change the player from a small red circle to be a big blue square.

# Challenge 2.2 - Make the controls WACKY!  Make left go up, right go down,
#    down go right, and up go left.

# Challenge 2.3 - Change the location of the text to be the top left corner
#    of the screen.

# BONUS TAKE-HOME Challenge - Make it more game-like by adding some more game
#    mechanics:
#      1. Make the text move once you reach it to a random spot on the screen.
#      2. Make it so once you get to the text five times you win.
#      3. Make it so if you don't reach the text within a certain time you lose.


# animation setup code below here #

class Struct(object): pass
data = Struct()

def run(width=600, height=600):
  def redrawAllWrapper(canvas):
    canvas.delete(ALL)
    redrawAll(canvas)
    canvas.update()    

  def keyPressedWrapper(event, canvas):
    keyPressed(event)
    redrawAllWrapper(canvas)

  def timerFiredWrapper(canvas):
    timerFired()
    redrawAllWrapper(canvas)
    # pause, then call timerFired again
    canvas.after(data.timerDelay, timerFiredWrapper, canvas)

  # Set up data and call init
  data.width = width
  data.height = height
  data.timerDelay = 200 # milliseconds
  init()
  # create the root and the canvas
  root = Tk()
  canvas = Canvas(root, width=data.width, height=data.height)
  canvas.pack()
  # set up events
  root.bind("<Key>", lambda event:
                          keyPressedWrapper(event, canvas))
  timerFiredWrapper(canvas)
  # and launch the app
  root.mainloop()  # blocks until window is closed
  print("bye!")

run()
