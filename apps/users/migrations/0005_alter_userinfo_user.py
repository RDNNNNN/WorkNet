# Generated by Django 5.1 on 2024-09-03 09:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_userinfo_location_alter_userinfo_nickname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
