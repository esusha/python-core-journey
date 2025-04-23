# String Filtering with Comprehensions

words = ["apple", "banana", "cherry", "date", "fig", "grape"]

print([fruit for fruit in words if "a" in fruit])

# Convert all words to uppercase using comprehension

print([fruit.upper() for fruit in words])