from turtle import Turtle

class Score(Turtle):


        def __init__(self):
            self.score = 0
            with open("data.txt") as file:
                self.HighScore = int(file.read())
            self.high_score = self.HighScore
            super().__init__()
            self.color("white")
            self.penup()
            self.goto(0, 265)
            self.hideturtle()
            self.update_score()
        def update_score(self):
            self.clear()
            self.write(f"Score: {self.score} High Score:{self.high_score}", align='center', font=('Arial', 24, 'normal'))
        def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
            self.score = 0
            self.update_score()
        def increase_score(self):
            self.score += 1
            self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Arial', 24, 'normal'))