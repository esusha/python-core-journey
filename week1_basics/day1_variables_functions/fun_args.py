# function using args and kwargs

def greating(*args):
    """Returns a greeting message with the provided name."""
    for arg in args:
        print(f"Hello {arg}!")
# Example usage
greating("Alice", "Bob", "Charlie")