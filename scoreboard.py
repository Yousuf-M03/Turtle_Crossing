from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("black")
        self.penup()
        self.ht()
        self.level = 1
        self.update_lvl()

    def update_lvl(self):
        self.clear()
        self.goto(-215, 260)
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)


    def lvl_up(self):
        self.level += 1
        self.update_lvl()

    def game_over(self):
        self.goto(0,0)
        self.pencolor("black")
        self.write("GAME OVER", align="center", font=("Courier", 40, "bold"))



