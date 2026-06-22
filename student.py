import json
FILE_NAME = "students.json"

def load_students():

    try:

        with open(FILE_NAME, "r") as file:

            return json.load(file)

    except:

        return []

def save_students(students):

    with open(FILE_NAME, "w") as file:

        json.dump(
            students,
            file,
            indent=4
        )  
    
def add_student(name, marks):

    students = load_students()

    students.append(
        {
            "name": name,
            "marks": marks
        }
    )

    save_students(students)


def get_students():

    return load_students()


def edit_student(name, marks):

    students = load_students()

    for student in students:

        if student["name"].lower() == name.lower():

            student["marks"] = marks

            save_students(students)

            return True

    return False


def delete_student(name):

    students = load_students()

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_students(students)

            return True

    return False