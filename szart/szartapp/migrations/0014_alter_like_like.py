# Generated by Django 4.2.2 on 2023-07-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szartapp', '0013_alter_like_like_alter_product_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.PositiveSmallIntegerField(choices=[(1, 'polubione'), (0, 'niepolubione')], default=0),
        ),
    ]
