from pymongo import MongoClient

# MongoDB setup - Replace with your MongoDB connection details
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
vehicles_collection = db['vehicles']
repairs_collection = db['repairs']

# Clear existing data
vehicles_collection.delete_many({})
repairs_collection.delete_many({})

# Example data
vehicles_collection.insert_many([
    {"year": 2020, "make": "Toyota", "model": "Camry", "trim": "LE"},
    {"year": 2020, "make": "Toyota", "model": "Camry", "trim": "SE"},
    {"year": 2021, "make": "Ford", "model": "F-150", "trim": "XLT"},
    {"year": 2021, "make": "Chevrolet", "model": "Silverado", "trim": "LT"},
    {"year": 2022, "make": "BMW", "model": "X5", "trim": "xDrive40i"},
    {"year": 2022, "make": "Mercedes", "model": "C-Class", "trim": "C300"},
    # Add more data as needed
])

repairs_collection.insert_many([
    {"type": "engine", "repair": "Oil Change"},
    {"type": "engine", "repair": "Spark Plug Replacement"},
    {"type": "transmission", "repair": "Fluid Change"},
    {"type": "transmission", "repair": "Filter Replacement"},
    {"type": "brakes", "repair": "Brake Pad Replacement"},
    {"type": "brakes", "repair": "Rotor Replacement"},
    # Add more data as needed
])

print("Database populated successfully!")
