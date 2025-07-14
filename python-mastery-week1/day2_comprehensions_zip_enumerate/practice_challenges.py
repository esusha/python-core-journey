#Find common elements from two lists using zip() and list comprehension.
list1 = [1, 2, 3, 4, 5]
list2 = [5, 2, 3, 8, 0]

common = [a for a, b in zip(list1, list2) if a==b]
print(common)

#Create a dict of squares for even numbers from 1 to 10.

dict_squares = {i: i**2 for i in range(1,11) if i % 2 ==0}
print(dict_squares)

#Replace all spaces in a string with - using list comprehension and join().

text = "python is powerfule"

text_1 = "".join(['-' if ch==" " else ch for ch in text])
print(text_1)


#Make a frequency dict of words in a sentence.

text = "learn python fast"
indexed = {i: word for i, word in enumerate(text.split())}

print(indexed)