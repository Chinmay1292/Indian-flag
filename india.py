import turtle as t
t.speed("fast")
# Big Blue Circle
t.penup()
t.goto (10, -65)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(65) 
t.end_fill()

# Big White Circle
t.penup()
t.goto (10, -57)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(57) 
t.end_fill()

# Mini Blue Circles
t.penup()
t.goto(3,53) 
t.pendown()
t.color("navy")
for i in range(24):
	t.begin_fill()
	t.circle(3)
	t.end_fill() 
	t.penup()
	t. forward(14)
	t.right(15) 
	t.pendown()

# Small Blue Circle
t.penup() 
t.goto (10, -15)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

# Spokes
t.penup()
t.goto(10, 0)
t.pendown() 
t.pensize(2)

for i in range(24):
	t.forward(60)
	t.backward (60) 
	t.left(15)
t.hideturtle()
t.speed("slowest")
t.penup()
t.goto(-400,250)
t.pendown()
t.bgpic("r2.png")







t.done()