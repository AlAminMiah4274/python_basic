# while True:
#     n = input("Please type a number (0 to exit): ");
#     n = int(n);

#     if n == 0:
#         break;
    
#     print("Square of", n, "is", n*n);


# while True:

#     n = input("Please type positve number (0 to exit): ");
#     n = int(n);

#     if n < 0:
#         print("We only allow positive number. Please try again");
#         continue;

#     if n == 0:
#         break;

#     print("Sqaure of", n, "is", n*n);

terminate = False;

while not terminate:
    number1 = input("Please enter a number: ");
    number1 = int(number1);
    number2 = input("Please enter another number: ");
    number2 = int(number2);

    while True:
        operation = input("Please type sub/add or quit to exit: ");

        if operation == "quit":
            terminate = True;
            break;

        if operation not in ["add", "sub"]:
            print("Unknown operation!");
            continue;

        if operation == "add":
            print("Result is", number1 + number2);
            break;

        if operation == "sub":
            print("Result is", number1 - number2);
            break;