from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient

# Below is mock database information to show the working display
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
    makes = {
        2020: ['Toyota', 'Ford'],
        2021: ['Chevrolet', 'BMW'],
        2022: ['Mercedes', 'Honda']
    }
    return makes.get(year, [])

def get_models_for_make(make):
    models = {
        'Toyota': ['Camry', 'Corolla'],
        'Ford': ['F-150', 'Mustang'],
        'Chevrolet': ['Silverado', 'Malibu'],
        'BMW': ['X5', 'X3'],
        'Mercedes': ['C-Class', 'E-Class'],
        'Honda': ['Civic', 'Accord']
    }
    return models.get(make, [])

def get_trims_for_model(model):
    trims = {
        'Camry': ['LE', 'SE'],
        'Corolla': ['L', 'XLE'],
        'F-150': ['XLT', 'Lariat'],
        'Mustang': ['EcoBoost', 'GT'],
        'Silverado': ['LT', 'High Country'],
        'Malibu': ['LS', 'RS'],
        'X5': ['xDrive40i', 'xDrive50i'],
        'X3': ['sDrive30i', 'xDrive30i'],
        'C-Class': ['C300', 'C43'],
        'E-Class': ['E350', 'E450'],
        'Civic': ['EX', 'Touring'],
        'Accord': ['LX', 'Sport']
    }
    return trims.get(model, [])

def get_repairs_for_type(repair_type):
    repairs = {
        'engine': ['Oil Change', 'Spark Plug Replacement'],
        'transmission': ['Fluid Change', 'Filter Replacement'],
        'brakes': ['Brake Pad Replacement', 'Rotor Replacement']
    }
    return repairs.get(repair_type, [])


# Below is the code setup for the Database
# # MongoDB setup - Replace with your MongoDB connection details
# client = MongoClient('mongodb://localhost:27017/')
# db = client['your_database_name']
# vehicles_collection = db['vehicles']
# repairs_collection = db['repairs']

# def home(request):
#     return render(request, 'repairs/home.html')

# def vehicle_selection(request):
#     return render(request, 'repairs/vehicle_selection.html')

# @csrf_exempt
# def get_dropdown_data(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         response_data = {}

#         if 'year' in data:
#             response_data['makes'] = get_makes_for_year(data['year'])
#         elif 'make' in data:
#             response_data['models'] = get_models_for_make(data['make'])
#         elif 'model' in data:
#             response_data['trims'] = get_trims_for_model(data['model'])
#         elif 'repair_type' in data:
#             response_data['repairs'] = get_repairs_for_type(data['repair_type'])

#         return JsonResponse(response_data)

#     return JsonResponse({})

# def get_makes_for_year(year):
#     makes = vehicles_collection.distinct("make", {"year": year})
#     return makes

# def get_models_for_make(make):
#     models = vehicles_collection.distinct("model", {"make": make})
#     return models

# def get_trims_for_model(model):
#     trims = vehicles_collection.distinct("trim", {"model": model})
#     return trims

# def get_repairs_for_type(repair_type):
#     repairs = repairs_collection.distinct("repair", {"type": repair_type})
#     return repairs
