# def avg_numbers(numbers):
#     result = 0
    
#     for number in numbers:
#         result += number
    
#     average = result // 2
#     return average

# total_amount = [40, 60, 100, 150, 50, 100]
# print(avg_numbers(total_amount))

# def average_numbers(numbers):
#     result = sum(numbers)
#     average = result // 2
#     return average

# my_money = average_numbers([45, 78, 19, 73, 21])
# print(my_money)

# num = int(input("please type an integer number: "))
# def multiply(num):
#     for i in range(1, 11):
#         print(num, "X", i, "=", num*i)
# multiply(num)

def multiplication(num=1):
    for i in range(1, 11):
        print(num, "X", i, "=", num*i)
multiplication()