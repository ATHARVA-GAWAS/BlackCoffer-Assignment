# Generated by Django 5.0 on 2023-12-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_alter_data_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
