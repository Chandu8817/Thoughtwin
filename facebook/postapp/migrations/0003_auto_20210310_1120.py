# Generated by Django 3.1.7 on 2021-03-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_auto_20210310_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='postcontain',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
