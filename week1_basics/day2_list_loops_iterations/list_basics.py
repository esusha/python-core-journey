# List basics
# create a list of 5 fruits1

fruits = ["apple", "banana", "grapes", "orange", "papaya"]
def fruits_count(fruits):
	""" returns total number of fruits """
	return f"Fruits list contains {len(fruits)} fruits."

print(fruits_count(fruits)) # 5

# Add a new fruit
fruits.append("mango")

# print updated list
#after adding new fruits print total number of fruits
print(f"list after updating fruit {fruits_count(fruits)}")

#remove a fruit
fruits.remove("papaya")

# print updated list
print(f"list after removing fruit {fruits_count(fruits)}")

#Check if banana is in the list

def check_fruits(fruit_name):
	""" checks if fruit_name is in the fruits list """
	if fruit_name in fruits:
		return f"{fruit_name} in the fruits list"

print(check_fruits('banana')) # banana in the fruits list

# using enumerate to get index and value
def fruits_list(fruits):
    """ prints fruits with index """
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
fruits_list(fruits) # 0: apple 1: banana 2: grapes 3: orange 4: mango

# Zip function to combine two lists
price = [10, 20, 30, 40, 50]
def fruits_price(fruits, price):
    """ prints fruit with price """
    for fruit, price in zip(fruits, price):
        print(f"{fruit}: {price}")
fruits_price(fruits, price) # apple: 1 banana: 2 grapes: 3 orange: 4 mango: 5