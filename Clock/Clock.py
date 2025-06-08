import time
import turtle
import datetime
import threading

#set the arms at current time location

H = int(datetime.datetime.now().strftime("%I")) 
M = int(datetime.datetime.now().strftime("%M"))
H = (H * 30) + (M * 12/30)
M = M * 6
P = str(datetime.datetime.now().strftime("%p"))


# making of turtles
a = turtle.Turtle()
a.screen.bgcolor("lightgreen")
a.hideturtle()
a.speed(0)

b = turtle.Turtle()
b.screen.bgcolor("lightgreen")
b.hideturtle()
b.speed(0)

c = turtle.Turtle()
c.screen.bgcolor("lightgreen")
c.hideturtle()
c.speed(0)


p = turtle.Turtle()
p.color('darkblue')
p.penup()
p.right(90)
p.fd(60)
p.pendown()
p.hideturtle()

turtle.setup(600,600)
turtle.title("CLOCK")

def ap():
    
    p.write(P,font = ('times of roman',20))


#design a clock
a.pensize(5)
a.begin_fill()
a.fillcolor('blue')
a.penup()
a.goto(0,-200)
a.pendown()
a.circle(200)
a.penup()
a.home()
a.goto(0,-170)
a.pendown()
a.circle(170)
a.end_fill()


a.begin_fill()
a.fillcolor('lightblue')
a.penup()
a.home()
a.goto(0,-170)
a.pendown()
a.circle(170)
a.end_fill()

a.penup()
a.home()
a.pendown()
a.left(90)

#marking a clock numbers
for i in range(0,12):

    a.right(30)
    a.penup()
    a.fd(130)
    a.pendown()
    a.write((i+1), font=("Arial", 20, "normal"))
    a.penup()
    a.goto(-6,-7)
    a.pendown()

#second hand
def second():
    angle = 0
    a.penup()
    a.home()
    a.left(90)
    a.pendown
    while True:
        a.right(angle)
        a.pendown()
        a.pensize(2)
        a.fd(100)
        time.sleep(1)
        a.undo()
        a.goto(0,0)
        angle = 6

#minute hand
def minute():
    angleb = 0
    b.left(90)
    b.right(M)
    while True:
        b.right(angleb)
        b.pendown()
        b.pensize(3)
        b.fd(120)
        time.sleep(60)
        b.undo()
        b.goto(0,0)
        angleb = 6

#hour hand
def hour():
    anglec = 0
    c.left(90)
    c.right(H)
    while True:
        c.right(anglec)
        c.pendown()
        c.pensize(6)
        c.fd(80)
        time.sleep(600)
        c.undo()
        c.goto(0,0)
        anglec = 1

#activate all three arm at once

thread1 = threading.Thread(target = second)
thread1.start()

thread2 = threading.Thread(target = minute)
thread2.start()

thread3 = threading.Thread(target = hour)
thread3.start()

thread4 = threading.Thread(target = ap)
thread4.start()

turtle.done()



















































