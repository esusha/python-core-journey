# Ask name. age and print name and next year age.

def ask_age():
    """
    This function asks the user for their name and age, then prints a message with their name and age next year.
    
    Returns:
    None
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    next_year_age = age + 1
    return (f"Hello {name.capitalize()}, you will be {next_year_age} old")

print(ask_age())