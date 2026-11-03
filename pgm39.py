def add(*args):
    total = 0
    for num in args:
        total += num
    return total

numbers = list(map(int, input("Enter integers : ").split()))

print("Sum =", add(*numbers))
