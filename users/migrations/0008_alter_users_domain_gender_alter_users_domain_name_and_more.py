# Generated by Django 4.2.5 on 2023-09-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_domain_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_domain',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users_domain',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users_domain',
            name='phone',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='users_domain',
            name='profile_pic',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='users_domain',
            name='roll_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users_domain',
            name='school_code',
            field=models.CharField(max_length=50),
        ),
    ]
