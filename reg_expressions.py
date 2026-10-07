import re

text = input("Enter a sentence:")

# 1. re.search() - Find the first match
match = re.search(r"\d+", text)
print("1. search():", match.group() if match else "Not found")


# 2. re.match() - Check only at the beginning
match = re.match(r"Hello", text)
print("2. match():", match.group() if match else "Not found")


# 3. re.findall() - Find all matching values
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print("3. findall():", emails)


#5. re.split() - Split a string using a pattern
words = re.split(r"[,; ]+", text)
print("4. split():", words)


# 4. re.sub() - Replace matching text
hidden_email = re.sub(
    r"[\w.-]+@[\w.-]+\.\w+",
    "[EMAIL HIDDEN]",
    text
)
print("7. sub():")
print(hidden_email)
