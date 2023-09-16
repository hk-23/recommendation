from users.models import course_modules, courses
from datetime import datetime

import csv

def run():
    with open('scripts/h_course_modules.csv') as file:
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
            c = courses.objects.get(c_id=row[0])
        
            user = course_modules(
                c_id = c,
                c_name = row[1],
                Module_name=row[2]
                )

            user.save()