value=int(input("enter number which upto series you want :"))

t1=0
t2=1
t3=t1+t2

print(t1)
print(t2)

for i in range (0,value):
    print(t3)
    t1=t2
    t2=t3
    t3=t1+t2
    
