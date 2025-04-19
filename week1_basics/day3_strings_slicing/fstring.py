#explore fstring

while True:
    try:
        name = input("Enter your name: ")
        score = float(input("Enter your score: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    print(f"Hello {name}, your score is {score:.2f}.")
    break