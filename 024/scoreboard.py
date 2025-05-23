from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\arcis\OneDrive\Pulpit\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C\\Users\\arcis\\OneDrive\\Pulpit\\data.txt", mode='w', encoding="utf-8") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def highest_score(self):
    #     try:
    #         with open("data.txt", mode="r", encoding="utf-8") as file:
    #             score = file.read().strip()
    #             return int(score) if score else 0
    #     except FileExistsError:
    #         return 0




