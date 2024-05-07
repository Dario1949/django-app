# Generated by Django 4.2.10 on 2024-03-19 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0006_person_created_at_person_deleted_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('id_dept', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 798820))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 798820))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countrie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 797820))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 797820))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('id_country', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 798820))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 798820))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Identification_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 798820))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 798820))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('id_person', models.IntegerField()),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 797820))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 797820))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 797820)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 797820)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 767813)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 22, 33, 26, 767813)),
        ),
    ]
