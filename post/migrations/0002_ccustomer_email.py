# Generated by Django 4.0 on 2024-07-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccustomer',
            name='email',
            field=models.EmailField(default='notprovided@gmail.com', max_length=254),
        ),
    ]
