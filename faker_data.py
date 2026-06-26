from faker import Faker
import random

fake = Faker()

SUBJECT_POOL = [
    "Python",
    "Database",
    "Networks",
    "Cloud",
    "DevOps",
    "Security",
    "AI",
    "Machine Learning"
]


def generate_student():

    subjects = random.sample(SUBJECT_POOL, 3)

    marks = [
        random.randint(70, 100)
        for _ in subjects
    ]

    return {
        "name": fake.name(),
        "year": random.choice(
            ["2024", "2025", "2026"]
        ),
        "term": random.choice(
            ["Term 1", "Term 2", "Term 3"]
        ),
        "subjects": subjects,
        "marks": marks
    }