import tkinter as tk
import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Player Names
info = trtl.Turtle()
info.penup()
info.goto(500, -300)
info.pendown()
info.color("white")
player_a = input("Enter a name for Player A: ")
info.penup()
info.goto(70, 0)
info.pendown()
player_b = input("Enter a name for Player B: ")

# Score
scores = [0, 0]

# font setup
font_setup = ("Arial", 24, "normal")

# Left Paddle
left_paddle = trtl.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle_color = input(player_a + ", enter a color for your paddle: ")
left_paddle.color(left_paddle_color)
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right Paddle
right_paddle = trtl.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle_color = input(player_b + ", enter a color for your paddle: ")
right_paddle.color(right_paddle_color)
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = trtl.Turtle()
ball.speed(0)
ball_shapes = ["circle", "square", "triangle", "turtle"]
ball.shape(rand.choice(ball_shapes))
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4
ball_colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

# Pen
pen = trtl.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(player_a + ": 0   " + player_b + ": 0",
          align="center",
          font=("Arial", 24, "normal"))


# Functions
def left_paddle_movement(move, direction):
    if (direction == "up"):
        y = left_paddle.ycor()
        y += move
        left_paddle.sety(y)
    else:
        y = left_paddle.ycor()
        y -= move
        left_paddle.sety(y)


def right_paddle_movement(move, direction):
    if (direction == "up"):
        y = right_paddle.ycor()
        y += move
        right_paddle.sety(y)
    else:
        y = right_paddle.ycor()
        y -= move
        right_paddle.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(lambda: left_paddle_movement(20, "up"), "w")
wn.onkeypress(lambda: left_paddle_movement(20, "down"), "s")
wn.onkeypress(lambda: right_paddle_movement(20, "up"), "Up")
wn.onkeypress(lambda: right_paddle_movement(20, "down"), "Down")

# Player Instructions
scoretill = input("Till what score would you like to go to?: ")
scoretill = int(scoretill)
print(
    player_a +
    ", click on the game screen and use the 'w' key on your keyboard to move up and the 's' key to go down"
)

print(
    player_b +
    ", click on the game screen and use the 'up' arrow on your keyboard to move up and the 'down' arrow to go down"
)

#Click to start
#IMPLEMENT THIS

# Main game loop

while (scores[0] < scoretill and scores[1] < scoretill):
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scores[0] += 1
        pen.clear()
        pen.write(player_a + ": " + str(scores[0]) + " " + player_b + ": " +
                  str(scores[1]),
                  align="center",
                  font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scores[1] += 1
        pen.clear()
        pen.write(player_a + ": " + str(scores[0]) + " " + player_b + ": " +
                  str(scores[1]),
                  align="center",
                  font=("Arial", 24, "normal"))

# Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < right_paddle.ycor() + 50
            and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        ball.color(rand.choice(ball_colors))

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < left_paddle.ycor() + 50
            and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        ball.color(rand.choice(ball_colors))

# Winner Message - how do i get this to show?
while(True):
    message = trtl.Turtle()
    message.penup()
    message.goto(-250, 0)
    message.pendown()
    message.color("white")
    if (scores[0] > scores[1]):
        message.write("Congratulations " + player_a + ", you win!",
                    font=font_setup)
    else:
        message.write("Congratulations " + player_b + ", you win!",
                    font=font_setup)
