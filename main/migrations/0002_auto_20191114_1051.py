# Generated by Django 2.1.7 on 2019-11-14 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='competitor',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='class_code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='score',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='weight',
            field=models.CharField(max_length=100),
        ),
    ]
