# Generated by Django 3.1.7 on 2021-03-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210311_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_cover',
            field=models.ImageField(default='images/coverimage', upload_to='images/coverimage'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='images/profile', upload_to='images/profile'),
        ),
    ]
