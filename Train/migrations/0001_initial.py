# Generated by Django 2.0b1 on 2017-11-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treeID', models.TextField(max_length=100, verbose_name='TREEID')),
                ('confirm', models.BooleanField(verbose_name='CONFIRM')),
                ('confirmDATE', models.DateTimeField(auto_now=True, verbose_name='CONFIRMDATE')),
                ('Answer1', models.IntegerField(max_length=5, verbose_name='Answer1')),
                ('Answer2', models.IntegerField(max_length=5, verbose_name='Answer2')),
                ('Answer3', models.IntegerField(max_length=5, verbose_name='Answer3')),
                ('Answer4', models.IntegerField(max_length=5, verbose_name='Answer4')),
                ('Answer5', models.IntegerField(max_length=5, verbose_name='Answer5')),
                ('Answer6', models.IntegerField(max_length=5, verbose_name='Answer6')),
                ('Answer7', models.IntegerField(max_length=5, verbose_name='Answer7')),
                ('Answer8', models.IntegerField(max_length=5, verbose_name='Answer8')),
                ('Answer9', models.IntegerField(max_length=5, verbose_name='Answer9')),
                ('Answer10', models.IntegerField(max_length=5, verbose_name='Answer10')),
            ],
        ),
    ]