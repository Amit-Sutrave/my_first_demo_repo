
#This is a Python Program to print the largest even and largest odd number in a list.


# list=[]

# a=[]
# b=[]
# value=int(input("enter how many elements you want to add in list :"))
# for i in range(0,value):
#     elements=int(input("enter element :"))
#     list.append(elements)

# print(list)


# for j in list:
#     if j%2==0:
#         print("even nuumbers is :",j)
#         a.append(j)  
#     else:
#         print("odd nuumbers is :",j)
#         b.append(j)
# a.sort()
# b.sort()

# print("largest even number is :",a[-1])
# print("largest odd number is :",b[-1])


#==============================================================================#

list=[]
evan=[]
odd=[]
value=int(input("enter how many elements you want to add in list :"))
for i in range(0,value):
    elements=int(input("enter element :"))
    list.append(elements)

# lar_even=list[0]
for j in list:
    if j%2==0:
        # j>lar_even
       # print("even number is :",j)
        evan.append(j)
    else:
       # print("odd number is :",j)
        odd.append(j)

m=evan[0]
for k in evan:
    if k>m:
        m=k
print("max even no ",m)

m=odd[0]
for k in odd:
    if k>m:
        m=k
print("max odd no ",m)


