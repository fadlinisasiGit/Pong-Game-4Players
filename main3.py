import turtle as t
import os

# Score variables

player_a_score = 0
player_b_score = 0

win = t.Screen()  # buat window
win.title("Volley Pong Game")  # memberi Nama game
win.bgcolor('black')  # warna untuk background homescreen
win.setup(width=1366, height=768)  # Ukuran Panel
win.tracer(0)

# membuat controller kiri 1
paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(stretch_wid=10, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-650, 0)

# membuat controller kiri 2
paddle_left2 = t.Turtle()
paddle_left2.speed(0)
paddle_left2.shape('square')
paddle_left2.color('Red')
paddle_left2.shapesize(stretch_wid=5, stretch_len=1)
paddle_left2.penup()
paddle_left2.goto(-650, 0)

# membuat controller kanan 1
paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(650, 0)

# membuat controller kanan 2
paddle_right2 = t.Turtle()
paddle_right2.speed(0)
paddle_right2.shape('square')
paddle_right2.shapesize(stretch_wid=5, stretch_len=1)
paddle_right2.color('red')
paddle_right2.penup()
paddle_right2.goto(650, 0)

# membuat bola ping pong

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball_dx = 4  # mengatur kecepatan bola
ball_dy = 4

# membuat pen scoreboard

pen = t.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                    Player B: 0 ", align="center", font=('Monaco', 24, "normal"))


# Menaikkan kontroler kiri

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

def paddle_left_up2():
    y = paddle_left2.ycor()
    y = y + 15
    paddle_left2.sety(y)

# Menurunkan kontroler kiri

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

def paddle_left_down2():
    y = paddle_left2.ycor()
    y = y - 15
    paddle_left2.sety(y)


# Menaikkan kontroler kanan

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

def paddle_right_up2():
    y = paddle_right2.ycor()
    y = y + 15
    paddle_right2.sety(y)

# Menurunkan kontroler kanan

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

def paddle_right_down2():
    y = paddle_right2.ycor()
    y = y - 15
    paddle_right2.sety(y)


# Fungsi Keyboard untuk menggerakkan kontroler

win.listen()
win.onkeypress(paddle_left_up, "w")
win.onkeypress(paddle_left_down, "s")
win.onkeypress(paddle_left_up2, "q")
win.onkeypress(paddle_left_down2, "a")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")
win.onkeypress(paddle_right_up2, "p")
win.onkeypress(paddle_right_down2, "l")

# Loop utama game

while True:
    win.update()  # This methods is mandatory to run any game

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border
    # width=1366, height=768
    if ball.ycor() > 265:  # Right top paddle Border
        ball.sety(265)
        ball_dy = ball_dy * -1

    if ball.ycor() < -265:  # Left top paddle Border
        ball.sety(-265)
        ball_dy = ball_dy * -1

    if ball.xcor() > 750:  # right width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write(" Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    if (ball.xcor()) < -750:  # Left width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write(" Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    # Handling the collisions with paddles.

    if (ball.xcor() > 640) and (ball.xcor() < 650) and (
            ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(640)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() > 640) and (ball.xcor() < 650) and (
            ball.ycor() < paddle_right2.ycor() + 40 and ball.ycor() > paddle_right2.ycor() - 40):
        ball.setx(640)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -640) and (ball.xcor() > -650) and (
            ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-640)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -640) and (ball.xcor() > -650) and (
            ball.ycor() < paddle_left2.ycor() + 40 and ball.ycor() > paddle_left2.ycor() - 40):
        ball.setx(-640)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if (player_a_score == 5):
        win.clear()
        pen.write("Player A Win", align="center", font=('Monaco', 35, "normal"))

    if (player_b_score == 5):
        win.clear()
        pen.write("Player B Win", align="center", font=('Monaco', 35, "normal"))
