# Generated by Django 3.0.6 on 2020-07-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('des', models.TextField()),
                ('img', models.URLField()),
                ('url', models.URLField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
