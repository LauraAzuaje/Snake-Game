from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from score import Score

# board game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
#disable default Turtle animation
screen.tracer(0)

snake = Snake()

#Object food
food = Food()

#Object score
score = Score()

#Metodo de escucha
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

#snake animation
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect colisions food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    #Detect colisions pared
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    #Detect colisions segment snake
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()