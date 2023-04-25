from domain import *
import math

class Input(Student,Course,StudentMarkManagement):
    list_course_name = []
    list_student_name = []
    list_credits = []
    def __init__(self, id, name, dob, cid, cname, credits, mark):
        Student.__init__(self,id,name,dob)
        Course.__init__(self,cid,cname,credits)
        Mark.__init__(self,mark)
    def add_student(self, student):
        self.students.append(student)
    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    def input_student_information(self):
        n_students = int(input("Enter number of student: "))
        for i in range(n_students):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.add_student(student)

    def list_students(self):
        print("List of students: ")
        for student in self.students:
            print(student)

    def __str__(self):
        return f"{self.id} - {self.name} ({self.dob})"
    def add_course(self, course):
        self.courses.append(course)
    def get_course(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None
    
    def add_credits(self):
        return self.credits
    def get_credits(self):
        self.credits = int(input(f"Enter credits for this course: "))
        list_credits.append(self.credits)

    def input_course_information(self):
        n_courses = int(input("Enter number of course: "))
        for i in range(n_courses):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            course = Course(id, name) 
            self.add_course(course)

    def list_courses(self):
        print("list of course: ")
        for course in self.courses:
            print(course)

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    def __init__(self, mark = None):
        self.students = []
        self.courses = []
        self.mark = mark
        self.marks_dict = {}
        self.list_gpa = []

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks
    def get_marks(self, course_name, stu_name):
        return self.marks_dict.get((stu_name, course_name), None)
    def get_marks(self, course_id):
        return self.add_marks.get(course_id)
    
    def input_student_marks(self):
        course_id = input("Enter course id: ")
        course = self.get_course(course_id)
        if course is None:
            print("Invalid course id.")
            return
        for student in self.students:
            marks = float(input(f"Enter marks for {student.name}: "))
            student.add_marks(course_id ,marks)
    def show_student_marks(self):
        course_id = input("Enter course id: ")
        course = self.get_course(course_id)
        if course is None:
            print("Invalid course id: ")
            return
        print(f"Marks for {course.name}:")
        for student in self.students:
            marks = student.get_marks(course_id)
            if marks is not None:
                print(f"{student.name}: {marks}")

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