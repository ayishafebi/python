
# Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Main program
n = int(input("Enter the number of terms: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + (i ** 3) / factorial(i)

print("Sum of the series =", sum)

