numbers = []

# Take 7 integers from the user
for i in range(7):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Assume first number is smallest and largest
smallest = numbers[0]
largest = numbers[0]

# Find smallest and largest
for num in numbers:
    if num < smallest:
        smallest = num

    if num > largest:
        largest = num

print("List:", numbers)
print("Smallest:", smallest)
print("Largest:", largest)
