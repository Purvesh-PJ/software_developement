from student import Student
from university import University
from course import Course
from instructor import Instructor


def __init__():
    university = University()

    while True:
        print(f"###### Welcome University ######")
        print("1] Register student to university")
        print("2] Register instructor to university")
        print("3] University affiliated courses")
        print("4] Display all students")
        print("5] Display all courses")
        print("0] Exit")
        print("################################")

        number = input("Enter the number: ")

        if number == '1':
            student_id = input("Enter student Id: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            phone_no = input("Enter student phone no: ")
            student = Student(student_id, name, email, phone_no)
            university.add_student_to_university(student)

        elif number == '2':
            instructor_id = input("Enter instructor id: ")
            name = input("Enter instructor name: ")
            department = input("Enter instructor department: ")
            instructor = Instructor(instructor_id, name, department)
            university.add_instructor(instructor)

        elif number == '3':
            course_id = input("Enter Course id: ")
            course_name = input("Enter course name: ")
            instructor_name = input("Enter instructor name: ")
            course = Course(course_id, course_name, instructor_name)
            university.add_course(course)

        elif number == '4':
            university.display_students()

        elif number == '5':
            university.display_courses()

        elif number == '0':
            print("Exiting the program.")
            break

        else:
            print("Enter valid number")


if __name__ == "__init__":
    __init__()
