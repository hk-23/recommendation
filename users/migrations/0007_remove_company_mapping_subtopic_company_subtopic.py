# Generated by Django 4.2.5 on 2023-09-16 21:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_company_company_mapping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_mapping',
            name='subTopic',
        ),
        migrations.CreateModel(
            name='company_subtopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.UUIDField(default=uuid.uuid4)),
                ('c_name', models.CharField(max_length=50, null=True)),
                ('subTopic', models.CharField(max_length=50, null=True)),
                ('Company', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.company')),
            ],
        ),
    ]
