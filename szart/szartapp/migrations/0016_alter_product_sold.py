# Generated by Django 4.2.2 on 2023-07-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szartapp', '0015_order_total_price_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sold',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Kup'), (1, 'Zapytaj o podobne')], default=0),
        ),
    ]
