from turtle import Turtle


class Square(Turtle):
    def __init__(self, STRETCH_FACTOR, HEIGHT, chosen_word):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color("black", "Snow")
        self.chosen_word = chosen_word
        self.stretch_factor = STRETCH_FACTOR
        self.height = HEIGHT
        self.block_size = STRETCH_FACTOR * 20
        self.movement = self.block_size
        self.xcor_block = (self.block_size * -2) - 5
        self.yblock_start = (self.height / 2) - ((self.block_size / 2) + 10)
        self.ycor_block = self.yblock_start
        self.shapesize(self.stretch_factor, self.stretch_factor)
        self.start_up()

    def start_up(self):
        for b in range(5):
            self.goto(self.xcor_block, self.ycor_block)
            self.ycor_block -= self.block_size
            for _ in range(5):
                self.stamp()
                self.forward(self.movement)
        self.goto(self.xcor_block, self.block_size * -2)
        for _ in range(5):
            self.stamp()
            self.forward(self.movement)
        self.goto(0, self.block_size * -3)
        self.write("^^FINAL GUESS^^", align="center", font=("Courier", 18, "normal"))
        self.ycor_block = self.yblock_start
        self.goto(self.xcor_block, self.ycor_block)

    def guess_feedback(self, user_guess):
        bad_letters = []
        for letter in range(5):
            if user_guess[letter] == self.chosen_word[letter]:
                self.color("black", "Green")
                self.stamp()
                self.forward(self.movement)
            elif user_guess[letter] in self.chosen_word:
                self.color("black", "Orange")
                self.stamp()
                self.forward(self.movement)
            else:
                self.color("black", "Grey")
                self.stamp()
                self.forward(self.movement)
                bad_letters.append(user_guess[letter])
        self.ycor_block -= self.block_size
        self.goto(self.xcor_block, self.ycor_block)
        return bad_letters

    def guess_feedback_final(self, user_guess):
        self.goto(self.xcor_block, self.block_size * -2)
        bad_letters = []
        for letter in range(5):
            if user_guess[letter] == self.chosen_word[letter]:
                self.color("black", "Green")
                self.stamp()
                self.forward(self.movement)
            elif user_guess[letter] in self.chosen_word:
                self.color("black", "Orange")
                self.stamp()
                self.forward(self.movement)
            else:
                self.color("black", "Grey")
                self.stamp()
                self.forward(self.movement)
                bad_letters.append(user_guess[letter])
        return bad_letters
