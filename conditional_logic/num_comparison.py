n1 = 20;
n2 = 30;
n3 = 25;

# if n1 > n2:
#     print('max number is:', n1);
# elif n1 > n3:
#     print('max number is:', n1);
# elif n2 > n3:
#     print('max number is:', n2);
# else:
#     print('max number is:', n3);

if n1 > n2 :
    max_n = n1;

else : 
    max_n = n2;

if n3 > max_n :
    max_n = n3;

print('maximum:', max_n);