value=int(input("enter number to check number is armstrong or not :"))
r=0

while(value>0):
    a=value%10
    r=r+(a*a*a)
    value=value/10

if r==value:
    print("number is armstrong :")
else:
    ("number is not armstrong ")