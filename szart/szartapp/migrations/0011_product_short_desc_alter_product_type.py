# Generated by Django 4.2.2 on 2023-07-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szartapp', '0010_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_desc',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ceramika'), (0, 'Malarstwo')], default=0),
        ),
    ]
