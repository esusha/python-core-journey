# file write mode
# 'w' is the mode for write
# 'a' is the mode for append
# 'x' is the mode for exclusive creation
# 'r+' is the mode for read and write
# 'w+' is the mode for write and read
# 'a+' is the mode for append and read
# 'x+' is the mode for exclusive creation and read

# # Open a file in write mode
# # write mode is used to write the content of the file
# # 'w' is the mode for write
try:
    file = open('file.txt', 'a')
    # Write to the file
    file.write("Hello World--------")
    # Close the file
    file.close()
except FileNotFoundError:
    print("File not found. Please check the file path.")
finally:
    # Ensure the file is closed even if an error occurs   
    if 'file' in locals():
        print("File is closed")
        file.close()
# # Open a file in append mode
# # append mode is used to append the content of the file
# # 'a' is the mode for append
# try: