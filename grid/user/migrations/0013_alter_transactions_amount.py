# Generated by Django 3.2a1 on 2022-03-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20220301_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.IntegerField(),
        ),
    ]