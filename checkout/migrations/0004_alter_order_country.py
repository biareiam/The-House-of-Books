# Generated by Django 3.2 on 2022-05-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220501_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='Ireland', max_length=40),
        ),
    ]