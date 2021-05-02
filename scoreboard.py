from turtle import Turtle
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 18, "bold")

with open("data.txt", mode="r") as data:
    HIGHT_SCORE = int(data.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.score = 0
        self.hight_score = HIGHT_SCORE
        self.write_score()

    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.hight_score}")
        self.score = 0

        self.write_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over.", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, hight score: {self.hight_score}", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
