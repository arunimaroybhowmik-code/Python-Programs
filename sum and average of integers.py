numbers = []

# Take 10 integers from the user
for i in range(10):
    n = int(input("Enter an integer: "))
    numbers.append(n)

# Find sum without using sum()
total = 0
for n in numbers:
    total = total + n

# Find average
average = total / 10

print("List:", numbers)
print("Sum:", total)
print("Average:", average)
