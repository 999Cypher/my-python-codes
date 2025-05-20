from turtle import *

def r(x,y):
    rt(x)
    fd(y)



tracer(4)
fd(400)
bgcolor("black")
color("green")
width(2)

for i in range(2000):
    fd(i)
    r(90, i)
    r(90, i)
    r(270, i)
    r(90, i)
    circle(100, 100)

done()