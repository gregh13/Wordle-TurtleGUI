from turtle import Turtle, colormode
colormode(255)

alpha = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
alphabet = alpha.split()


class Keyboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color(203, 206, 212)
        self.start_pointx = -165
        self.start_pointy = -220
        self.pos_x = self.start_pointx
        self.pos_y = self.start_pointy
        self.goto(self.pos_x, self.pos_y)

    def stamp_out(self, bad_letters):
        self.goto(self.start_pointx, self.start_pointy)
        squares = 0
        for letter in alphabet:
            if letter in bad_letters:
                self.stamp()
            squares += 1
            if squares < 10:
                self.forward(36.1)
            elif squares == 10:
                self.pos_x = self.start_pointx + 16
                self.pos_y = self.start_pointy - 50
                self.goto(self.pos_x, self.pos_y)
            elif 10 <= squares < 19:
                self.forward(36.5)
            elif squares == 19:
                self.pos_x = self.start_pointx + 52.5
                self.pos_y = self.start_pointy - 100
                self.goto(self.pos_x, self.pos_y)
            elif squares >= 19:
                self.forward(36.5)


# colors = colorgram.extract('keyboard_best.png', 4)
# print(colors)
# Rgb(r=203, g=206, b=212)
