# Generated by Django 4.0.1 on 2022-02-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100, unique=True)),
                ('population', models.PositiveIntegerField()),
                ('first_dose_rate', models.PositiveIntegerField()),
                ('second_dose_rate', models.PositiveIntegerField()),
            ],
        ),
    ]
