import turtle
import time

#Настройки экрана
win = turtle.Screen()
win.title("Голодная Змейка")
win.bgcolor("black")
win.setup (width=600, height=600)
win.tracer(0)

#Голова змейки
head = turtle.Turtle()
head.speed(0)
head.goto(0,0)
head.shape("square")
head.color("green")
head.penup()
head.direction = "stop"

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

while True:
    win.update()
    move()
    time.sleep(0.1)