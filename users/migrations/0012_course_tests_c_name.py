# Generated by Django 4.2.5 on 2023-09-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_course_students_course_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_tests',
            name='c_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
