# Generated by Django 3.2.15 on 2022-09-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonaccihistory',
            name='index',
            field=models.IntegerField(help_text='Index of fibonacci', unique=True),
        ),
    ]