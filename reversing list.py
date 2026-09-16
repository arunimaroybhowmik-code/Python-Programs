numbers = []

n = int(input("Enter the number of elements: "))

# Take elements from user
for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Reverse the list without reverse() or slicing
reversed_list = []

for i in range(n - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)
