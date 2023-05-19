class Student():
    def __init__(self,id = str(),name = str(),dob = str()):
        self.id = id
        self.name = name
        self.dob = dob
        self.stu_list = []
class Course():
    def __init__(self,cid = str(),cname = str(),credits = int()):
        self.cid = cid
        self.cname = cname
        self.credits = credits
        self.course_list = []
class Mark():
    def __init__(self,mark = None):
        self.mark = mark
        self.mark_dict = {}