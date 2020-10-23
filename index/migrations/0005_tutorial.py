# Generated by Django 3.0.6 on 2020-07-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200709_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('descripation', models.TextField()),
                ('type', models.CharField(choices=[('CS3', 'CS3'), ('CC', 'CC')], max_length=10)),
                ('link', models.URLField()),
            ],
        ),
    ]
