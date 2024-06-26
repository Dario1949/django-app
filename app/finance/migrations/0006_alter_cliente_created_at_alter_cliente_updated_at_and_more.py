# Generated by Django 4.2.10 on 2024-04-29 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_alter_cliente_created_at_alter_cliente_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='cliente_producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='cliente_producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 10, 3, 46, 461737)),
        ),
    ]
