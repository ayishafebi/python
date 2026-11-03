numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0

for num in numbers:
    total = total + num

print("Sum of all items in the list =", total)
