from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0, 0, 0)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self): self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self): self.x_move *= -1

    def bounce_y(self): self.y_move *= -1

ball = Ball()
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280: ball.bounce_y()
    if ball.xcor() > 280 or ball.xcor() < -280: ball.bounce_x()

screen.exitonclick()