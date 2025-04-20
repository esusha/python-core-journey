# Explore tuples
person = ("Suresh", 35, "Bangalore")

# Accessing tuple elements
name = person[0]
age = person[1]
city = person[2]
print(f"Name: {name}, Age: {age}, City: {city}")  # Name: Suresh, Age: 35, City: Bangalore
# Tuple unpacking
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")  # Name: Suresh, Age: 35, City: Bangalore
# Then make a list of such tuples and loop over them.
people = [
    ("Suresh", 35, "Bangalore"),
    ("Ramesh", 28, "Delhi"),
    ("Rajesh", 40, "Mumbai")
]
# Looping through the list of tuples
for person in people:
    name, age, city = person
    print(f"Name: {name}, Age: {age}, City: {city}")