# Generated by Django 4.2.5 on 2023-09-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_module_wise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language_wise',
            name='MarksPercentage',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='module_wise',
            name='MarksPercentage',
            field=models.FloatField(null=True),
        ),
    ]
