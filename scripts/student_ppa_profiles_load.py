from users.models import student_ppa_profiles
from datetime import datetime

import csv

def run():
    with open('scripts/student_ppa_profiles.csv') as file:
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
            user = student_ppa_profiles(
                s_profile_id = row[0],
                user_id = row[1],
                tenth_marks = None if row[2]=="" else row[2],
                is_tenth_percentage = None if row[3]=="" else row[3],
                twelfth_marks = None if row[4]=="" else row[4],
                is_twelfth_percentage =None if row[5]=="" else row[5],
                diploma_marks =None if row[6]=="" else row[6],
                is_diploma_percentage = None if row[7]=="" else row[7],
                ug_marks = None if row[8]=="" else row[8],
                is_ug_percentage =None if row[9]=="" else row[9],
                pg_marks = None if row[10]=="" else row[10],
                is_pg_percentage = None if row[11]=="" else row[11],
                roll_no = row[12],
                backlogs= None if row[13]=="" else row[13],
                current_backlogs =None if row[14]=="" else row[14],
                degree = row[15],
                work_experience=None if row[16]=="" else row[16],
                school_id = row[17]
                )

            user.save()