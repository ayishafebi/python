def simple_interest(p, t, senior):
    if senior == "yes":
        r = 12
    else:
        r = 10
    return (p * t * r) / 100

p = float(input("Enter principal amount: "))
t = float(input("Enter time in years: "))
senior = input("Are you a senior citizen? (yes/no): ").lower()

si = simple_interest(p, t, senior)
print("Simple Interest =", si)
