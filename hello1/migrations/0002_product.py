# Generated by Django 4.0 on 2022-04-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('auth_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=250)),
                ('description', models.CharField(blank=True, default='', max_length=800, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
    ]
