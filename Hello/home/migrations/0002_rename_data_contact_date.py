# Generated by Django 4.0.3 on 2022-03-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='data',
            new_name='date',
        ),
    ]
