from turtle import Turtle

FONT = ("Arial", 50, "bold")


class Letters(Turtle):
    def __init__(self, STRETCH_FACTOR, HEIGHT):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.font = FONT
        self.stretch_factor = STRETCH_FACTOR
        self.height = HEIGHT
        self.block_size = STRETCH_FACTOR * 20
        self.movement = self.block_size
        self.xcor_writing = (self.block_size * -2) - 5
        self.ycor_writing = (self.height / 2) - ((self.block_size / 2) + 40)
        self.goto(self.xcor_writing, self.ycor_writing)

    def write_guess(self, user_guess):
        for letter in user_guess.upper():
            self.write(letter, align="center", font=FONT)
            self.forward(self.movement)
        self.ycor_writing -= self.block_size
        self.goto(self.xcor_writing, self.ycor_writing)

    def write_guess_final(self, user_guess):
        self.goto(self.xcor_writing, (self.block_size * -2) - 30)
        for letter in user_guess.upper():
            self.write(letter, align="center", font=FONT)
            self.forward(self.movement)
