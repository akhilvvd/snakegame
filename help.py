from turtle import Turtle


class Help(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=-200, y=240)
        self.color("blue")
        self.hideturtle()
        self.option()

    def option(self):
        self.write(f"GAME OPTIONS\nUp= ⬆\nDown= ⬇\nLeft= ⬅"
               f"\nRight= ➡", align="right")
