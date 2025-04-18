# Ask name. age and print name and next year age.

def main():
    """
    This function asks the user for their name and age, then prints a message with their name and age next year.
    
    Returns:
    None
    """
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
        next_year_age = age + 1
        return (f"Hello {name.capitalize()}, you will be {next_year_age} old")
    except ValueError:
        return "Please enter a valid age."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    result = main()
    print(result)