#Write a small loop that keeps asking the user to enter a number until they enter 0.

while True:
    try:
        number = int(input("Enter a number (0 to exit): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if number == 0:
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {number}")