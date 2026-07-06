import csv
import os


class BaseStudentService:

    HEADERS = [
        "name",
        "year",
        "term",
        "subjects",
        "marks"
    ]

    def __init__(self, file_name):

        self.file_name = file_name

    def load_students(self):

        students = []

        try:

            with open(
                self.file_name,
                "r"
            ) as file:

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

    def save_students(self, students):

        file_exists = os.path.exists(self.file_name)

        with open(
            self.file_name,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow(self.HEADERS)

            else:

                writer.writerow(self.HEADERS)

            for student in students:

                writer.writerow(
                    [
                        student["name"],
                        student["year"],
                        student["term"],
                        ",".join(student["subjects"]),
                        ",".join(
                            map(
                                str,
                                student["marks"]
                            )
                        )
                    ]
                )
