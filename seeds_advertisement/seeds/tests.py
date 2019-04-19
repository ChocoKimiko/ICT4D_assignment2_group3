import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Advertisement, RegionChoice, Farmer


class AdvertisementModelTests(TestCase):

    def test_was_published_recently_with_future_advertisement(self):
        """
        was_published_recently() returns False for advertisements whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_advertisement = Advertisement(pub_date=time)
        self.assertIs(future_advertisement.was_published_recently(), False)

    def test_was_published_recently_with_old_advertisement(self):
        """
        was_published_recently() returns False for advertisements whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_advertisement = Advertisement(pub_date=time)
        self.assertIs(old_advertisement.was_published_recently(), False)

    def test_was_published_recently_with_recent_advertisement(self):
        """
        was_published_recently() returns True for advertisements whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_advertisement = Advertisement(pub_date=time)
        self.assertIs(recent_advertisement.was_published_recently(), True)


def create_advertisement(farmer, seed, seed_type, description, quantity, price, pub_date):
    """
    Create an advertisement with the given `advertisement_text` and published the
    given number of `days` offset to now (negative for advertisements published
    in the past, positive for advertisements that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=pub_date)
    return Advertisement.objects.create(farmer=farmer, seed =seed,seed_type =seed_type, description=description, quantity=quantity, price=price, pub_date=time)


class AdvertisementIndexViewTests(TestCase):
    def test_no_advertisements(self):
        """
        If no advertisements exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('seeds_advertisement:advertisements'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no advertisements available.")
        self.assertQuerysetEqual(response.context['advertisement_list'], [])

    def test_past_advertisement(self):
        """
        Advertisements with a pub_date in the past are displayed on the
        index page.
        """
        f = Farmer(phone_number="098583850", full_name="Mariam Issa", region=RegionChoice.Mopti, place="Commerce")
        create_advertisement(farmer=f, seed ="Maize",seed_type ="Sotubaka", description="", quantity="492", price="340", pub_date=-30)
        response = self.client.get(reverse('seeds_advertisement:advertisements'))
        self.assertQuerysetEqual(
            response.context['advertisement_list'],
            ['<Advertisement: Maize - Sotubaka>']
        )
