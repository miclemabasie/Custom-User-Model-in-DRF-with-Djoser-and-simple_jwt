# Generated by Django 3.2 on 2022-07-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Bamenda', max_length=200, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Cameroon', max_length=200, null=True, verbose_name='Country'),
        ),
    ]
