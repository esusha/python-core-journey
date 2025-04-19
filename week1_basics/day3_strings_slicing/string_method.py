# As part of this we will explore string methods
# string methods
# string methods are built-in functions that can be used to manipulate and analyze strings
# they are called methods because they are associated with string objects and can be called on them
# string methods are called on string objects using the dot notation
# for example: string_object.method_name(arguments)
# string methods are used to perform various operations on strings, such as:
# - converting case (upper, lower, title)
my_string = "hello world"

def string_methods(my_string):
    """ demonstrates string methods """
    print(my_string.upper())  # HELLO WORLD
    print(my_string.lower())  # hello world
    print(my_string.title())  # Hello World
    print(my_string.capitalize())  # Hello world
    print(my_string.swapcase())  # HELLO WORLD
    print(my_string.startswith("hello"))  # True
    print(my_string.endswith("world"))  # True
    print(my_string.find("world"))  # 6
    print(my_string.index("world"))  # 6
    print(my_string.replace("world", "Python"))  # hello Python
    print(my_string.split())  # ['hello', 'world']
    print(my_string.join(["hello", "world"]))  # hello world
    print(my_string.strip())  # hello world
    print(my_string.lstrip())  # hello world
    print(my_string.rstrip())  # hello world
    print(my_string.count("o"))  # 2
    print(my_string.isalpha())  # False
    print(my_string.isdigit())  # False
    print(my_string.isalnum())  # False
    print(my_string.isnumeric())  # False
    print(my_string.isspace())  # False
    print(my_string.isprintable())  # True
    print(my_string.istitle())  # True
    print(my_string.islower())  # False
    print(my_string.isupper())  # False
    print(my_string.isdecimal())  # False
    print(my_string.startswith("hello"))  # True
    print(my_string.endswith("world"))  # True
    print("hello" in my_string)  # True
    print("Python" in my_string)  # False
    print("hello" not in my_string)  # False



