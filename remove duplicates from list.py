numbers = []

n = int(input("Enter the number of elements: "))

# Take integers from user
for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Remove duplicates
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List after removing duplicates:", unique)
