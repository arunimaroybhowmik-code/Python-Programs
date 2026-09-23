def maximum(a, b):
    if a > b:
        return a
    else:
        return b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = maximum(num1, num2)

print("Greater number is:", result)
