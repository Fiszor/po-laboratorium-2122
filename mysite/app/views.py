from gc import get_objects
from multiprocessing import context
from re import template
from django.http import HttpResponse
from .models import Generation, Model, Vehicle, Brand
from django.template import loader
from django.shortcuts import render

def index(request):
    index_list = Generation.objects, Vehicle.objects, Brand.objects, Model.objects
    template = loader.get_template('app/index.html')
    context = {
        'index_list': index_list,
    }
    return HttpResponse(template.render(context, request))

def generation(request):
    generation_list = Generation.objects.all
    template = loader.get_template('app/generation.html')
    context = {
        'generation_list': generation_list,
    }
    return HttpResponse(template.render(context, request))

def model(request):
    model_list = Model.objects.all
    template = loader.get_template('app/model.html')
    context = {
        'model_list': model_list,
    }
    return HttpResponse(template.render(context, request))

def brand(request):
    brand_list = Brand.objects.all
    template = loader.get_template('app/brand.html')
    context = {
        'brand_list': brand_list,
    }
    return HttpResponse(template.render(context, request))

def vehicle(request):
    vehicle_list = Vehicle.objects.all
    template = loader.get_template('app/vehicle.html')
    context = {
        'vehicle_list': vehicle_list
    }
    return HttpResponse(template.render(context, request))
