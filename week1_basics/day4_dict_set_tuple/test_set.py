#Explore set operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Union
set_union = set1.union(set2)
print(f"Union: {set_union}")  # Union: {1, 2, 3, 4, 5, 6, 7}

# Intersection
set_intersection = set1.intersection(set2)
print(f"Intersection: {set_intersection}")  # Intersection: {4, 5}
# Difference
set_difference = set1.difference(set2)
print(f"Difference: {set_difference}")  # Difference: {1, 2, 3}


#Check if a number exists in either set
def check_number_in_sets(number):
    if number in set1 or number in set2:
        return f"{number} exists in either set1 or set2"
    else:
        return f"{number} does not exist in either set1 or set2"
print(check_number_in_sets(3))  # 3 exists in either set1 or set2

#Check if a number exists in both sets
def check_number_in_both_sets(number):
    if number in set1 and number in set2:
        return f"{number} exists in both set1 and set2"
    else:
        return f"{number} does not exist in both set1 and set2"
print(check_number_in_both_sets(4))  # 4 exists in both set1 and set2