from app.services.base_student_service import BaseStudentService
from app.services.config import CLASS_CONFIG


class AnalyticsStudentService:

    def get_all_students(self):

        students = []

        for config in CLASS_CONFIG.values():

            service = BaseStudentService(
                config["file"]
            )

            students.extend(
                service.load_students()
            )

        return students

    def calculate_total(self, student):

        return sum(student["marks"])

    def find_topper(self):

        students = self.get_all_students()

        if not students:

            return None

        topper = students[0]

        for student in students:

            if self.calculate_total(student) > self.calculate_total(topper):

                topper = student

        return topper

    def summarize_results(self):

        students = self.get_all_students()

        if not students:

            return {}

        totals = [
            self.calculate_total(student)
            for student in students
        ]

        return {
            "Total Students": len(students),
            "Highest": max(totals),
            "Lowest": min(totals),
            "Average": round(
                sum(totals) / len(students),
                2
            )
        }
