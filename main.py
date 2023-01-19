from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
from help import Help
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
help = Help()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    help.option()





    # detect the collision of the food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_count()


    # detect the collision of the wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.high_score()
        snake.reset()

    # detect to collision with tail

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.high_score()
            snake.reset()

screen.exitonclick()
