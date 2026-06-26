import csv
import os

FILE_NAME = "students.csv"


def add_student(name, year, term, subjects, marks):

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow(
                [
                    "name",
                    "year",
                    "term",
                    "subjects",
                    "marks"
                ]
            )

        writer.writerow(
            [
                name,
                year,
                term,
                ",".join(subjects),
                ",".join(map(str, marks))
            ]
        )


def get_students():

    students = []

    try:

        with open(FILE_NAME, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                students.append(
                    {
                        "name": row["name"],
                        "year": row["year"],
                        "term": row["term"],
                        "subjects": row["subjects"].split(","),
                        "marks": list(
                            map(
                                int,
                                row["marks"].split(",")
                            )
                        )
                    }
                )

    except FileNotFoundError:

        return []

    return students


def save_students(students):

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "name",
                "year",
                "term",
                "subjects",
                "marks"
            ]
        )

        for student in students:

            writer.writerow(
                [
                    student["name"],
                    student["year"],
                    student["term"],
                    ",".join(student["subjects"]),
                    ",".join(map(str, student["marks"]))
                ]
            )


def edit_student(name, marks):

    students = get_students()

    for student in students:

        if student["name"].lower() == name.lower():

            student["marks"] = marks

            save_students(students)

            return True

    return False


def delete_student(name):

    students = get_students()

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_students(students)

            return True

    return False