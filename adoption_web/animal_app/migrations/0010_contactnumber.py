# Generated by Django 4.1.4 on 2023-01-13 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_app', '0009_person_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.IntegerField()),
            ],
        ),
    ]
