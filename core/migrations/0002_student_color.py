# Generated by Django 4.2.7 on 2024-03-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
