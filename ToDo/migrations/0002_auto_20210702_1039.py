# Generated by Django 3.2.3 on 2021-07-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]
