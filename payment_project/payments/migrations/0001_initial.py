# Generated by Django 5.1.6 on 2025-02-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('currency', models.CharField(choices=[('usd', 'USD'), ('eur', 'EUR')], max_length=3)),
            ],
        ),
    ]
