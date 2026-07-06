from app.services.base_student_service import BaseStudentService
from app.services.config import CLASS_CONFIG


class StudentService:

    def get_students(self):

        students = []

        for config in CLASS_CONFIG.values():

            service = BaseStudentService(
                config["file"]
            )

            students.extend(
                service.load_students()
            )

        return students

    def edit_student(
        self,
        name,
        marks
    ):

        for config in CLASS_CONFIG.values():

            service = BaseStudentService(
                config["file"]
            )

            students = service.load_students()

            updated = False

            for student in students:

                if student["name"].lower() == name.lower():

                    student["marks"] = marks

                    service.save_students(students)

                    return True

        return False

    def delete_student(
        self,
        name
    ):

        for config in CLASS_CONFIG.values():

            service = BaseStudentService(
                config["file"]
            )

            students = service.load_students()

            remaining = []

            deleted = False

            for student in students:

                if student["name"].lower() == name.lower():

                    deleted = True

                else:

                    remaining.append(student)

            if deleted:

                service.save_students(remaining)

                return True

        return False
