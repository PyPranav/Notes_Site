# Generated by Django 3.0.7 on 2020-09-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='text',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]