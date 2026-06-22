from student import students


def calculate_total(student):

    return sum(student["marks"])


def find_topper():

    if not students:

        return None

    topper = students[0]

    for student in students:

        if calculate_total(student) > calculate_total(topper):

            topper = student

    return topper


def summarize_results():

    if not students:

        return {}

    total_students = len(students)

    total_marks = 0

    highest = 0

    lowest = calculate_total(students[0])

    for student in students:

        marks = calculate_total(student)

        total_marks += marks

        highest = max(highest, marks)

        lowest = min(lowest, marks)

    return {

        "Total Students": total_students,

        "Highest": highest,

        "Lowest": lowest,

        "Average": round(
            total_marks / total_students,
            2
        )
    }
