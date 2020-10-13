# Generated by Django 3.0.4 on 2020-09-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('photo', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=500, verbose_name='краткое описание товара')),
                ('description', models.TextField(verbose_name='подробное описание товара')),
                ('specifications', models.TextField(verbose_name='характеристики товара')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена товара')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
