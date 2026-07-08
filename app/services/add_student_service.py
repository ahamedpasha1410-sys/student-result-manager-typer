from app.services.base_student_service import BaseStudentService
from app.services.config import CLASS_CONFIG


class AddStudentService(BaseStudentService):

    def __init__(self, student_class):

        if student_class not in CLASS_CONFIG:

            raise ValueError(
                f"Invalid class: {student_class}"
            )

        self.student_class = student_class

        config = CLASS_CONFIG[student_class]

        super().__init__(
            config["file"],
            config["subjects"]
        )
        self.student_class = student_class

    def add_student(
        self,
        name,
        term,
        marks
    ):

        if len(marks) != len(self.subjects):

            raise ValueError(
                f"Exactly {len(self.subjects)} marks are required."
            )

        students = self.load_students()

        marks_dict = dict(
            zip(
                self.subjects,
                marks
            )
        )

        students.append(
            {
                "name": name,
                "year": self.student_class,
                "term": term,
                "marks": marks_dict
            }
        )

        self.save_students(students)
