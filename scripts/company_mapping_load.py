from users.models import company_mapping,company
from datetime import datetime

import csv

def run():
    with open('scripts/company_mapping.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            c = company.objects.get(company=row[2])
            user = company_mapping(
                c_id = row[0],
                c_name = row[1],
                company=c
                )

            user.save()