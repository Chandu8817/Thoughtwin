# Generated by Django 3.1.7 on 2021-03-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210311_0953'),
        ('postapp', '0008_auto_20210311_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile'),
        ),
    ]