# Generated by Django 4.2.13 on 2024-06-18 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
