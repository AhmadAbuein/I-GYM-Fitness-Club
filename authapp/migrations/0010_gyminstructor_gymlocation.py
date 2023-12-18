# Generated by Django 3.2.12 on 2023-09-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_attendance_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GymInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('gym_locations', models.ManyToManyField(related_name='instructors', to='authapp.GymLocation')),
            ],
        ),
    ]
