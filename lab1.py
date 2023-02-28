students = {} # Defined a dictionary to store student info
courses = {} # Defined a dictionary to store courses info
marks = {} # Defined a dictionary to store marks



# Function for the input of student info:
def input_students():
    n_students = int(input("Enter the number of students in the class:"))
    for i in range(n_students):
        students_id = input("Enter students id: ")
        students_name = input("Enter students name: ")
        students_DoB = input("Enter students date of birth: ")
        students[students_id]= {'name': students_name, 'DoB': students_DoB}

# Function for the input of courses info:
def input_courses():
    n_courses = int(input("Enter the number of the courses: "))
    for i in range(n_courses):
        courses_id = input("Enter courses id: ")
        courses_name = input("Enter courses name: ")
        courses[courses_id]= {'name': courses_name}

# Function to select a course and put in the marks for students:
def input_marks():
    courses_id = input("Enter the course id: ")
    if courses_id not in courses:
        print("No courses found!")
        return
    for students_id in students:
        mark = int(input(f"Enter the mark for {students[students_id]['name']}: "))
        if students_id not in marks:
            marks[students_id] = {}
        marks[students_id][courses_id] = mark

# Defined function to list courses and students:
def list_courses():
    for courses_id in courses:
        print(f"(courses_id: {courses[courses_id]['name']})")

def list_students():
    for students_id in students:
        print(f"(students_id: {students[students_id]['name']})")

# Function to show marks of given courses:
def show_marks():
    courses_id = input("Enter the courses id: ")
    if courses_id not in courses:
        print("No courses found!")
        return
    for students_id in students:
        if students_id in marks and courses_id in marks[students_id]:
            print(f"(students_id: {students[students_id]['name']}: {marks[students_id][courses_id]}")
        else:
            print(f"{students[students_id]['name']}: Not found")

# Main program to run:
input_students()
input_courses()

while True:
    print("Select: ")
    print("1. Input marks of a course")
    print("2. List courses")
    print("3. List Students")
    print("4. Show the student marks of the given courses")
    print("5. End")
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
        print("Invalid choice, sorry!")