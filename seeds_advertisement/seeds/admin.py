from django.contrib import admin
from .models import Farmer, Advertisement


class AdvertisementInline(admin.StackedInline):
    model = Advertisement
    extra = 1


class FarmerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'region')
    fieldsets = [
        (None, {'fields': ['full_name']}),
        ('Other information', {'fields': ['phone_number', 'region', 'place']}),
    ]
    inlines = [AdvertisementInline]
    search_fields = ['full_name']


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('seed', 'seed_type', 'farmer', 'pub_date', 'was_published_recently')
    fieldsets = [
        ('Seed information', {'fields': ['seed', 'seed_type', 'description', 'quantity', 'price', 'pub_date']}),
        ('Farmer information', {'fields': ['farmer']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['seed']


admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
