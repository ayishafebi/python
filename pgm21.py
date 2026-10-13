words = input("enter words seprated by spaces:").split()
longest = max(words,key=len)
print("Longest word:",longest)
print("length:",len(longest))
