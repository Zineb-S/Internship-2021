# Generated by Django 3.2.6 on 2021-08-17 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-pk', '-publish_date', '-updated', '-timestamp']},
        ),
    ]