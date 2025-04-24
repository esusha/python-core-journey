#Explore zip function
# Combine two or more iterables element-wise

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
# Combine names and scores using zip
combined = zip(names, scores)
print(list(combined))  # Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# Unzip the combined list
combined = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
unzipped = zip(*combined)
print(list(unzipped))  # Output: [('Alice', 'Bob', 'Charlie'), (85, 92, 78)]
# Combine three lists using zip 
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
ages = [25, 30, 22]
combined = zip(names, scores, ages)
print(list(combined))  # Output: [('Alice', 85, 25), ('Bob', 92, 30), ('Charlie', 78, 22)]