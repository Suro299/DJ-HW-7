# Generated by Django 4.1.6 on 2023-04-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_shopprod'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprod',
            name='button_text_en_ca',
            field=models.CharField(max_length=50, null=True, verbose_name='Item Button Text'),
        ),
        migrations.AddField(
            model_name='shopprod',
            name='button_text_en_gb',
            field=models.CharField(max_length=50, null=True, verbose_name='Item Button Text'),
        ),
        migrations.AddField(
            model_name='shopprod',
            name='button_text_en_us',
            field=models.CharField(max_length=50, null=True, verbose_name='Item Button Text'),
        ),
        migrations.AddField(
            model_name='shopprod',
            name='description_en_ca',
            field=models.CharField(max_length=100, null=True, verbose_name='Item Description'),
        ),
        migrations.AddField(
            model_name='shopprod',
            name='description_en_gb',
            field=models.CharField(max_length=100, null=True, verbose_name='Item Description'),
        ),
        migrations.AddField(
            model_name='shopprod',
            name='description_en_us',
            field=models.CharField(max_length=100, null=True, verbose_name='Item Description'),
        ),
    ]
