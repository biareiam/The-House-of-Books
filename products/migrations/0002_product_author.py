# Generated by Django 3.2 on 2022-04-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
