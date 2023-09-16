from users.models import company_subtopic,company
from datetime import datetime

import csv

def run():
    with open('scripts/company_subtopic.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            c = company.objects.get(company=row[0])
            user = company_subtopic(
                company=c,
                subTopic=row[1]
                )

            user.save()