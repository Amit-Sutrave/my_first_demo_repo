

list=[]

value=int(input("enter how many element you want to add in list :"))
for i in range(0,value):
    elements=int(input("enter elements "))
    list.append(elements)


sum=0
for j in list:
    sum=sum+j

avg=sum//value
print("average is :",avg)




# otherwise you can use sum() function for adding the values in list  >>>

      #  s=sum(list)
      #  print("addition of elements in list by using sum fumction is : ",s)