def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
n = int(input("Enter the number of terms: "))
total = 0

for i in range(1, n + 1):
    total = total + (i ** 3) / factorial(i)

print("Sum of the series =", total)
