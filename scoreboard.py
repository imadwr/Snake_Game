from turtle import Turtle
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 18, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over.", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def write_score(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align=SCORE_ALIGNMENT, font=SCORE_FONT)
