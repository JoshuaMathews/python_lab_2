from dataclasses import dataclass

# Our main student dataclass.
@dataclass
class Student:
    # This automatically initializes our variables but since we're giving variables
    # it can infer what we want so this is equal to __init__(self, name, school_id, gpa)
    # and it helps remove a lot of the boilerplate that we'd have to do otherwise.
    name: str
    school_id: str
    gpa: float

# We provide the variables and since it handles init etc for us
# all we (the programmers) have to worry about is focusing on our code.
josh = Student('Josh', 'qwerty', 3.9)
print(josh.name)
print(josh.school_id)
print(josh.gpa)

test = Student('Testing Testington', '123test123', 4.0)
print(test.name)
print(test.school_id)
print(test.gpa)