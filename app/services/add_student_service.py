from app.services.base_student_service import BaseStudentService
from app.services.config import CLASS_CONFIG


class AddStudentService:

    def add_student(
        self,
        name,
        student_class,
        term,
        marks
    ):

        if student_class not in CLASS_CONFIG:

            raise ValueError(
                f"Invalid class: {student_class}"
            )

        config = CLASS_CONFIG[student_class]

        subjects = config["subjects"]

        if len(marks) != len(subjects):

            raise ValueError(
                f"Exactly {len(subjects)} marks are required."
            )

        service = BaseStudentService(
            config["file"]
        )

        students = service.load_students()

        students.append(
            {
                "name": name,
                "year": student_class,
                "term": term,
                "subjects": subjects,
                "marks": marks
            }
        )

        service.save_students(students)
