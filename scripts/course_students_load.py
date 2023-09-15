from users.models import course_students
from datetime import datetime

import csv

def run():
    with open('scripts/h_course_students.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
        #     # print(row[13])
            last_viewed = row[6]
            try:
                last_viewed = datetime.strptime(last_viewed, "%m-%d-%Y %H:%M")
                last_viewed = last_viewed.strftime("%Y-%m-%d")
            except ValueError as e:
                last_viewed = None

            # print(dob)
            user = course_students(
                id = row[0],
                c_id = row[1],
                user_id = row[2],
                branch_id = row[3],
                department_id = row[4],
                course_completion = row[5],
                last_viewed = last_viewed,
                penalty_points =row[7],
                superbadge=row[8],
                badge=row[9]
                )

            user.save()