# Generated by Django 4.2.5 on 2023-09-18 22:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bit_posts', '0009_rename_comment_subcomment_parent_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvoted_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]