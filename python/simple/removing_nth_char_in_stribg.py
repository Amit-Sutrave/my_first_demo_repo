# def remove_char(str, n):
      #first_part = str[:n] 
    #   last_part = str[n+1:]
    #   return  last_part
# print(remove_char('Python', 0))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))







string=input("enter string :")
num=int(input("enter char number to delete from string"))

m1_string=string[:num]
mo_string=string[num+1:]
print("old string is :"+string)
print("after removing char string is :"+m1_string+mo_string)