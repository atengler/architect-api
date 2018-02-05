# Generated by Django 2.0.1 on 2018-02-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='engine',
            field=models.CharField(default='prometheus', max_length=32),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='status',
            field=models.CharField(default='active', max_length=32),
        ),
    ]
