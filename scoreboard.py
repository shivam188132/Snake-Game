from turtle import Turtle

ALINGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())


        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", align=ALINGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        print(f"high score: {self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 10
        print(f"Score: {self.score}")
        self.update_scoreboard()



