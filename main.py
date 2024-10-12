from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_PADDLE_COORDINATE = (350,0)
L_PADDLE_COORDINATE = (-350,0)

Y_COORDINATE_UP_WALL = 270
Y_COORDINATE_DOWN_WALL = -270

# Set up the screen
screen = Screen()
screen.setup(width=800,height=600) #Set up the size
screen.bgcolor("Black") # Set background color of the TurtleScreen
screen.title("Pong Game") # Set title of the turtle window to .title(title_string)

screen.tracer(0) #Turn turtle animation on/off and set delay for update drawings
#Remeber-> When I turn off the tracer I need to manually update the screen and refresh it every single time
#           To do that we'll need some sort of while loop

#Create the objects paddles
r_paddle = Paddle(R_PADDLE_COORDINATE)
l_paddle = Paddle(L_PADDLE_COORDINATE)


#Create the object Ball
#ball = Ball()

#create the field
lines = Turtle()
lines.hideturtle()
lines.color("white")
lines.setheading(270)
lines.penup()
lines.goto(0,330)
for _ in range(0,31):
    lines.forward(20)
    lines.penup()
    lines.forward(20)
    lines.pendown()



scoreboard = Scoreboard()


screen.listen() # Set focus on TurtleScreen (in order to collect key-events).
#Keyboard for right paddle
screen.onkey(fun = r_paddle.up,key="Up") # I need to use this here because first I need to create the object and the use the method
screen.onkey(fun = r_paddle.down, key="Down")

#Keyboard for left paddle
screen.onkey(fun = l_paddle.up,key="w")
screen.onkey(fun = l_paddle.down, key="s")


def play_game():
    time_game = 0.1
    ball = Ball()
    game_on = True
    while game_on:
        screen.update()   # What happens is: 1-The animations gets turned off
                          #                  2-paddle then gets created in the background and the ball
                          #                  3-The screen is updated and show everything that happened in the background so far

        time.sleep(time_game)
        #Move the ball
        ball.move()

        #Detect collision with a wall and bounce_y
        if ball.ycor() > Y_COORDINATE_UP_WALL:
            if ball.heading() <= 90:  # 1_quartet
                ball.change_direction_to_4_quartet()
            elif ball.heading() <=180:
                ball.change_direction_to_3_quartet()


        if ball.ycor() < Y_COORDINATE_DOWN_WALL:
            if 180 <= ball.heading() <= 270:
                ball.change_direction_to_2_quartet()
            if 270 < ball.heading() <=360:
                ball.change_direction_to_1_quartet()


        # Detect collision with the paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() >= 330:
            if ball.heading() <= 90:
                ball.setheading(ball.heading()+90)
            if 270 < ball.heading() <=360:
                ball.setheading(ball.heading() - 90)
            time_game *= 0.9


        if ball.distance(l_paddle) < 50 and ball.xcor() <= -330:
            if 90 <= ball.heading() <=180:
                ball.setheading(ball.heading()-90)
            if 180 < ball.heading() <=270:
                ball.setheading(ball.heading() + 90)
            time_game *= 0.9

        #Detect when the right paddle misses a ball
        if ball.distance(r_paddle) > 50 and ball.xcor() >380:
            #Left player win a point
            scoreboard.l_point()
            # Restart the game
            print("You missed the ball")
            ball.hideturtle()
            time.sleep(0.3)
            play_game()

        # Detect when the left paddle  misses a ball
        if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
            # right player win a point
            scoreboard.r_point()
            # Restart the game
            print("You missed the ball")
            ball.hideturtle()
            time.sleep(0.3)
            play_game()




play_game()

#screen.update()






screen.exitonclick() # Bind bye() method to mouse clicks on the Screen