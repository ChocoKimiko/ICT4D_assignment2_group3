# Generated by Django 2.2 on 2019-04-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0002_auto_20190418_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='seed_type',
            field=models.CharField(max_length=200),
        ),
    ]
