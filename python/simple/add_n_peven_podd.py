list=[-1,-2,-3,1,2,3,4,5,0]

ne=[]
po=[]
s=0
for i in list:
    if i<0:
        ne.append(i)
    else:
        po.append(i)

print(ne)
print(po)


for o in ne:
    s=s+o
      
print("addition of negative numbers is :",s)  

add_ev=0
add_po=0
for j in po:
    if j%2==0:
        add_ev=add_ev+j
    else:
        add_po=add_po+j
   
print("addition of even numbers is :",add_ev)

print("addition of odd numbers is :",add_po)