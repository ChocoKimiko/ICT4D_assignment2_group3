from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Farmer, Advertisement


def index_view(request):
    advertisements_count = Advertisement.objects.count()
    farmers_count = Farmer.objects.count()
    context = {
        'advertisements_count': advertisements_count,
        'farmers_count': farmers_count,
    }
    return render(request, 'seeds/index.html', context)


def advertisements_view(request):
    advertisement_list = Advertisement.objects.order_by('-farmer').order_by('-pub_date')
    context = {
        'advertisement_list': advertisement_list,
    }
    return render(request, 'seeds/advertisements.html', context)


def advertisements_detail_view(request, advertisement_id):
    advertisement = get_object_or_404(Advertisement, pk=advertisement_id)
    return render(request, 'seeds/advertisements_detail.html', {'advertisement': advertisement})


def farmers_view(request):
    farmer_list = Farmer.objects.order_by('-full_name')
    context = {
        'farmer_list': farmer_list,
    }
    return render(request, 'seeds/farmers.html', context)
