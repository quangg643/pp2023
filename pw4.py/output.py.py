import numpy as np
import math 
from input import *
class Output(Input):
    def __init__(self,id = str(),name = str(),dob = str(),cid = str(),cname = str(),credits = int(),mark = None):
        input.__init__(self,id,name,dob,cid,cname,credits,mark)
        self.list_gpa = []
    def display_students_info(self):
        for student in self.stu_list:
            print("studetn id: ",student[0])
            print("studetn name: ",student[1])
            print("date of birth: ",student[2])

    def display_course_info(self):
        for course in self.course_list:
            print("course id: ",course[0])
            print("course name: ",course[1])
            print("this course has numbers of credits: ",course[2])

    def get_mark(self,stu_name,course_name):
        return self.mark_dict.get((stu_name,course_name),None)
    def display_marks(self):
        course_name = input("Enter the course name you want to display marks: ")
        if course_name not in self.list_course_name:
            print("No course was found")
            return 0
        else:
            print(f"Marks for {course_name}")
            for self.stu_name in self.list_student_name:
                mark = self.get_mark(self.stu_name,course_name)
                print(f"{self.stu_name} : {mark}")

    def calculate_gpa(self):
        credits_array = np.array([list_credits])
        for self.stu_name in list_student_name:
            product_array = np.array([])
            for i in range(len(list_course_name)):
                course_name = list_course_name[i]
                mark = self.marks.get_marks(self.stu_name, course_name)
                if mark is None:
                    print(f"No mark found for {self.su_name}")
                    continue
                product = mark * list_credits[i]
                product_array = np.append(product_array, product)
            total_credits = np.sum(credits_array)
            if len(product_array) > 0:
                gpa = round(np.sum(product_array ) / total_credits,2)
                self.list_gpa.append(gpa)
                print(f"Gpa for {self.stu_name} : {gpa}")

    def sort_student_by_gpa(self):
        self.calculate_gpa()
        gpa_dict = dict(zip(list_student_name, self.list_gpa))
        sorted_gpa_dict = dict(sorted(gpa_dict.items(), key=lambda x: x[1], reverse=True))
        print("After students's name are sorted by GPA (descencing):")
        for student, gpa in sorted_gpa_dict.items():
            print(f"GPA of {student} : {gpa}")