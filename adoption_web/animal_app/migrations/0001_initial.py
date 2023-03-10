# Generated by Django 4.1 on 2023-01-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.FloatField(max_length=3)),
                ('adopted', models.BooleanField(default=False)),
                ('breed', models.CharField(max_length=100)),
                ('exotic', models.BooleanField(default=False)),
                ('baby', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalShelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.FloatField()),
                ('postal_code', models.FloatField()),
                ('province', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.FloatField(max_length=3)),
                ('dni', models.FloatField(max_length=15)),
                ('house', models.CharField(max_length=50)),
            ],
        ),
    ]
