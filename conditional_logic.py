num_equal = 2 == 3;
# print(num_equal);

num_equal2 = 3 == 3;
# print(num_equal2);

num_less = 2 > 3;
# print(num_less);

num_greater = 2 < 3;
# print(num_greater);

num_not_equal = 2 != 3;
# print(num_not_equal);

num_not_equal2 = 3 != 3;
# print(num_not_equal2);

num_less_equal = 2 >= 3;
# print(num_less_equal);

num_greater_equal = 2 <= 3;
# print(num_greater_equal);

"""comparison operator in Python:
1. Equal: ==
2. Not equal: != 
3. Less than: < 
4. Greater than: > 
5. Lessthan or equal: <= 
6. Greaterthan or equal: >= 
"""

# two string equal or not 
large_str = 'Bangladesh' == 'Bangladesh';
# print(large_str);

small_str = 'Bangladesh' == 'bangladesh';
# print(small_str);

my_money = 30;
rickshaw_fare = 40;
ride_at_rickshaw = my_money >= rickshaw_fare;
# print(ride_at_rickshaw);

my_money2 = 60;
rickshaw_fare2 = 40;
ride_at_rickshaw2 = my_money2 >= rickshaw_fare2;
# print(ride_at_rickshaw2);

day = 'Sunday';
day_true = day == 'Sunday';
# print(day_true);

day = 'Friday';
day_false = day == 'Saterday';
# print(day_false);

today = 'Wednesday';
day_false = not (today == 'Wednesday');
# print(day_false);

value_false = not True; 
# print(value_false);

value_true = not False;
# print(value_true);

num = 20;
value_true = num > 10;
value_false = num > 100;

validation_and = value_true and value_false;
# print(validation_and);

validation_or = value_true or value_false;
# print(validation_or);

validation_not = not (value_true == value_false);
# print(validation_not);

numbers = [1,2,3,57,54, 78, 50, 74];
# print(numbers);
total_index = len(numbers);
# print(index);
specific_element = numbers[2];
# print(specific_element);

saarc = ['Bangladesh', 'Afganistan', 'India', 'Bhutan', 'Nepal', 'Pakistan', 'Sri Lanka'];
# print(saarc);
# print(saarc[0]);
# print('Number of countries in SAARC: ', len(saarc));

saarc_element = 'Bangladesh' in saarc;
# print(saarc_element);

saarc_element = 'Japan' in saarc;
# print(saarc_element);

saarc_element = 'China' not in saarc;
# print(saarc_element);

# if and else statement: 
saarc = ['Bangladesh', 'Afganistan', 'India', 'Bhutan', 'Nepal', 'Pakistan', 'Sri Lanka'];
# country = input('Enter the name of the country: ');
# if country in saarc:
#     print(country, 'is a member of SAARC');
# else:
#     print(country, 'is not a member of SAARC');

# print('Program terminated');

# elif statement: 
marks = input('Please type your marks and press enter: ');
marks = int(marks);

if marks >= 80:
    grade = 'A+';
elif marks >= 70:
    grade = 'A';
elif marks >= 60:
    grade = 'A-';
elif marks >= 50:
    grade = 'B';
else:
    grade = 'F';

print('Your grade is:', grade);