#This is a Python Program to find the largest number in a list.


# list =[]

# value=int(input("enter how many element you want to add in list :"))

# for i in range(0,value):
#     element=int(input())
#     list.append(element)

# print(list)

# list.sort()
# print("after sort list is :",list)

# print("largest number in list is :",list[-1])

#also you can do by using max() function as mentioned below __

# print("largest number using max() function ",max(list))   #max() :-> maximum value in list  
# print("largest number using max() function ",min(list))   #min()    :-> minimum value in list 



#################################==========================================================###########################################

#This is a Python Program to find the second largest number in a list.





# list1=[]
# value=int(input("enter how many element you want to add in list :"))
# for i in range(0,value):
#     elements=int(input("enter elements "))
#     list1.append(elements)

# list1.sort()
# print("second largest number in list is :",list1[-2])

########================================###################

list1=[]
value=int(input("enter how many element you want to add in list :"))
for i in range(0,value):
    elements=int(input("enter elements "))
    list1.append(elements)
    

print(list1)

m=list1[0]

for i in list1:
    if i>m:
        m=i

print(m)
list1.remove(m)
print(list1) 
   
n=list1[0]
########===============########

for j in list1:
    if i>n:
        n=j

print(n)

 



