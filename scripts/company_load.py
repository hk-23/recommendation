from users.models import company
from datetime import datetime

import csv

def run():
    with open('scripts/company.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:

            user = company(
                company= row[0]
                )

            user.save()