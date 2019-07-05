import turtle

t = turtle.Pen()
t.color(1,0,0)
t.begin_fill()
for i in range(1,20):
    t.forward(100)
    t.left(95)
t.up()
t.end_fill()
t.forward(200)
t.color(0,0,1)
t.begin_fill()
t.down()

for i in range(1,38):
    t.forward(100)
    t.left(175)
t.color(0,0,0)
t.end_fill()
t.up()


