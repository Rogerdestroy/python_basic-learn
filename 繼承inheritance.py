"""
繼承 inheritance
person.py 
"""
from person import Person

class Student(Person):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
        
    def print_school(self):
        print(self.school)

"""
class Student(Person):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        
    def print_name(self):
        print(self.name)
    
    def print_age(self):
        print(self.age)
        
    def print_school(self):
        print(self.school)
"""
