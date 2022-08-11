


class College:

    college_name = "Edyoda"                     # static/class variable

    def __init__(self,student_name,student_rno):
        self.stud_name = student_name
        self.stud_rno = student_rno

    def display(self):
        return f"Name : {self.stud_name} | Rno : {self.stud_rno}"

    @classmethod    
    def get_college_name(cls):
        return cls.college_name

    @classmethod
    def set_college_name(cls,college_name):
        cls.college_name = college_name

    

college = College("Bharati",24)
print(college.display())
print(college.get_college_name())

college.set_college_name("Coder")
print(college.get_college_name())

print(College.get_college_name())