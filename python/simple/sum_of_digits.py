#This is a Python Program to find the sum of digits in a number.

# value=int(input("enter a number of minimum of 2 digits :"))
# b=0
# while(value>0):
#     a=value%10
#     b=b+a
#     value=value//10

# print("sum of digits is :",b)

###########===================================================================######################################
#This is a Python Program to count the number of digits in a number.

value=int(input("enter a number to count the number of digits  :"))
b=0
while(value>0):
    a=value%10
    b=b+1
    value=value//10

print("sum of digits is :",b)