with open("names.txt", "a+") as file:
    file.write("King\n")
    file.write("Queen\n")
    file.seek(0) 
    print(file.read())