# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-16 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '0001_initial'),
        ('MarketApp', '0002_axfgoods'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxfOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_time', models.DateTimeField(auto_now_add=True)),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.AxfUser')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='AxfOrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_goods_num', models.IntegerField()),
                ('og_total_price', models.FloatField()),
                ('og_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarketApp.AxfGoods')),
                ('og_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrderApp.AxfOrder')),
            ],
            options={
                'db_table': 'ordergoods',
            },
        ),
    ]
