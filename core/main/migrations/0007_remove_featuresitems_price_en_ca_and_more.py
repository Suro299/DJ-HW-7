# Generated by Django 4.1.6 on 2023-04-03 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_featuresitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuresitems',
            name='price_en_ca',
        ),
        migrations.RemoveField(
            model_name='featuresitems',
            name='price_en_gb',
        ),
        migrations.RemoveField(
            model_name='featuresitems',
            name='price_en_us',
        ),
    ]