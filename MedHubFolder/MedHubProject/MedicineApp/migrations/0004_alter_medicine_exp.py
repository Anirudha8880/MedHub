# Generated by Django 5.1.4 on 2025-01-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicineApp', '0003_alter_medicine_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='exp',
            field=models.DateTimeField(),
        ),
    ]
