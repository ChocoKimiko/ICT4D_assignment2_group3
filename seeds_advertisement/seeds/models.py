import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
from enum import Enum


class RegionChoice(Enum):   # A subclass of Enum
    Kayes = "Kayes"
    Koulikoro = "Koulikoro"
    Bamako = "Bamako"
    Sikasso = "Sikasso"
    Segou = "Ségou"
    Mopti = "Mopti"
    Tombouctou = "Tombouctou"
    Gao = "Gao"
    Kidal = "Kidal"


class Farmer(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=9)
    full_name = models.CharField(max_length=70)
    region = models.CharField(
      max_length=10,
      choices=[(tag.name, tag.value) for tag in RegionChoice]  # Choices is a list of Tuple
    )
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Advertisement(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    seed = models.CharField(max_length=200)
    seed_type = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    price = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)])
    pub_date = models.DateTimeField('date published')

    class Meta:
        unique_together = (('farmer', 'pub_date'),)
        unique_together = (('farmer', 'seed_type'),)

    def __str__(self):
        return self.seed + " - " + self.seed_type

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
