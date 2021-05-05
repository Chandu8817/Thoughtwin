# Generated by Django 3.1.7 on 2021-04-12 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
        ('products', '0012_auto_20210412_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.seller'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order_id',
            field=models.CharField(default='2BA6CF', editable=False, max_length=15, unique=True),
        ),
    ]