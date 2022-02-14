import turtle as t

t.Screen().bgcolor("lightblue")
t.Screen().screensize(500, 500)
t.Screen().setworldcoordinates(-300, 300, 300, 900)
t.Screen().tracer(0, 0)


def filled_circle(radius, color):
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def cloud(radius, cloud_color="white"):
    filled_circle(radius, cloud_color)
    t.forward(radius)
    filled_circle(radius, cloud_color)
    t.right(90)
    filled_circle(radius, cloud_color)
    t.right(90)
    filled_circle(radius, cloud_color)
    t.right(90)
    filled_circle(radius, cloud_color)
    t.right(90)


def rainbow(radius=200, interval=10):
    roygbiv = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']

    for r_color in roygbiv:
        filled_circle(radius, r_color)
        radius -= interval

        # Move turtle a up by a little
        t.left(90)
        t.forward(interval)
        t.right(90)


t.penup()

t.goto(100, 900)
cloud(20)
t.goto(-50, 850)
cloud(30)
t.goto(50, 600)
cloud(50)
t.goto(200, 500)
cloud(5)

t.goto(0, 0)
rainbow(300, 10)

t.goto(-200, 500)
cloud(15)
t.goto(50, 400)
cloud(10)
t.goto(50, 300)
cloud(10)

t.Screen().update()

# 设置成画完不会自动退出
t.done()
