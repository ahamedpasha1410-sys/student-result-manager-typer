students = []


def add_student(name, marks):

    students.append(
        {
            "name": name,
            "marks": marks
        }
    )


def get_students():

    return students


def edit_student(name, marks):

    for student in students:

        if student["name"].lower() == name.lower():

            student["marks"] = marks

            return True

    return False


def delete_student(name):

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            return True

    return False
