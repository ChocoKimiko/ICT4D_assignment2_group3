# Generated by Django 2.2 on 2019-04-19 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0010_auto_20190419_0155'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='advertisement',
            unique_together={('farmer', 'seed_type')},
        ),
    ]
