# Squares of numbers from 0 to 9
Squares = [x*x for x in range(10)]
print(Squares)

# Even numbers from 0 to 20

even_num = [x for x in range(21) if x %2 == 0]
print(even_num)

# Upper case conversion
words = ['python', 'is', 'awesome']
upper_conv = [x.upper() for x in words]
print(upper_conv)