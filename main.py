import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Breakout Game")


# # Turn off animation
screen.tracer(0)

paddle = Paddle((0, -350))
ball = Ball()
blocks = Blocks()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    if len(blocks.total_blocks) < 32:

        blocks.create_blocks()
    else:
        # update animation
        screen.update()
        ball.move_ball()

        # Detect collision with Wall
        if ball.ycor() > 380:
            # Needs to bounce
            ball.bounce_y()
        elif ball.xcor() > 580 or ball.xcor() < -580:
            # Needs to bounce
            ball.bounce_x()

        # Detect collision with paddle
        if ball.distance(paddle) < 60 and ball.ycor() > -360:
            ball.bounce_y()

        # Detect when paddle misses
        if ball.ycor() < -420:
            ball.reset_position()

        # Detect collision with block
        for block in blocks.total_blocks:
            # print(block)
            if block.distance(ball) < 70:

                blocks.total_blocks.remove(block)
                block.ht()
                ball.bounce_y()
                scoreboard.point()
            if scoreboard.score == 32:
                scoreboard.winner()
                game_is_on = False
                break


screen.exitonclick()
