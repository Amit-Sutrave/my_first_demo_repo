list=[]

value=int(input("enter how many element you want to add in list :"))
for i in range(0,value):
    elements=int(input("enter elements "))
    list.append(elements)
num=int(input("enter number ,which you want to know how many times the number is repaet :"))


count=0
for j in list:
    if num==j:
        count=count+1

print(count)
