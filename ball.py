import turtle
import random


class Ball:
    def __init__(self, xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.color = ball_color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.size = ball_radius
        self.num_balls = num_balls

    def draw_circle(self, i):
        turtle.penup()
        turtle.color(self.color[i])
        turtle.fillcolor(self.color[i])
        turtle.goto(self.xpos[i], self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_circle(self, i):
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.size):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.size):
            self.vy[i] = -self.vy[i]

    def initializing(self):
        for i in range(self.num_balls):
            self.xpos.append(random.randint(-1*self.canvas_width + self.size, self.canvas_width - self.size))
            self.ypos.append(random.randint(-1*self.canvas_height + self.size, self.canvas_height - self.size))
            self.vx.append(random.randint(1, 0.01*self.canvas_width))
            self.vy.append(random.randint(1, 0.01*self.canvas_height))
            self.color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))