import turtle
from ball import Ball

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
vx = []
vy = []
xpos = []
ypos = []
color_list = []
ball_color = []
ball = Ball(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls)
ball.initializing()

while True:
    turtle.clear()
    for i in range(num_balls):
        ball.draw_circle(i)
        ball.move_circle(i)
    turtle.update()

turtle.done()