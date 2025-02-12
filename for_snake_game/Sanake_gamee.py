from turtle import Turtle,Screen
import time
from food import Food
from score import Score
from snake_uz import Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        score.add_score()
    
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        score.game_ower()
        for segmant in snake.segments:
            if segmant == snake.segments[0]:
                pass
                if snake.segments[0].distance(segmant)<10:
                    game_is_on=False
                    score.game_ower()


screen.exitonclick()