thistuple = ("apple", "banana", "cherry")
lst=list(thistuple)
# print(lst[1])
lst.remove("banana")
thistuple=tuple(lst)
print(thistuple)
   