# Generated by Django 4.1.2 on 2022-10-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_helper', '0003_alter_task_deadline_alter_task_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
