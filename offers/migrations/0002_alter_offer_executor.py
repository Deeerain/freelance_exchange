# Generated by Django 4.2.1 on 2023-05-17 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
