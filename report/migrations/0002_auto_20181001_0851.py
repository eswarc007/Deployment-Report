# Generated by Django 2.1.1 on 2018-10-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Empid',
            field=models.IntegerField(blank=True),
        ),
    ]