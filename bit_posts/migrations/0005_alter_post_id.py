# Generated by Django 4.2.5 on 2023-09-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bit_posts', '0004_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
