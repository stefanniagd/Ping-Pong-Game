from turtle import Turtle
STEP = 20
class Paddle(Turtle):

    def __init__(self, coordinates,):  #attributes
        super().__init__()
        self.penup()
        #self.speed("fastest") # Check without it
        self.goto(coordinates) # Where my paddle starts
        self.shape("square") #name -a string which is a valid shape name
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=None, stretch_len=5) # Default 20x20 wid

        # stretch_wid is stretch_factor perpendicular to its orientation,
        # stretch_len is stretch_factor in direction of its orientation,
        # outline determines the width of the shape’s outline.


    def up(self):
        self.forward(STEP)

    def down(self):
        self.backward(STEP)


