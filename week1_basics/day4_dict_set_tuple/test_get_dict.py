#explore get() method in dictionary
# get() method in dictionary
# The get() method returns the value for the specified key if the key is in the dictionary.
# If the key is not found, it returns the default value (None if not specified).
# The get() method is useful when you want to avoid KeyError exceptions when trying to access a key that may not exist in the dictionary.

students = {"Alice": 85, "Bob": 92, "Charlie": 78}

def get_student_score(student_name):
    """
    Returns the score of the specified student.
    If the student is not found, returns None.
    
    Parameters:
    student_name (str): The name of the student to look up
    
    Returns:
    int or None: The score of the student or None if not found
    """
    return students.get(student_name, "Not found")

print(get_student_score("SAm"))  