from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-270, 260)
        self.write(f'Level: {self.level}', font=FONT)


    def update(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', font=FONT)


    def game_over(self):
        self.goto(-70, 0)
        self.write(f"Game Over", font=FONT)