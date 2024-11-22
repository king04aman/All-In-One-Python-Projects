from turtle import Turtle, Screen
import time
from food import Food
from Snake import Snake
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
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
    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset()
        data = str(score.high_score)
        with open("data.txt", mode="w") as file:
            file.write(data)
        snake.reset()
    # collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            data = str(score.high_score)
            with open("data.txt", mode="w") as file:
                file.write(data)
            snake.reset()








screen.exitonclick()
