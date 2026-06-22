import typer

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

    marks = list(
        map(
            int,
            typer.prompt(
                "Marks separated by space"
            ).split()
        )
    )

    add_student(name, marks)

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


if __name__ == "__main__":

    app()