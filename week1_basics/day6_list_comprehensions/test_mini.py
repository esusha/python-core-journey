# Write a function:
# Use list comprehension

# Rules:

# If divisible by 3: "Fizz"

# If divisible by 5: "Buzz"

# If both: "FizzBuzz"

# Else: the number as string

def main(n: int) -> list[str]:
    """
    Returns a list of 'Fizz', 'Buzz', 'FizzBuzz', or the number as a string for values 1 to n.
    """
    return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, n + 1)]
# Test cases 

if __name__ == "__main__":
    # Test cases
    print(main(15))
    print(main(20))
    print(main(30))
    print(main(50))
    print(main(100))