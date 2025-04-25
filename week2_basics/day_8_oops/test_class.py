# explore class oops

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"

class Teacher():
    pass

# Example usage
if __name__ == "__main__":
    # Create a Person object
    john = Person("John", 25)
    john.greet()  # Output: Hello, my name is John and I am 25 years old.
    john.birthday()  # Output: Happy birthday John! You are now 26 years old.
    # Create a Student object
    jane = Student("Jane", 20, "S12345")
    jane.greet()  # Output: Hello, my name is Jane and I am 20 years old.
    jane.birthday()  # Output: Happy birthday Jane! You are now 21 years old.
    jane.study("English")  # Output: Jane is studying.
    # Print the string representation of the objects
    print(john)  # Output: Person(name=John, age=26)
    print(jane)  # Output: Student(name=Jane, age=21, student_id=S12345)
    s = Student("Sachin", 45, "1233")
    print(isinstance(s, Person))  # Output: True
    print(issubclass(Student, Person))

    print(s)  # Output: Student(name=Sachin, age=45, student_id=Maths)