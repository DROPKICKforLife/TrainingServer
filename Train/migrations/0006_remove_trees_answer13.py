# Generated by Django 2.0b1 on 2017-11-14 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Train', '0005_auto_20171114_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trees',
            name='Answer13',
        ),
    ]
