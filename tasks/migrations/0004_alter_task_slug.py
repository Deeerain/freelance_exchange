# Generated by Django 4.2.1 on 2023-05-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_categories_task_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
