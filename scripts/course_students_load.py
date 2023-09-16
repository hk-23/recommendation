from users.models import course_students,courses
from datetime import datetime
from usersapp.models import User

import csv

def run():
    with open('scripts/h_course_students.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
        #     # print(row[13])
            last_viewed = row[7]
            try:
                last_viewed = datetime.strptime(last_viewed, "%m-%d-%Y %H:%M")
                last_viewed = last_viewed.strftime("%Y-%m-%d")
            except ValueError as e:
                last_viewed = None

            c = courses.objects.get(c_id=row[1])    
            e = User.objects.get(email=row[3])
            # print(dob)
            user = course_students(
                id = row[0],
                c_id = c,
                user_id = row[2],
                email=e,
                branch_id = row[4],
                department_id = row[5],
                course_completion = row[6],
                last_viewed = last_viewed,
                penalty_points =row[8],
                superbadge=row[9],
                badge=row[10]
                )

            user.save()