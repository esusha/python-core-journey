# function using args and kwargs

def greating(*args):
    for arg in args:
        print(f"Hello {arg}!")
# Example usage
greating("Alice", "Bob", "Charlie")