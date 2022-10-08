import random

from  class_final_2_project import Student
from class_final_2_project import Course
list_student=[]
list_course=[]
ID_list=[]
ID_list_course=[]
add_course_to_student=[]


def check(student_class,course_class):
    if student_class==course_class:
        return +1
    return -1

def display_student_details(list_student):
    for a in list_student:

        print('ID\t|name student\t|class student')
        print('--------------------------------------')
        print(a.student_id, a.student_name, a.student_class)
def display_course_details(list_student):
    for a in list_course:
        print('ID\t|name course\t|class course')
        print('----------------------------------')

        print(a.course_id, a.course_name, a.course_class)


while True:
    print('---------------------------------------------------------')
    print('''Select Choice Please 
    1.Add New Student 
    2.Remove Student 
    3.Edit Student 
    4.Display ALl Students 
    5.Create New Course 
    6.Add course to student 
    7.Display ALl Course
    8.View all added courses for students
    0.Exit''')
    num=int(input('Enter The Number\t|:'))

    if   num==1:
        student_name=input('Enter The name :')
        student_class = input('Enter The class student :')
        if student_class in ['A','B','C']:
            student1=Student(student_name,student_class)
            list_student.append(student1)
            if student1.student_id not in ID_list:
                ID_list.append(student1.student_id)
            else:
                student1.student_id=random.randint(1,100)
                ID_list.append(student1.student_id)

            print(' student saved successfully')
        else:
            print(' just Enter  |A|B|C|')


    elif num==2:
        ID=int(input('Enter ID_student :'))
        if ID in  ID_list:
            W =-1
            for a  in list_student:
                W+=1
                if a.student_id ==ID:
                    del list_student[W]
        else:
            print('user not exist')

    elif num == 3:
        display_student_details(list_student)
        ID=int(input('Enter ID_student :'))
        if ID in  ID_list:
            new_name=input('Enter The New Name :')
            new_class=input('Enter New Class :')
            for a in list_student:
                a.student_name=new_name
                a.student_class=new_class
        else:
            print('user not exist')


    elif num == 4:
        display_student_details(list_student)

    elif num == 5:
        course_name=input('Enter The course name :')
        course_class=input(' select course_class (A-B-C) :')
        course1=Course(course_name,course_class)
        list_course.append(course1)
        if course1.course_id not in ID_list_course:
            ID_list_course.append(course1.course_id)
        else:
            course1.course_id=random.randint(100,200)
            ID_list_course.append(course1.course_id)

        print(' course saved successfully')


    elif num == 6:

        display_student_details(list_student)
        print("_________________________________")
        display_course_details(list_student)
        ID = int(input('Enter ID_student :'))
        if ID in ID_list:
            ID_course=int(input('Enter course_id who joined :'))
            if ID_course in ID_list_course:
                for x in list_course:
                    for y in list_student:
                        return_check = check(y.student_class, x.course_class)
                print(return_check)
                if return_check==1:
                    dictionary = {ID:ID_course }
                    add_course_to_student.append(dictionary)
                else:
                    print('The class of the student must be the same as the class of the course')
            else:
                print('course not exist')
        else:
            print('user not exist')


    elif num == 7:
        display_course_details(list_course)
    elif num==8:
        print(add_course_to_student)
    elif num==0:
        exit()
    else:
        print(' just !!  Enter the number 1|2|3|4|5|6|7|0')