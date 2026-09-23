# Taking 5 fruits from the user
fruits = []

for i in range(5):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

# Print 2nd and 4th items
print("2nd item:", fruits[1])
print("4th item:", fruits[3])

# Replace last item with Mango
fruits[-1] = "Mango"

# Print updated list
print("Updated list:", fruits)
