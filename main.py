import typer
from faker_data import generate_student
from student import (
    add_student,
    get_students,
    edit_student,
    delete_student
)

from utils import (
    find_topper,
    summarize_results
)

app = typer.Typer()


@app.command()
def add():

    name = typer.prompt("Student Name")

    year = typer.prompt("Academic Year")

    term = typer.prompt("Term")

    subjects = typer.prompt(
        "Subjects (comma separated)"
    ).split(",")

    marks = list(
        map(
            int,
            typer.prompt(
                "Marks separated by space"
            ).split()
        )
    )

    add_student(
        name,
        year,
        term,
        subjects,
        marks
    )

    print("Student added")


@app.command()
def view():

    for student in get_students():

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

    if edit_student(name, marks):

        print("Updated")

    else:

        print("Student not found")


@app.command()
def delete():

    name = typer.prompt("Student Name")

    if delete_student(name):

        print("Deleted")

    else:

        print("Student not found")


@app.command()
def topper():

    print(find_topper())


@app.command()
def summary():

    print(summarize_results())


@app.command()
def generate(count: int = 10):

    for _ in range(count):

        student = generate_student()

        add_student(
            student["name"],
            student["year"],
            student["term"],
            student["subjects"],
            student["marks"]
        )

    print(f"{count} students generated successfully.")


if __name__ == "__main__":

    app()
