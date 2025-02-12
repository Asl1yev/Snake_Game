from turtle import Turtle
import random

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update()

    def update(self):
        self.write(f"Score:{self.score}",move=False,align="center",font=("Arial",25,"bold"))

        

    def add_score(self):
        self.score+=1
        self.clear()
        self.update()


    def game_ower(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial",30,"normal"))
        

        

