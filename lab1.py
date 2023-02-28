# define a dictionary to store student, marks and courses inforrmation 
students = []
marks = []
courses = []

def input_number_students():
    return int(input("Enter number of students:"))

def input_student_infor():
    id = input("Enter student ID:")
    name = input("Enter student name:")
    dob = input("Enter student date of birth:")
    students[student_id] = {"name": student_name, "dob": student_dob}

no_students = input_number_students()
for i in range(no_students):
    students += [input_student_infor()]

def input_number_courses():
    return int(input("Enter number of courses:"))

def input_courses_infor():
    courses_id = input("Enter courses ID:")
    courses_name = input("Enter courses name:")
     courses[course_id] = {"name": course_name}
    
no_courses = input_number_courses()
for i in range(no_courses):
    courses += [input_courses_infor()]

def input_marks():
    courses_id = input("Enter the courese ID:")
    if courses_id not in courses:
        print("Wrong courses ID")
        return
    for id in students:
        mark = int(input("Enter the mark for {students[id]['name]}:"))
        if id not in marks:
            marks[id] = {}
        marks[id][courses_id] = mark

def list_courses():
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]['name']}")

def list_students():
    for id in students:
        print(f"{id}: {students[id]['name']}")

def show_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Wrong course ID")
        return
    for id in students:
        if id in marks and course_id in marks[id]:
            print(f"{students[id]['name']}: {marks[id][course_id]}")
        else:
            print(f"{students[id]['name']}: N/A")

#Main program
while True:
    print("Select an option")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given choice")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_marks()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        list_students()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        break
    else:
        print("Wrong choice, please try again!")