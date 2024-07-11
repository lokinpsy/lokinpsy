# Generated by Django 4.0 on 2024-07-10 08:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_ccustomer_c_date_alter_post_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccustomer',
            name='c_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 10, 8, 39, 22, 589584, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 10, 8, 39, 22, 588584, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='date_join',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 10, 8, 39, 22, 590585, tzinfo=utc)),
        ),
    ]
