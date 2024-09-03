# Generated by Django 5.1 on 2024-09-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='average_score',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=5),
        ),
    ]
