#This is a Python Program to print all prime numbers within a given range.


value=int(input("enter number to check  prime number or not :"))
p=0
for i in range (1,value+1):
    if value%i==0:
       p=p+1

if p==2:
     print("number is prime number ")
else:
    print("number is not a primenumber ")       