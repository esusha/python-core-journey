#list comphensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#squares of given numbers
squares = [x**2 for x in nums]
print(f"squares of the given number --> {squares}")

#even numbers
evens = [x for x in nums if x % 2 == 0]
print(f"even numbers from the given list --> {evens}")  

#squares of even numbers
squares_of_evens = [x**2 for x in nums if x % 2 == 0]   
print(f"squares of even numbers from the given list --> {squares_of_evens}")

#If number is even, return the number, else return 0
evens_or_zero = [x if x % 2 == 0 else 0 for x in nums]
print(f"if number is even, return the number, else return 0 --> {evens_or_zero}")

