# function with keyword arguments

def introduce(name, age, **kwargs) -> str:
    """
    This function introduces a person with their name, age, and additional information.
    
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    kwargs: Additional keyword arguments for extra information.
    
    Returns:
    str: An introduction message.
    """
    introduction = f"My name is {name} and I am {age} years old."
    
    # Adding additional information if provided
    for key, value in kwargs.items():
        introduction += f" My {key} is {value}."
    
    return introduction
# Example usage     
introduction_message = introduce("Alice", 30, city="New York", hobby="painting")
print(introduction_message)  # Output: My name is Alice and I am 30 years old. My city is New York. My hobby is painting.