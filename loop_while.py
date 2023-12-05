i = 0
while i < 5:
    print(i)
    i += 1

i = 5
while i > 1:
    i -= 1
    print(i)

multiplication_table/Namta

n = 9
m = 1
while m <= 10:
    print(n, "X", m, "=", n*m)
    m += 1

n = input("Please type a postive integer number and press enter: ")
n = int(n)
for i in range(1, 11):
    print(n, "X", i, "=", n*i)
    i += 1

n = 15
for i in range(1, 11):
    print(n, "X", i, "=", n*i)
    i += 1

n = input("Please write a positive integer number and press enter: ")
n = int(n)

m = 1
while m <= 10:
    print(n, "X", m, "=", n*m)
    m += 1

import turtle

turtle.color("olive")
turtle.speed(20)
turtle.shape("turtle")

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick();

import turtle

height = 14
width = 10

turtle.speed(25)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()