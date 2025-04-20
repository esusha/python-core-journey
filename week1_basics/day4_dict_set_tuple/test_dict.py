#Dictionary exploration 

students = {"Alice": 85, "Bob": 92, "Charlie": 78}

#Add a new student

students["sachin"] = 90
print(f"After adding new student: {students}") # Added new student: 90

#Update a score

students["Alice"] = 99  # updated Alice score
print(f"After updating Alice's score: {students}") # Updated Alice's score: 99

#Delete a student

del students["Bob"]
print(f"After deleting Bob: {students}") # Deleted Bob: 92

#Print all students and scores

def print_students(students):
    for student, scores in students.items():
	    print(f"{student}: {scores}")

print(f"All students and scores:")
print_students(students) # All students and scores: Alice: 99 Charlie: 78 sachin: 90
#Check if a student is in the dict

if "Alice" in students.keys():
	print("Alice is in the dict")
