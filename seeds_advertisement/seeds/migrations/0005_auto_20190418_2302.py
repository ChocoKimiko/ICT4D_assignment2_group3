# Generated by Django 2.2 on 2019-04-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0004_auto_20190418_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='region',
            field=models.CharField(choices=[('Kayes', 'Kayes'), ('Koulikoro', 'Koulikoro'), ('Bamako', 'Bamako'), ('Sikasso', 'Sikasso'), ('Segou', 'Ségou'), ('Mopti', 'Mopti'), ('Tombouctou', 'Tombouctou'), ('Gao', 'Gao'), ('Kidal', 'Kidal')], max_length=10),
        ),
    ]
