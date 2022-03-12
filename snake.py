from turtle import Turtle, Screen

#build snake body
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

class Snake:
    #builder
    def __init__(self):
         # save snake segments
        self.segments = []
        # method than created snake
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    def add_segment(self,position):
        snake_segment = Turtle("square")
        snake_segment.color("green")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    #snake initial position
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    #moving up
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    #moving down
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    #moving right
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    #moving left
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)