# Generated by Django 3.2.15 on 2022-09-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fib', '0002_alter_fibonaccihistory_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonaccihistory',
            name='fibonacci_number',
            field=models.TextField(help_text='Actual fibonacci'),
        ),
    ]