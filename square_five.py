import turtle;

turtle.shape('turtle');
turtle.speed(5);

for side_length in range(50, 131, 20):
    for i in range(4):
        turtle.forward(side_length);
        turtle.left(90);

turtle.exitonclick();