# Take input from the user and convert it to an integer
num = int(input("Enter a number: "))

# Store the original number and find the total number of digits
temp = num
num_digits = len(str(num))
sum_of_powers = 0

# Process each digit using a while loop
while temp > 0:
    digit = temp % 10                  # Extract the last digit
    sum_of_powers += digit ** num_digits  # Raise to power and add to sum
    temp //= 10                        # Remove the last digit

# Check if the calculated sum matches the original number
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

