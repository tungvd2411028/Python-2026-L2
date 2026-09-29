students = []
courses = []
marks = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print ("\nStudent", i + 1)
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter date of birth: ")

    student = {
        "id": student_id,
        "name": name,
        "dob": dob
    }

    students.append(student)

m = int(input("\nEnter number of courses: "))

for i in range(m):
    print("\nCourse", i + 1)

    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")

    course = {
        "id": course_id,
        "name": course_name
    }

    courses.append(course)

for course in courses:
    course_id = course["id"]

    print("\nEnter marks for course:", course["name"])

    marks[course_id] = {}

    for student in students:
        student_id = student["id"]

        mark = float(
            input("Enter mark for " + student["name"] + ": ")
        )

        marks[course_id][student_id] = mark

print("\n========== LIST COURSES ==========")

for course in courses:
    print(
        "ID:", course["id"],
        "| Name:", course["name"]
    )

    print("\n========== LIST STUDENTS ==========")

for student in students:
    print(
        "ID:", student["id"],
        "| Name:", student["name"],
        "| DoB:", student["dob"]
    )

print("\n========== SHOW STUDENT MARKS ==========")

course_id = input("Enter course ID: ")

if course_id in marks:

    # Find course name
    course_name = ""

    for course in courses:
        if course["id"] == course_id:
            course_name = course["name"]

    print("\nCourse:", course_name)

    for student in students:
        student_id = student["id"]

        print(
            "Student:", student["name"],
            "| Mark:", marks[course_id][student_id]
        )

else:
    print("Course not found.")

