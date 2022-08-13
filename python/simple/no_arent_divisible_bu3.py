
#Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

value=int(input("enter number  :"))
for i in range(0,value):
    if i%2==0:
        print("--")
    elif i%3==0:
         print("--")
    else:
        print(i)
    
####################=============================================================================########################

#Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

value=int(input("enter number  :"))
for i in range(0,value):
    if i%7==0 and i%5==0:
        print(i)
    elif i%5==0:
         print("--")
    else:
        print(i)
#######################====================================================================#######################################i)

#This is a Python Program to print all numbers in a range divisible by a given number.

value=int(input("enter number  :"))

for i in range(0,1000):
    if i%value==0:
        print(i)
   