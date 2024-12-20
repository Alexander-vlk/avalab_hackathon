# Generated by Django 5.1.3 on 2024-11-23 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_userdata_business_type_alter_userdata_industry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFromSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_url', models.URLField(max_length=500, verbose_name='URL сайта')),
                ('text', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Текст с сайта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.userdata', verbose_name='Данные с сайта')),
            ],
            options={
                'verbose_name': 'Данные с сайта',
            },
        ),
    ]
