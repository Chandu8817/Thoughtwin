# Generated by Django 3.1.7 on 2021-03-16 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0017_comment_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]