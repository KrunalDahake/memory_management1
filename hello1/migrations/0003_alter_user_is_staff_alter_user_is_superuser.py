# Generated by Django 4.0 on 2022-04-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello1', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
