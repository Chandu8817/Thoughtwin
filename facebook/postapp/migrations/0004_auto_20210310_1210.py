# Generated by Django 3.1.7 on 2021-03-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_auto_20210310_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='dateofpost',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
