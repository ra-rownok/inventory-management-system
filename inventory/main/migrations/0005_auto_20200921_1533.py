# Generated by Django 3.1.1 on 2020-09-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200921_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyorder',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=10),
        ),
    ]
