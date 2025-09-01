import turtle
import time
import random 

delay = 0.1
score = 0

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

#Еда
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Тело
segments = []

#Счет
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Счет: 0", align="center", font=("Courier", 24, "normal"))

def close_game():
    if head.direction != "stop":
        head.direction = "stop"
        win.bye()

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
win.onkeypress(close_game, "q")

while True:
    win.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Счёт: {}".format(score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        # Перемещаем еду
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("darkgreen")
        new_segment.penup()
        segments.append(new_segment)

        # Увеличиваем счёт
        score += 10
        pen.clear()
        pen.write("Счёт: {}".format(score), align="center", font=("Courier", 24, "normal"))

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Счёт: {}".format(score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)