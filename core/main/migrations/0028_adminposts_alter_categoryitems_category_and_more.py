# Generated by Django 4.1.6 on 2023-04-07 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_recommendeditems'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Post Title')),
                ('img', models.ImageField(upload_to='', verbose_name='Post Image')),
                ('description', models.TextField(verbose_name='Item Description')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='categoryitems',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AlterField(
            model_name='shopprod',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Item Description'),
        ),
        migrations.AlterField(
            model_name='shopprod',
            name='description_en_ca',
            field=models.CharField(max_length=255, null=True, verbose_name='Item Description'),
        ),
        migrations.AlterField(
            model_name='shopprod',
            name='description_en_gb',
            field=models.CharField(max_length=255, null=True, verbose_name='Item Description'),
        ),
        migrations.AlterField(
            model_name='shopprod',
            name='description_en_us',
            field=models.CharField(max_length=255, null=True, verbose_name='Item Description'),
        ),
    ]