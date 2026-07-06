from faker import Faker
import random

from app.services.config import CLASS_CONFIG

fake = Faker()


def generate_student():

    student_class = random.choice(
        list(CLASS_CONFIG.keys())
    )

    subjects = CLASS_CONFIG[
        student_class
    ]["subjects"]

    return {
        "name": fake.name(),
        "year": student_class,
        "term": random.choice(
            ["1", "2"]
        ),
        "subjects": subjects,
        "marks": [
            random.randint(60, 100)
            for _ in subjects
        ]
    }
