# function with default arguments

def greet(name, greeting="Hello") -> str:
    """
    This function greets a person with a given greeting.
    
    Parameters:
    name (str): The name of the person to greet.
    greeting (str): The greeting message. Defaults to "Hello".
    
    Returns:
    str: A greeting message.
    """
    return f"{greeting}, {name}!"

# Example usage
greeting_message = greet("Alice")
print(greeting_message)  # Output: Hello, Alice!
# Example usage with a custom greeting
custom_greeting_message = greet("Bob", "Hi")
print(custom_greeting_message)  # Output: Hi, Bob!