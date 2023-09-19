# Generated by Django 4.2.5 on 2023-09-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bit_posts', '0008_comment_is_reply_alter_subcomment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcomment',
            old_name='comment',
            new_name='parent_comment',
        ),
        migrations.AddField(
            model_name='subcomment',
            name='is_reply',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]
