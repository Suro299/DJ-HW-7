# Generated by Django 4.1.6 on 2023-04-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_adminposts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminposts',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]