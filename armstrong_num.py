# Python program to check if a number is an Armstrong number or not
num = int(input("Enter a number: "))  # Take input from the user

# Initialize the sum
sum = 0

# Find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# Display the result
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

    


# Python program to check if a number is an Armstrong number or not
num = 1634

# Calculate the number of digits
order = len(str(num))

# Initialize the sum
sum = 0

# Find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Display the result
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")



    