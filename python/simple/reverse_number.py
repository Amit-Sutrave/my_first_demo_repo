value=int(input("enter number to do it reverse :"))
b=0
while(value>0):
    a=value%10
    b=(b*10)+a
    value=value//10

print("reverse number is :",b)