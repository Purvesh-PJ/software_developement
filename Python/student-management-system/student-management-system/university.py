class University:
    def __init__(self):
        self.students = []
        self.courses = []
        self.instructors = []

    def add_student_to_university(self, student):
        for stud in self.students:
            if stud.student_id == student.student_id:
                print("Student already exists")
                return
        self.students.append(student)
        print("Student added to university")

    def add_course(self, course):
        for course_id in self.courses:
            if course_id == course.course_id:
                print("course already exists")
                return
        self.courses.append(course)
        print(f"Course {course.course_name} added to university")

    def add_instructor(self, instructor):
        for inst in self.instructors:
            if inst.instructor_id == instructor.instructor_id:
                print("Instructor exists in university")
            return
        self.instructors.append(instructor)
        print(f"Instructor added in university with id : {instructor.instructor_id}")

    def find_student_by_id(self, student_id):
        for stud in self.students:
            if stud.student_id == student_id:
                print(f"student-id: {stud.student_id}\n name: {stud.name}")
                return
        print(f"student not found with id: {student_id}")

    def find_course_by_id(self, course_id):
        for crc in self.courses:
            if crc.cource_id == course_id:
                print(f"course-id: {crc.cource_id}\n course-name: {crc.course_name}")
                return
        print(f"Course not found with id: {course_id}")

    def find_instructor_by_id(self, instructor_id):
        for ins in self.instructors:
            if ins.instructor_id == instructor_id:
                print(f"instructor-id: {ins.instructor_id}\n instructor-name: {ins.name}")
                return
        print(f"Instructor not found with id: {instructor_id}")

    def display_students(self):
        if not self.students:
            print("No students")
            return
        for stud in self.students:
            print(f"Student id: {stud.student_id}\nname: {stud.name}\n")

    def display_courses(self):
        if not self.courses:
            print("No courses found")
            return
        for crc in self.courses:
            print(crc.cource_id, " ", crc.course_name)
