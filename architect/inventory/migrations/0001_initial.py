# Generated by Django 2.0.1 on 2018-02-13 17:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('engine', models.CharField(default='reclass', max_length=32)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('cache', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('status', models.CharField(default='unknown', max_length=32)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Inventories',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=511)),
                ('name', models.CharField(max_length=511)),
                ('kind', models.CharField(max_length=32)),
                ('size', models.IntegerField(default=1)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('cache', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('status', models.CharField(default='unknown', max_length=32)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='inventory.Inventory')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
