# enumerate Iterate with index + value combo

# enumerate is a built-in function in Python that allows you to loop over an iterable (like a list or a string) and get both the index and the value of each item in the iterable.

colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

colors = ("red", "green", "blue")
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

text = "hello"
for index, char in enumerate(text):
    print(f"Index: {index}, Character: {char}")
# Enumerate with start parameter
# You can also specify a starting index by passing a second argument to enumerate.
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):
    print(f"Index: {index}, Color: {color}")
# Output: