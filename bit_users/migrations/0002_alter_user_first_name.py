# Generated by Django 4.2.4 on 2023-09-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bit_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
