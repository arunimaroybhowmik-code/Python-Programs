def add_entry(d):
    key = input("Enter new key: ")
    value = input("Enter new value: ")
    d[key] = value


def reassign_dict(d):
    d = {"new": "dictionary"}
    print("Inside reassign_dict():", d)


# Taking dictionary from user
d = {}

n = int(input("Enter number of entries: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("\nOriginal dictionary:", d)

# Calling add_entry()
add_entry(d)
print("After add_entry():", d)

# Calling reassign_dict()
reassign_dict(d)
print("After reassign_dict():", d)
