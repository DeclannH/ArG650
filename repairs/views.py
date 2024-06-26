from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient
from django.conf import settings

# MongoDB setup 
client = MongoClient(settings.MONGODB_URI)
db = client.get_database("ARMechanicGlasses")  
vehicles_collection = db['vehicles']
repairs_collection = db['repairs']

def home(request):
    return render(request, 'repairs/home.html')

def vehicle_selection(request):
    return render(request, 'repairs/vehicle_selection.html')

@csrf_exempt
def get_dropdown_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        response_data = {}

        if 'year' in data:
            response_data['makes'] = get_makes_for_year(data['year'])
        elif 'make' in data:
            response_data['models'] = get_models_for_make(data['make'])
        elif 'model' in data:
            response_data['trims'] = get_trims_for_model(data['model'])
        elif 'repair_type' in data:
            response_data['repairs'] = get_repairs_for_type(data['repair_type'])

        return JsonResponse(response_data)

    return JsonResponse({})

def get_makes_for_year(year):
    makes = vehicles_collection.distinct("make", {"year": year})
    return makes

def get_models_for_make(make):
    models = vehicles_collection.distinct("model", {"make": make})
    return models

def get_trims_for_model(model):
    trims = vehicles_collection.distinct("trim", {"model": model})
    return trims

def get_repairs_for_type(repair_type):
    repairs = repairs_collection.distinct("repair", {"type": repair_type})
    return repairs
