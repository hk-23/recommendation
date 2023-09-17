# Generated by Django 4.2.5 on 2023-09-17 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_course_students_email_alter_course_students_c_id'),
        ('studentapp', '0009_rename_email_id_company_recommendation_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_recommendation',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
    ]
