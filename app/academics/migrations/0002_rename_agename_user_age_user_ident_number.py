# Generated by Django 4.2.10 on 2024-03-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='agename',
            new_name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='ident_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
