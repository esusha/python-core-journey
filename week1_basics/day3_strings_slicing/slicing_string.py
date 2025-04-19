#As part of this we will explore string slicing
# string slicing
# string slicing is a technique used to extract a portion of a string
# it allows you to create a new string by specifying a range of indices
# string slicing is done using the square brackets [] and the colon : operator
# the syntax for string slicing is:
# string[start:end:step]
# where:
# - start is the index where the slice begins (inclusive)
# - end is the index where the slice ends (exclusive)
# - step is the number of characters to skip (optional)
#

message = "Mastering Python is rewarding"
print(len(message))  
#First 5 characters
print(message[:5])  # Maste
#Last 5 characters
print(message[-5:])  # rding
#Every second character
print(message[::2])  
#Reversed string
print(message[::-1])  # gnidarowe si nohtyP gniretsam