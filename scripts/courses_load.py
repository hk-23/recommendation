from users.models import courses
from datetime import datetime

import csv

def run():
    with open('scripts/h_courses.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:

            user = courses(
                c_id = row[0],
                c_name = row[1]
                )

            user.save()