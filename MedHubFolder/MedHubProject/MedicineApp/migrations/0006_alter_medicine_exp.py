# Generated by Django 5.1.4 on 2025-01-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicineApp', '0005_alter_medicine_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='exp',
            field=models.CharField(max_length=100),
        ),
    ]
