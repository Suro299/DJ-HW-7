# Generated by Django 4.1.6 on 2023-04-03 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_productsubcategory_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsubcategory',
            name='img',
        ),
    ]
