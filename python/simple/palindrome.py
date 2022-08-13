value=int(input("enter a number to check number is palindrome or not :"))
b=0
while(value>0):
    a=value%10
    b=(b*10)+a
    value=value/10

if b==value:
    print("number is palindrome")
else:
    print("number is not palindrome")
