# Generated by Django 2.0.7 on 2018-07-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0010_auto_20180717_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='click_rate',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='open_rate',
        ),
    ]