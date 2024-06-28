
class Student:
    def __init__(self, student_id, name, email, phone_no):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone_no = phone_no

    def __repr__(self):
        return f"student-id: {self.student_id}\n name: {self.name}\n email: {self.email}\n phone no: {self.phone_no}"


