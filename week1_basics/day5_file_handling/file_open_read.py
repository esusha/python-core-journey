import  time
# Explore file handing in Python
# Open a file
# Open a file in read mode
# read mode is used to read the content of the file
# 'r' is the mode for read
try:
    file = open('file.txt', 'r')
    # Read the file 
    content = file.read()
    # Print the content
    print(content)
    # Close the file
    file.close()
except FileNotFoundError:
    print("File not found. Please check the file path.")
finally:
    # Ensure the file is closed even if an error occurs   
    if 'file' in locals():
        print("File is closed")
        file.close()
