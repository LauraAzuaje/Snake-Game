from cgitb import text
from turtle import Turtle

class Score(Turtle):
    #Score builder
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    #Score text style
    def update_score(self):
        self.write(f"Score: {self.score}", font=("Arial",20, "normal"), align="center")

    #score sum
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    #score text style game over
    def game_over(self):
        self.clear()
        self.write("GAME OVER", font=("Arial",20, "normal"), align="center")
