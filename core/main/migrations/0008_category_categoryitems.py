# Generated by Django 4.1.6 on 2023-04-03 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_featuresitems_price_en_ca_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveBigIntegerField(verbose_name='Item Price')),
                ('img', models.ImageField(upload_to='', verbose_name='Item Image')),
                ('description', models.CharField(max_length=100, verbose_name='Item Description')),
                ('button_text', models.CharField(max_length=50, verbose_name='Item Button Text')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
        ),
    ]
