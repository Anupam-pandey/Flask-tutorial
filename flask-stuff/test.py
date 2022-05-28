class Student:
    def __init__(self):
        self.grades = (90,90,90,83,78,67)
    def average(self):
        return sum(self.grades)/len(self.grades)



student = Student()
print(Student.average(student))