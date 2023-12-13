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


# to draw a circle using square box:
# import turtle;

# turtle.speed(35);
# turtle.color("red");
# turtle.shape("turtle");

# def draw_square(side_length):
#     for i in range(4):
#         turtle.forward(side_length);
#         turtle.left(90);

# counter = 0;
# while counter < 36:
#     draw_square(150);
#     turtle.right(10);
#     counter += 1;

# turtle.exitonclick();

# to draw a equilateral triangle: 
# import turtle

# turtle.shape("turtle")
# turtle.speed(20)
# turtle.color("purple")

# def equilateral_triangle(side_length):
#     for i in range(3):
#         turtle.forward(side_length)
#         turtle.left(120)

# counter = 0
# while counter < 1:
#     equilateral_triangle(200)
#     counter += 1

# turtle.exitonclick();

# local and global variable: ********
# def my_func(x):
#     print("Inside my_func: ", x)
#     x = 10
#     print("Inside my_func: ", y)

# x = 20
# y = 50
# my_func(x)
# print(x)

# def my_func(y):
#     print("y =", y)
#     print("x =", x)

# x = 20
# my_func(x)

# def my_func(y):
#     print("y =", y)
#     print("xyz =", xyz)

# xyz = 20
# my_func(xyz)
# print("y =", y)

# default value: *****
# def my_func(y=10):
#     print("y =", y)

# x = 40
# my_func(x)
# my_func()

# def my_func(x, y=10, z):
#     print("x =", x, "y =", y, "z =", z)

# x = 5
# y = 6
# z = 7
# my_func(x, y, z)

def my_func(x, y=10, z=0):
    print("x =", x, "y =", y, "z =", z)

a = 5
b = 6
c = 7
print(a, b, c)
print(a, c)
print(a)