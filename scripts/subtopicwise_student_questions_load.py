from studentapp.models import subtopic_wise
from datetime import datetime
import csv

def run():
    with open('scripts/subtopicwise_student_questions.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:



            # print(dob)
            user = subtopic_wise(
                user_id = row[0],
                email =None,
                subtopic_name = row[2],
                student_marks = 0 if row[3]=='' else row[3],
                total_marks = 0 if row[4]=='' else row[4],
                MarksPercentage = None if row[5]=='' else row[5],
                Hard_correct_questions = row[6],
                Easy_correct_questions =row[7],
                medium_correct_questions=row[8],
                Questions_Correct=row[9],
                Questions_wrong=row[10],
                Questions_skipped=row[11],
                Questions_partial_correct=row[12],
                Questions_not_viewed=row[13],
                testcase_passed=row[14],
                no_of_testcases=row[15],
                testcase_percentage=row[16]

                )

            user.save()