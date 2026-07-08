import csv
import os


class BaseStudentService:

    def __init__(
        self,
        file_name,
        subjects
    ):

        self.file_name = file_name

        self.subjects = subjects

    def load_students(self):

        students = []

        try:

            with open(self.file_name, "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    students.append(
                        {
                            "name": row["name"],
                            "year": row["year"],
                            "term": row["term"],
                            "marks": {
                                subject: int(row[subject])
                                for subject in self.subjects
                            }
                        }
                    )

        except FileNotFoundError:

            return []

        return students

    def save_students(self, students):

        os.makedirs(
            os.path.dirname(self.file_name),
            exist_ok=True
        )

        with open(
            self.file_name,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "name",
                    "year",
                    "term",
                    *self.subjects
                ]
            )

            for student in students:

                writer.writerow(
                    [
                        student["name"],
                        student["year"],
                        student["term"],
                        *[
                            student["marks"][subject]
                            for subject in self.subjects
                        ]
                    ]
                )
