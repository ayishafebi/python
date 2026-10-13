string=input("enter a string:")
if len(string) < 3:
    result = string
elif string.endswith("ing"):
     result = string + "1y"
else:
    result=string+"ing"
print(result)    

