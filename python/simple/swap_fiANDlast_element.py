#python program to swap first and last element in list
lst=[]
value=int(input("enter range "))

for i in range(0,value):
    elements=int(input("enter element"))
    lst.append(elements)

print(lst)

for j in lst:
    pass

a=lst[0]
z=lst[value-1]
print(a,z)
lst[0]=z
lst[value-1]=a

print("swapping values first and last :",lst)

#==========================================#

