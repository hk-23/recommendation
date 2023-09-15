from users.models import course_tests
from datetime import datetime

import csv

def run():
    with open('scripts/h_course_tests.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
        # #     # print(row[13])
        #     last_viewed = row[6]
        #     try:
        #         last_viewed = datetime.strptime(last_viewed, "%m-%d-%Y %H:%M")
        #         last_viewed = last_viewed.strftime("%Y-%m-%d")
        #     except ValueError as e:
        #         last_viewed = None

            # print(dob)
            user = course_tests(
                id = row[0],
                school_id = row[1],
                c_name = row[2],
                c_type = row[3],
                t_name = row[4],
                t_type = row[5],
                c_id=row[6],
                t_id=row[7],
                Module_name=row[8]
                )

            user.save()