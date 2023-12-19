# positive or negative: 
num = input('Please type any number and press enter: ');
num = int(num);

if num > 0:
    print('It is a positive number.');
elif num == 0:
    print('It is a nutral number.');
else:
    print('It is a negative number.');

print('Programme terminated');

# # odd or even: 
num = input('Type a number and press enter: ');
num = int(num);

if num % 2 == 0:
    print('the number is even');
else:
    print('the number is odd');

print('programme terminated')

# positve or negative and odd or even:
type_validation = input('enter any number and press enter: ');
type_validation = int(type_validation);

if type_validation >= 0 and type_validation % 2 == 0:
    print('The number is positive and even');

elif type_validation < 0 and type_validation % 2 == 0:
    print('the number is negative but even');

elif type_validation >= 0 and type_validation % 2 != 0:
    print('the number is positive but odd');

else:
    print('the number negative and odd');

print('programme terminated');