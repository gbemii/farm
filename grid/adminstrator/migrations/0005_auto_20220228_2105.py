# Generated by Django 3.2a1 on 2022-02-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0004_rename_farms_farm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Kyc_user_info',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]