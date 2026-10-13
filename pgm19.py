string=input("Enter a string:")
seen=""
for ch in string:
    if ch not in seen:
        print(ch, ":", string.count(ch))
        seen += ch
    
