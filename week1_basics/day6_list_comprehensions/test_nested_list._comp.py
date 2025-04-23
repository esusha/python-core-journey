#Nested List Comprehension

#Create a 3x3 matrix using list comprehension:
matrix = [[j for j in range(3)] for i in range(3)]
print(f"3x3 matrix using list comprehension --> {matrix}")
#Create a 3x3 matrix using nested for loops:
matrix_2 = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(j)
    matrix_2.append(row)
print(f"3x3 matrix using nested for loops --> {matrix_2}")

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3 matrix using list comprehension with multiplication --> {matrix}")