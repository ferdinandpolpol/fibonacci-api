# Generated by Django 3.2.15 on 2022-09-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibonacciHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(help_text='Index of fibonacci')),
                ('fibonacci_number', models.BigIntegerField(help_text='Actual fibonacci')),
            ],
        ),
    ]