
a = int(input("Enter first num:"))
b = int(input("Enter sec num:"))
c = int(input("Enter third num:"))

if a >= b and a >= c:
    print("Biggest", a)
elif b >= a and b >= c:
    print("Biggest", b)
else:
    print("Biggest", c)



