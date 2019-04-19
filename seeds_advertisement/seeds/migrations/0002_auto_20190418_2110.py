# Generated by Django 2.2 on 2019-04-18 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='description',
            new_name='seed_type',
        ),
        migrations.AlterUniqueTogether(
            name='advertisement',
            unique_together={('seed', 'seed_type')},
        ),
    ]
