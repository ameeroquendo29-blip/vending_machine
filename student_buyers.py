class Student:
    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age

class EngineeringStudent(Student):
    def __init__(self, student_name, student_age, engineering_department):
        super().__init__(student_name, student_age)
        self.engineering_department = engineering_department