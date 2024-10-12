from turtle import Turtle
import random

DEGREES_OF_REDUCTION = 30

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.setheading(random.randrange(start=5,stop=359)) #Return a randomly selected element from range(start, stop, step).
        # I need to remove some values--- 0. 90,180,270

    def move(self):
        self.forward(20)



# I Quartet

    def change_direction_to_4_quartet(self):
        #heading = int(self.heading())
        #angle = 360 - heading #Stop ---> it is not necessary
        #50% of 270grades and 360 to have a good effect
        self.setheading(random.randrange(start=int(270+DEGREES_OF_REDUCTION),stop=int(360-DEGREES_OF_REDUCTION)))
        #print(self.heading()) ---> Just for checking the heading

# II Quartet
    def change_direction_to_3_quartet(self):
        #heading = int(self.heading())
        #print(f"This is the initial heading {self.heading()}") ---> Just for checking the heading
        #angle = 360 - heading #Stop---> it is not necessary
        # 50% of 270grades and 360 to have a good effect
        self.setheading(random.randrange(start=int(180+DEGREES_OF_REDUCTION),stop=int(270-DEGREES_OF_REDUCTION)))


# III Quartet
    def change_direction_to_2_quartet(self):
        #heading = int(self.heading())
        #angle = 360 - heading  # Stop---> it is not necessary
        self.setheading(random.randrange(start=90+DEGREES_OF_REDUCTION, stop=180-DEGREES_OF_REDUCTION))
        #print(self.heading()) ---> Just for checking the heading

# IV Quartet

    def change_direction_to_1_quartet(self):
        #heading = int(self.heading())
        #angle = 360 - heading  # Stop
        self.setheading(random.randrange(start=30, stop=90-DEGREES_OF_REDUCTION))
        #print(self.heading())  ---> Just for checking the heading

    def disappear(self):
        self.hideturtle()

    def restart_position(self):
        self.goto(0,0)


