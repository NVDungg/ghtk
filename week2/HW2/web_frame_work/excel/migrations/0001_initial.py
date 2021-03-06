# Generated by Django 4.0.3 on 2022-06-11 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('stu_class', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=20)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('ethnic', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(blank=True)),
                ('total_grade_1', models.PositiveSmallIntegerField(blank=True)),
                ('total_grade_2', models.PositiveSmallIntegerField(blank=True)),
                ('total_grade_3', models.PositiveSmallIntegerField(blank=True)),
                ('total_grade_4', models.PositiveSmallIntegerField(blank=True)),
                ('total_grade_5', models.PositiveSmallIntegerField(blank=True)),
                ('total_5_years', models.PositiveSmallIntegerField(blank=True)),
                ('plus', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('total_all', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('decripsion', models.CharField(max_length=255)),
            ],
        ),
    ]
