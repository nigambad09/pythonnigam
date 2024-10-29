# Autpmation classs in OOPs
#  automation tester blueprint (
# Class -Student, Courses
# Objeect -name and coursename
# name - ram sham
# cousre - manual automation

class Student:
    name = None
    course = None

    def stu_name(self):
        print("kids",self.name)

    def stu_course(self):
        print("course name ", self.course)

sham_obj = Student()
jack_obj = Student()

sham_obj.name = "Sham"
jack_obj.name = "Jack"

sham_obj.course = "Auto"
jack_obj.course = "Manual"

sham_obj.stu_name()
jack_obj.stu_course()