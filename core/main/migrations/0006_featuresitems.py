# Generated by Django 4.1.6 on 2023-04-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_activcarusel_button_text_en_ca_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturesItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveBigIntegerField(verbose_name='Item Price')),
                ('price_en_us', models.PositiveBigIntegerField(null=True, verbose_name='Item Price')),
                ('price_en_gb', models.PositiveBigIntegerField(null=True, verbose_name='Item Price')),
                ('price_en_ca', models.PositiveBigIntegerField(null=True, verbose_name='Item Price')),
                ('img', models.ImageField(upload_to='', verbose_name='Item Image')),
                ('description', models.CharField(max_length=100, verbose_name='Item Description')),
                ('description_en_us', models.CharField(max_length=100, null=True, verbose_name='Item Description')),
                ('description_en_gb', models.CharField(max_length=100, null=True, verbose_name='Item Description')),
                ('description_en_ca', models.CharField(max_length=100, null=True, verbose_name='Item Description')),
                ('button_text', models.CharField(max_length=50, verbose_name='Item Button Text')),
                ('button_text_en_us', models.CharField(max_length=50, null=True, verbose_name='Item Button Text')),
                ('button_text_en_gb', models.CharField(max_length=50, null=True, verbose_name='Item Button Text')),
                ('button_text_en_ca', models.CharField(max_length=50, null=True, verbose_name='Item Button Text')),
            ],
        ),
    ]
