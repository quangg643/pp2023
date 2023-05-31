class Student():
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name 
        self.dob = dob
        self.mark = {}
class Course():
     def __init__(self, cid, cname, credits):
        self.id = cid
        self.name = cname
        self.credits = credits
class StudentMarkManagement:
    def __init__(self, mark = None):
        self.students = []
        self.courses = []
        self.mark = mark 
        self.marks_dict = {}
        self.list_gpa = []