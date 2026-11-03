def compare(s1, s2, n):
    return s1[:n] == s2[:n]

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter number of characters: "))

print(compare(s1, s2, n))
