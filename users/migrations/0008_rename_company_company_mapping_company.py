# Generated by Django 4.2.5 on 2023-09-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_company_mapping_subtopic_company_subtopic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_mapping',
            old_name='Company',
            new_name='company',
        ),
    ]
