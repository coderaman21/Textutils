# Generated by Django 3.2.3 on 2021-07-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0003_alter_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
