# Generated by Django 4.0.3 on 2022-03-15 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_petphoto_photo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together=set(),
        ),
    ]
