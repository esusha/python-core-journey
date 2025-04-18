# Write a function that takes a list of numbers and returns a new list with only the even numbers using a list comprehension.

def get_even_numbers(numbers):
	"""
	Returns a list of even numbers from the input list.
	Skips any non-integer values in the list.
	
	Parameters:
	numbers (list): A list containing values of any type
	
	Returns:
	list: A list containing only the even integer values from the input list
	"""
	return [number for number in numbers if isinstance(number, int) and number % 2 == 0]

# Example with only integers
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [2, 4, 6, 8, 10]

# Example with mixed data types
mixed_list = [1, 2.5, "three", 4, True, 6, None, 8, [9], 10]
print(get_even_numbers(mixed_list)) # [2, 4, 6, 8, 10]

