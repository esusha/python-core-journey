names = ["Alice", "Bob", "Charlie", "Diana"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
