value=int(input("enter values :"))


lst=[]
for i in range(0,value):
    sorry=int(input("enter elements "))
    lst.append(sorry)

print(lst)

lst=list(dict.fromkeys(lst))


print(lst)