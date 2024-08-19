# Generated by Django 5.0.6 on 2024-06-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_availability_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookpatient',
            name='user',
        ),
        migrations.AddField(
            model_name='availability',
            name='doctor_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bookpatient',
            name='patient_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
