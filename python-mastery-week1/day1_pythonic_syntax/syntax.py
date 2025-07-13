# Original -> Refactor the unpythonic code:
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i * i)
result = [x for x in range(10) if x % 2 == 0]
print(result)


# Use built-in functions:
# Given a list of integers, check if all elements are positive
numbers = [1, 3, 7, 0, 5]
# TODO: Use all() to check if all elements > 0
result = all(num > 0 for num in numbers)
print(result)

# Unpacking -> Variable Swapping:
x = 100
y = 200

# TODO: Swap x and y without using a temporary variable
x,y = y,x
print(x, y)


#Tuple Unpacking with Extended Syntax:

data = [10, 20, 30, 40, 50]

# TODO: Unpack to:
#   first = 10
#   middle = [20, 30, 40]
#   last = 50
first, *middle, last = [10, 20, 30, 40, 50]
print(first, middle, last)

# Unpacking Dictionary for Merging:

user_info = {"name": "Alice"}
contact_info = {"email": "alice@example.com"}

# TODO: Merge both dictionaries using unpacking
merge = {**user_info, **contact_info}
print(merge)


#Using Walrus in a while loop:

# TODO: Keep reading integers from input until user enters 0
# Print square of each number

# Example input: 4 → 16
#                5 → 25
#                0 → exit

while (num := int(input("Enter a number (0 to exit): "))) != 0:
    print(f"{num} → {num ** 2}")

# Using Walrus in if condition:

my_list = [1, 2, 3, 4, 5, 6]

# TODO: If the length of the list is more than 4, print it using :=

if (length := len(my_list)) > 4:
    print(f"The list has {length} elements: {my_list}")

#Write a function that takes any number of arguments using *args and returns the sum of only even numbers.

def my_list(*args):
    return sum(args)