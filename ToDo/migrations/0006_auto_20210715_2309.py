# Generated by Django 3.2.3 on 2021-07-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0005_auto_20210715_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
