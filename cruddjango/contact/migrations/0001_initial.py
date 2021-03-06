# Generated by Django 3.2.8 on 2021-10-27 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('elastname', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('ephonenumber', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
