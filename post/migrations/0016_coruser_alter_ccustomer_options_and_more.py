# Generated by Django 4.0 on 2024-07-10 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('post_no_or_title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('cor_date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('is_connect', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-cor_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='ccustomer',
            options={'ordering': ['-c_date']},
        ),
        migrations.AlterModelOptions(
            name='subscriber',
            options={'ordering': ['-date_join']},
        ),
    ]
