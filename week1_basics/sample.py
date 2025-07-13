squares=[]
for i in range(1, 11):
    squares.append(i*i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)

a,*b,c=(1,2, 3,4)
print(a, b)

dict1 = {"a":1}
dict2 = {"b":2}
merged = {**dict1, **dict2}
merged = dict1 | dict2
print(merged)
