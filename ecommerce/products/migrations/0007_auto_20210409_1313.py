# Generated by Django 3.1.7 on 2021-04-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210409_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='order_id',
            field=models.CharField(default='36547C', editable=False, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
