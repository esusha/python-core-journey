#Returns names of students whose scores are above the threshold.
# Use zip() + filter() + lambda.

def get_students_above_threshold(students, scores, threshold):
    """
    Returns names of students whose scores are above the threshold.
    Use zip() + filter() + lambda.
    """
    # Combine students and scores using zip
    combined = zip(students, scores)
    
    # Filter students based on the threshold
    filtered_students = filter(lambda x: x[1] > threshold, combined)
    
    # Extract names of students who meet the criteria
    result = [student for student, score in filtered_students]
    
    return result

print(get_students_above_threshold(["Alice", "Bob", "Charlie"], [85, 92, 78], 80))  # Output: ['Alice', 'Bob']