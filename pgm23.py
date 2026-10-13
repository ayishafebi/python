d={}
n= int (input("Enter number of items:"))
for i in range(n):
    key= input("Enter key:")
    value=int(input("Enter value:"))
    d[key]=value
    print("Orginal dictionary:",d)
    ascending = dict(sorted(d.items()))
    descending=dict(sorted(d.items(),reverse=True))
    print("Ascending order:",ascending)
    print("Descending order:",descending)
