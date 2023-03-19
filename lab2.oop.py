class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks

    def get_marks(self, course_id):
        return self.marks.get(course_id)

    def __str__(self):
        return f"{self.id} - {self.name} ({self.dob})"


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id} - {self.name}"


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_course(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def input_student_information(self):
        n_students = int(input("Enter number of students: "))
        for i in range(n_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (dd-mm-yyyy): ")
            student = Student(id, name, dob)
            self.add_student(student)

    def input_course_information(self):
        n_courses = int(input("Enter number of courses: "))
        for i in range(n_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(id, name)
            self.add_course(course)

    def input_student_marks(self):
        course_id = input("Enter course ID: ")
        course = self.get_course(course_id)
        if course is None:
            print("Invalid course ID.")
            return
        for student in self.students:
            marks = float(input(f"Enter marks for {student.name}: "))
            student.add_marks(course_id, marks)

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        course_id = input("Enter course ID: ")
        course = self.get_course(course_id)
        if course is None:
            print("Invalid course ID.")
            return
        print(f"Marks for {course.name}:")
        for student in self.students:
            marks = student.get_marks(course_id)
            if marks is not None:
                print(f"{student.name}: {marks}")


def main():
    smm = StudentMarkManagement()
    smm.input_student_information()
    smm.input_course_information()

    while True:
        print("\n1. Input student marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            smm.input_student_marks()
        elif choice == 2:
            smm.list_students()
        elif choice == 3:
            smm.list_courses()
        elif choice == 4:
            smm.show_student_marks()
        elif choice == 5:
            break
if __name__ == "__main__":
    main()