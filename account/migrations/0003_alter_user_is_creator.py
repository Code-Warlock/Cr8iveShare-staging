# Generated by Django 4.0.4 on 2022-12-31 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_is_viewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_creator',
            field=models.BooleanField(default=False, verbose_name='Content Creator'),
        ),
    ]
