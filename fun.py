# # def add(n1, n2):
# #     return n1 + n2;

# # result = add(8,10);
# # print(result);

# def add(n1, n2):
#     return n1 + n2;

# # n = 10;
# # m = 5;
# # result = add(n, m);
# # print(result);

# # number1 = 10;
# # number2 = 10;
# # result = add(number1, number2);
# # print(result);

# # n1 = 15;
# # n2 = 10;
# # result = add(n1, n2);
# # print(result);

# print(add(5.5, 8.5));


# to draw square box:
import turtle

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length);
        turtle.left(90);

counter = 0;
while counter < 90:
    draw_square(100);
    turtle.right(4);
    counter += 1;

turtle.exitonclick();