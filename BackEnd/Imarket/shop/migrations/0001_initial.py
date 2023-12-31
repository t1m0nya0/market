# Generated by Django 3.2.16 on 2023-09-02 14:47

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Shop')),
                ('rating', models.FloatField(default=5, validators=[shop.models.validate_rating], verbose_name='Rating')),
                ('rate_cnt', models.IntegerField(default=1, null=True)),
                ('address', models.CharField(max_length=255, unique=True, verbose_name='Shop address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
                'ordering': ('-rating', 'name'),
            },
        ),
        migrations.CreateModel(
            name='WarehouseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'verbose_name': 'warehouse item',
                'verbose_name_plural': 'warehouse items',
            },
        ),
    ]
