import random


class Course:
    course_id=random.randint(1,100)

    def __init__(self,course_name,course_class):

        self.course_name=course_name
        self.course_class=course_class



class Student:
    student_id=random.randint(1,100)
    def __init__(self,student_name,student_class):

        self.student_name=student_name

        self.student_class=student_class
