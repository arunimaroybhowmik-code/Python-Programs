def remove_last(lst):
    lst.pop()


n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)

print("Original list:", numbers)

remove_last(numbers)

print("List after removing last element:", numbers)
