# Generated by Django 5.0.1 on 2024-01-20 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название компании')),
                ('company_type', models.CharField(choices=[('factory', 'Завод'), ('retail_network', 'Розничная сеть'), ('individual_entrepreneur', 'Индивидуальный предприниматель')], max_length=23, verbose_name='тип компании')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('country', models.CharField(max_length=150, verbose_name='страна')),
                ('city', models.CharField(max_length=150, verbose_name='город')),
                ('street', models.CharField(max_length=150, verbose_name='улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='номер дома')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='company.company', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компании',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название товара')),
                ('model', models.CharField(max_length=200, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='company.company', verbose_name='компания-владелец')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
