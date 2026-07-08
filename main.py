from app.services.config import CLASS_CONFIG
from app.services.analytics_student_service import AnalyticsStudentService
import typer

from faker_data import generate_student

from app.services.add_student_service import AddStudentService

from app.services.student_service import StudentService
student_service = StudentService()
analytics_service = AnalyticsStudentService()

app = typer.Typer()


@app.command()
def add():

    name = typer.prompt("Student Name")

    student_class = typer.prompt("Class")

    term = typer.prompt("Term")

    subjects = CLASS_CONFIG[student_class]["subjects"]

    marks = []

    for subject in subjects:

        mark = int(
            typer.prompt(
                f"Enter marks for {subject}"
            )
        )

        marks.append(mark)

    add_student_service = AddStudentService(
        student_class
    )

    add_student_service.add_student(
        name,
        term,
        marks
    )

    print("Student added successfully")


@app.command()
def subject(subject: str):

    result = analytics_service.get_subject_marks(
        subject
    )

    if not result:

        print("No records found.")

        return

    for student in result:

        print(
            f'{student["name"]}: {student["marks"]}'
        )


@app.command()
def view():

    students = student_service.get_students()

    if not students:

        print("No students found.")

        return

    for student in students:

        print("-" * 40)

        print(f'Name  : {student["name"]}')
        print(f'Class : {student["year"]}')
        print(f'Term  : {student["term"]}')

        print()

        for subject, mark in student["marks"].items():

            print(f"{subject:<12}: {mark}")

        print("-" * 40)


@app.command()
def edit():

    name = typer.prompt("Student Name")

    student_class = typer.prompt("Class")

    if student_class not in CLASS_CONFIG:

        print("Invalid class")

        return

    marks = []

    for subject in CLASS_CONFIG[student_class]["subjects"]:

        mark = typer.prompt(
            f"Enter marks for {subject}",
            type=int
        )

        marks.append(mark)

    if student_service.edit_student(
        name,
        student_class,
        marks
    ):

        print("Student updated successfully.")

    else:

        print("Student not found.")


@app.command()
def delete():

    name = typer.prompt("Student Name")

    student_class = typer.prompt("Class")

    if student_service.delete_student(
        name,
        student_class
    ):

        print("Student deleted successfully.")

    else:

        print("Student not found.")


@app.command()
def topper():

    print(
        analytics_service.find_topper()
    )


@app.command()
def summary():

    print(
        analytics_service.summarize_results()
    )


@app.command()
def generate(count: int = 10):

    for _ in range(count):

        student = generate_student()
        service = AddStudentService(
            student["year"]
        )

        service.add_student(
            student["name"],
            student["term"],
            student["marks"]
        )

    print(f"{count} students generated successfully.")


if __name__ == "__main__":

    app()
