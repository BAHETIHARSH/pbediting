# Generated by Django 3.0.6 on 2020-07-09 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200708_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.URLField(),
        ),
    ]
