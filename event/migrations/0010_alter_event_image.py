# Generated by Django 3.2.9 on 2021-11-28 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='eventimg'),
        ),
    ]
