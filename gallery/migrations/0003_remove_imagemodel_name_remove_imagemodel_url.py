# Generated by Django 4.2 on 2023-05-02 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_rename_image_imagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='url',
        ),
    ]
