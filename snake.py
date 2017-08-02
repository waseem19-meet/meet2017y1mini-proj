import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window

#size.

turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 5
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stampID=snake.stamp()
    stamp_list.append(stampID)

UP_ARROW = "Up" #Make sure you pay attention to upper and lower

#case

LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many

#milliseconds

SPACEBAR = "space" # Careful, it's not supposed to be capitalized!
UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN=1
LEFT=2
RIGHT=3
direction=UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def up():
    global direction
    direction=UP
    print("you pressed up key!")
def down():
    global direction
    direction=DOWN
    print("you pressed down key!")
def right():
    global direction
    direction=RIGHT
    print("you pressed right key!")
def left():
    global direction
    direction=LEFT
    print("you pressed left key!")

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)

turtle.listen()

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food_turtle_pos=(food_x,food_y)
    food.goto(food_x,food_y)
    food_pos.append(food_turtle_pos)
    food_stamps.append(food.stamp())
    

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up!")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        #print("You moved down!")
#4. Write the conditions for UP and DOWN on your own
##### YOUR CODE HERE
#Stamp new element and append new stamp in list
#Remember: The snake position changed - update my_pos()
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        make_food()
#HINT: This if statement may be useful for Part 8
#Don't change the rest of the code in move_snake() function:
#If you have included the timer so the snake moves
#automatically, the function should finish as before with a
#call to ontimer()
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    if new_x_pos>=RIGHT_EDGE:
        print("You hit the right edge! Game Over!")
        quit()
    elif new_x_pos<=LEFT_EDGE:
        print("You hit the left edge! Game Over!")
        quit()
    if new_y_pos>=UP_EDGE:
        print("you hit the up edge!Game Over!")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("you hit the down edge!Game Over!")
        quit()

    turtle.ontimer(move_snake,TIME_STEP)

move_snake()

turtle.register_shape("trash.gif") #Add trash picture

# Make sure you have downloaded this shape
# from the Google Drive folder and saved it
# in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif")
food.hideturtle()
#Locations of food
food_pos = [(100,100)]
# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append( )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
####WRITE YOUR CODE HERE!!
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())
    
if pos_list() in stamp_list():
    print("Game Over!")
    
