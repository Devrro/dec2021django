# Generated by Django 4.0.5 on 2022-07-06 12:10

import django.core.validators
from django.db import migrations, models

import apps.users.services


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=apps.users.services.upload_to),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{5,20}$', ['Something went wrong, your name can`t contain numbers or other non-alphabetic symbols'])]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='phone',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('(?=.*[0-9]{3}[0-9]{2}[0-9]{3}[0-9]{4,5}$)', ['Number can`t contain whitespaces', 'Number can`t contain any other character but digits'])]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{5,20}$', ['Something went wrong, your name can`t contain numbers or other non-alphabetic symbols'])]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\d\\s:])([^\\s]){8,50}$', ['password must contain 1 number(0 - 9)', 'password must contain 1 uppercase letters', 'password must contain 1 lowercase letters', 'password must contain 1 non - alpha numeric number', 'password is 8 - 16 characters with no space'])]),
        ),
    ]
