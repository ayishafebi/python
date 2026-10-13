numbers=list(map(int,input("Enter integers:").split()))
result=[]
for n in numbers:
    if n % 2 !=0:
        result.append(n)
print("list after removing even numbers:",result)        
