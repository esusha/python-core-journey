#explore lambdas, map, and filter
# 1. Lambda function
# 2. Map function
# 3. Filter function    

print("1. Lambda function")
# Lambda function

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6
# Lambda function with multiple arguments
def add(x, y):
    return x + y
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
# Lambda function with default argument
def add(x, y=0):
    return x + y
add = lambda x, y=0: x + y
print(add(2))  # Output: 2
# Lambda function with variable number of arguments
def add(*args):
    return sum(args)
add = lambda *args: sum(args)
print(add(2, 3, 4))  # Output: 9
# Lambda function with keyword arguments
def add(**kwargs):
    return sum(kwargs.values())
add = lambda **kwargs: sum(kwargs.values())
print(add(a=2, b=3))  # Output: 5
# Lambda function with list comprehension
def add(x):
    return [i + 1 for i in x]
add = lambda x: [i + 1 for i in x]
print(add([1, 2, 3]))  # Output: [2, 3, 4]
# Lambda function with dictionary comprehension
def add(x):
    return {i: i + 1 for i in x}
add = lambda x: {i: i + 1 for i in x}
print(add([1, 2, 3]))  # Output: {1: 2, 2: 3, 3: 4}
# Lambda function with set comprehension
def add(x):
    return {i + 1 for i in x}
add = lambda x: {i + 1 for i in x}
print(add([1, 2, 3]))  # Output: {2, 3, 4}
# Lambda function with generator expression
def add(x):
    return (i + 1 for i in x)
add = lambda x: (i + 1 for i in x)
print(add([1, 2, 3]))  # Output: <generator object <lambda>.<locals>.<genexpr> at 0x7f8c8c0b4d60>