import turtle as t
t.hideturtle()
t.bgcolor("black")
t.color('lightblue')
days=["Sunday","Monday","Tuesday", "Wednesday", "Thursday", "Friday","saturday"]
num_days=len(days)
angle_gap= 250/num_days
redius=100

for r in range (num_days):
    angle=angle_gap * r
    t.setheading(angle)
    t.pendown()
    t.forward(redius - 20)
    t.stamp()
    t.penup()
    t.forward(40)

    t.write(days[r],align='center',font=('Arial',13,'bold'))
    t.backward(redius)
t.done()