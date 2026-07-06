from app.services.config import CLASS_CONFIG
from app.services.analytics_student_service import AnalyticsStudentService
import typer

from faker_data import generate_student

from app.services.add_student_service import AddStudentService

from app.services.student_service import StudentService
student_service = StudentService()
add_student_service = AddStudentService()
analytics_service = AnalyticsStudentService()

app = typer.Typer()

add_student_service = AddStudentService()


@app.command()
def add():

    name = typer.prompt("Student Name")

    student_class = typer.prompt("Class (5-10)")

    term = typer.prompt("Term")

    if student_class not in CLASS_CONFIG:

        print("Invalid class")

        return

    subjects = CLASS_CONFIG[student_class]["subjects"]

    print("\nEnter marks for:")

    print(", ".join(subjects))

    marks = list(
        map(
            int,
            typer.prompt(
                "Marks separated by space"
            ).split()
        )
    )

    add_student_service.add_student(
        name,
        student_class,
        term,
        marks
    )

    print("Student added successfully.")


@app.command()
def view():

    for student in student_service.get_students():

        print(student)


@app.command()
def edit():

    name = typer.prompt("Student Name")

    marks = list(
        map(
            int,
            typer.prompt(
                "New marks"
            ).split()
        )
    )

    if student_service.edit_student(
        name,
        marks
    ):

        print("Updated")

    else:

        print("Student not found")


@app.command()
def delete():

    name = typer.prompt("Student Name")

    if student_service.delete_student(
        name
    ):

        print("Deleted")

    else:

        print("Student not found")


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

        add_student_service.add_student(
            student["name"],
            student["year"],
            student["term"],
            student["marks"]
        )

    print(f"{count} students generated successfully.")


if __name__ == "__main__":

    app()
