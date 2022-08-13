import random

value=int(input("enter number ;"))

a=[]
for i in range(value):
    a.append(random.randint(10,50))
    
print(a)


