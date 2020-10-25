import turtle   # import turtle library
import random   # import random library
import math   # import math library

# create turtle object for obstacle
don = turtle.Turtle()
don.speed(10)
don.width(3)

# create turtle object for obstacle
don_2 = turtle.Turtle()
don_2.speed(10)
don_2.width(3)

t = turtle.Turtle()   # create turtle object for main character
w = turtle.Turtle()   # create turtle object for writing

# sets the screen up
screen = don.getscreen()
screen.setup(500,500)
screen.bgcolor('cyan')
screen.tracer(0)    # tell screen to not show automatically

# creates an object for the screen and gets its to listen for changes
screen_list = turtle.Screen()
screen_list.listen()

def draw_circle(radius):
  '''function to draw circle with a radius parameter and fills it in'''
  don.fillcolor('green')
  don.begin_fill()
  don.circle(radius)
  don.end_fill()

def draw_circle_2(radius):
  '''function to draw circle with a radius parameter and fills it in'''
  don_2.fillcolor('red')
  don_2.begin_fill()
  don_2.circle(radius)
  don_2.end_fill()

# assigns how much the circle is going to move through each loop
x_direct = -5
y_direct = 0

# we'll represent the properties of our villain object using a dictionary
villain = {  
  "x" : -200,
  "y" : 0,
  "size": 25,
  "color" : "yellow",
  "speed" : 2
}

def move_up():
  '''function to constantly create the circle and move the turtle up'''
  for i in range(25):   # loop to draw and keep the circle moving
    t.clear()
    draw_villain()
    t.update()
    villain["y"] += villain["speed"]    #change the villain's y property

def move_down():
  '''function to constantly create the circle and move the turtle down'''
  for i in range(25):   # loop to draw and keep the circle moving
    t.clear()
    draw_villain()
    t.update()
    villain["y"] -= villain["speed"]    #change the villain's y property

def draw_villain():
  '''draw the villain, using its properties'''
  t.penup()
  t.goto(villain["x"], villain["y"])    # gets the postion of the circle for villian
  t.pendown()
  t.pencolor('violet')
  t.fillcolor(villain['color'])
  t.begin_fill()
  t.circle(villain["size"])   # sets the size of the circle by getting the size variable from villian
  t.end_fill()

def run_game():
  '''game function to let the whole program run through'''

  # initializes lives and points of player
  lives = 3
  points = 0

  update_info(lives, points)    # function is called to update info on screen

  # sets initial point for obstacle to appear
  x_1 = 300
  y_1 = 150

  # sets initial point for obstacle to appear
  x_2 = 300
  y_2 = -150

  # loop to keep circle moving through each iteration
  while True:
    # clears everything in turtle don
    don.clear()
    don_2.clear()

    # calls dar_circle function with radius 50
    draw_circle(25)
    draw_circle_2(25)

    # starts initial position of circle to the (x, y) positions for movement
    x_1 += x_direct
    x_2 += x_direct

    don.hideturtle()    # hide don turtle
    don_2.hideturtle()    # hide don 2 turtle

    # resets the obstacle to come back from the right right side with a different y coordinate
    if x_1 == -300:
      x_1 = 300
      y_1 = random.randint(-200, 200)

    # resets the obstacle to come back from the right right side with a different y coordinate
    if x_2 == -300:
      x_2 = 300
      y_2 = random.randint(-200, 200)

    screen.update()   # only now show the screen, as one of the frames

    # starts initial movement of circle and then keeps it moving through each iteration of the loop
    don.goto(x_1, y_1)
    don_2.goto(x_2, y_2)

    t.hideturtle()    # hide the turtle so only the circle can be seen

    # listens to the key presses
    screen_list.onkey(move_up, "Up")
    screen_list.onkey(move_down, "Down")

    # https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection 
    dx = villain['x'] - x_1
    dy = villain['y'] - y_1
    distance = math.sqrt(dx * dx + dy * dy)

    dx_2 = villain['x'] - x_2
    dy_2 = villain['y'] - y_2
    distance_2 = math.sqrt(dx_2 * dx_2 + dy_2 * dy_2)

    # condition to check if main character touched red object making the player lose a life and circle to be reset to the right if condition is met
    if (distance_2 < villain["size"] + 25):
      x_2 = 300
      y_2 = random.randint(-200, 200)
      lives -= 1
      update_info(lives, points)
      if lives == 0:
        update_info(lives, points)
        w.penup()
        w.goto(0, 0)
        w.write('GAME OVER')    # prints GAME OVER to the screen once game has been lost
        break   # breaks out of loop because the game is over

    # condition to check if main character touched green object making the player gain a point and circle to be reset to the right if condition is met  
    if (distance < villain['size'] + 25):
      x_1 = 300
      y_1 = random.randint(-200, 200)
      points += 1
      update_info(lives, points)

def update_info(lives, points):
  '''function to keep updating info on page'''
  w.clear()
  w.hideturtle()
  w.penup()
  w.goto(-150, -150)
  w.write('Lives: ' + str(lives))
  w.penup()
  w.goto(-150, -160)
  w.write('Points: ' + str(points))

def main():
  '''main function to run the game'''
  run_game()

main()    # main function is called to run the game