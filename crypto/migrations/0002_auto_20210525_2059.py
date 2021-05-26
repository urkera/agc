# Generated by Django 3.2.3 on 2021-05-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Price', 'verbose_name_plural': 'Prices'},
        ),
        migrations.AddField(
            model_name='price',
            name='average',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='volume',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
