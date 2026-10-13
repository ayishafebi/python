numbers = list(map(int, input("Enter integers:").split()))
positive = [n for n in numbers if n >0]
print("positive numbers:",positive)

n=int(input("Enter N:"))
squares=[i*i for i in range(1, n+1)]
print("Squares:", squares)


word= input("Enter a word:")
vowels=[ch for ch in word if ch.lower() in "aeiou"]
print("vowels:",vowels)

word= input("Enter  a word:")
values=[ord(ch) for ch in word]
print("Ordinal values:",values)
