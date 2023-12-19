year = 2012;

# METHOD ONE:
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('leap year');
#         else:
#             print('not leap year');
#     else:
#         print('leap year');
# else:
#     print('not leap year');

# METHOD TWO:
# if year % 4 != 0:
#     print('not leap year');
# else:
#     if year % 100 != 0:
#         print('leap year');
#     else:
#         if year % 400 != 0:
#             print('not leap year');
#         else:
#             print('leap year');

# METHOD THREE:
# if year % 400 == 0:
#     print('leap year');
# elif year % 100 == 0:
#     print('not leap year');
# elif year % 4 == 0:
#     print('leap year');
# else:
#     print('not leap year');

# METHOD FOUR:
# if year % 100 != 0 and year % 4 == 0:
#     print('leap year');
# elif year % 100 == 0 and year % 400 == 0:
#     print('leap year');
# else:
#     print('not leap year');

year = input('type a year and press enter: ');
year = int(year);

if year % 100 != 0 and year % 4 == 0:
    print(year,'is leap year');
elif year % 100 == 0 and year % 400 == 0:
    print(year,'is leap year');
else:
    print(year,'is not leap year');