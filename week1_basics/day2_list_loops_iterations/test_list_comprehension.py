#Convert a list of numbers to a new list containing only their squares — using list comprehension.
list_of_numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in list_of_numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
# Convert a list of strings to a new list containing their lengths — using list comprehension.
list_of_strings = ["apple", "banana", "cherry"]
lengths = [len(string) for string in list_of_strings]
print(lengths)  # Output: [5, 6, 6]

def fruits_length(fruits):
    """ returns length of each fruit in the list """
    for fruit, length in zip(fruits, lengths):
        print(f"{fruit}: {length}")
fruits_length(list_of_strings)  # apple: 5 banana: 6 cherry: 6