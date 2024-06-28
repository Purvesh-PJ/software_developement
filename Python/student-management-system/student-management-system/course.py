
class Course:
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        for stud in self.students:
            if stud.student_id == student.student_id:
                print(f"Student already acquired this course ${self.course_name}")
                return
        self.students.append(student)
        print(f"${student.name} registered course ${self.course_name}")

    def remove_student(self, student):
        for stud in self.students:
            if stud.student_id == student.student_id:
                self.students.remove(student)
                print(f"Student ${student.name} removes successfully")
                return
        return print("Student not found in course to remove")

    def display_course_joined_students(self):
        for stud in self.students:
            print(f"student-id: ${stud.student_id}\n student name: ${stud.name}")
            return

    def __repr__(self):
        return f"Course Created name: ${self.course_name}\n instructor: ${self.instructor}"

