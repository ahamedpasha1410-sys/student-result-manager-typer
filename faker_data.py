from faker import Faker
import random

fake = Faker()


def generate_student():
    subjects = [
        "Python",
        "Database",
        "Networking"
    ]

    return {
        "name": fake.name(),
        "year": random.choice(["2025", "2026"]),
        "term": random.choice(["1", "2"]),
        "subjects": subjects,
        "marks": [
            random.randint(60, 100)
            for _ in subjects
        ]
    }
