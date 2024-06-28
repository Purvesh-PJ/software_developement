class Instructor:
    def __init__(self, instructor_id, name, department):
        self.instructor_id = instructor_id
        self.name = name
        self.department = department
        self.courses = []

    def add_course_to_instructor(self, course):
        for crc in self.courses:
            if crc.course_id == course.course_id:
                print("Course exists to instructor courses")
                return
            self.courses.append(course)
            print(f"Course added to instructor")

    def remove_course_from_instructor(self, course):
        for crc in self.courses:
            if crc.course_id != course.course_id:
                print("Course not found in instructor")
                return
            self.courses.remove(course)
            print("Course removed from instructor")

    def get_course_list_from_instructor(self):
        if len(self.courses) > 0:
            for courses in self.courses:
                print(courses)
                return
        else:
            print("no courses to display")
