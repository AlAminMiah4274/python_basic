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