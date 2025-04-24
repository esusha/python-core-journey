#Explore map, filter and lambda functions
# 1. Map function
# Apply a function to every item in an iterable
# get squares of numbers using map
nums = [1, 2, 3, 4, 5]
x = map(lambda x: x ** 2, nums)
print(list(x))  # Output: [1, 4, 9, 16, 25]

# filter function
#Filter elements from an iterable based on a condition
# Filter only even numbers
nums = [10, 15, 20, 25, 30]
x = filter(lambda x: x % 2 == 0, nums)
print(list(x))  # Output: [10, 20, 30]

# Filter numbers greater than 20

x = filter(lambda x : x> 20, nums)
print(list(x))