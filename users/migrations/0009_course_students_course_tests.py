# Generated by Django 4.2.5 on 2023-09-15 15:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_users_domain_gender_alter_users_domain_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_students',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('c_id', models.UUIDField(default=uuid.uuid4)),
                ('user_id', models.UUIDField(default=uuid.uuid4)),
                ('badge', models.BigIntegerField(default=0)),
                ('superbadge', models.BigIntegerField(default=0)),
                ('penalty_points', models.BigIntegerField(default=0)),
                ('course_completion', models.BigIntegerField(default=0)),
                ('last_viewed', models.DateTimeField(null=True)),
                ('branch_id', models.UUIDField(default=uuid.uuid4)),
                ('department_id', models.UUIDField(default=uuid.uuid4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='course_tests',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('c_id', models.UUIDField(default=uuid.uuid4)),
                ('school_id', models.UUIDField(default=uuid.uuid4)),
                ('c_type', models.CharField(max_length=50, null=True)),
                ('branch_id', models.UUIDField(default=uuid.uuid4)),
                ('t_type', models.CharField(blank=True, max_length=50)),
                ('t_name', models.CharField(max_length=50, null=True)),
                ('t_id', models.UUIDField(default=uuid.uuid4, null=True)),
                ('Module_name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
