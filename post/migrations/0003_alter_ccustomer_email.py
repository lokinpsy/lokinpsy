# Generated by Django 4.0 on 2024-07-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_ccustomer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccustomer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
