# Generated by Django 4.2.5 on 2023-09-17 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0008_company_recommendation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_recommendation',
            old_name='email_id',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='company_recommendation',
            name='company_id',
        ),
    ]
