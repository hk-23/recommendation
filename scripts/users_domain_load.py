import uuid
from users.models import users_domain
from datetime import datetime

import csv

def run():
    with open('scripts/h_users_domain.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            # print(row[13])
            dob = row[13]
            try:
                dob = datetime.strptime(dob, "%d-%m-%Y %H:%M")
                dob = dob.strftime("%Y-%m-%d")
            except ValueError as e:
                dob = None

            # print(dob)
            user = users_domain(
                users_domain_id=row[0],
                user_id = row[1],
                school_id = uuid.uuid4() if row[2] == "" else row[2],
                school_name = row[3],
                school_code = row[4],
                email = row[5],
                name = row[6],
                phone = None if row[7] == "" else row[7],
                gender = row[8],
                profile_pic = row[9],
                roll_no = row[10],
                badge = row[11],
                superbadge = row[12],
                dob = dob,
                branch_id = uuid.uuid4() if row[14] == "" else row[14],
                branch_name = row[15],
                batch_id = uuid.uuid4() if row[16] == "" else row[16],
                batch = row[17],
                department_id = uuid.uuid4() if row[18] == "" else row[18],
                department_name = row[19],
                degree_id = uuid.uuid4() if row[20] == "" else row[20],
                degree = row[21]
            )

            user.save()