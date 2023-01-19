from turtle import Turtle


ALIGN = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_Score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.color("Purple")
        self.write(f"Score: {self.score} || High Score: {self.high_Score}", align=ALIGN, font=FONT)

    def high_score(self):
        if self.score > self.high_Score:
            self.high_Score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_Score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.color("green")
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def score_count(self):
        self.score += 1
        self.update_score()
