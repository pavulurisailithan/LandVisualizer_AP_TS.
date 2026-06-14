from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os, math

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

DEFAULT_LAND = {
    "name": "Premium Plot - AP & TS Region",
    "location": "Amaravati, Andhra Pradesh & Telangana",
    "gps": {"lat": 17.4065, "lng": 78.3772},
    "area_sqft": 4800,
    "area_acres": round(4800 / 43560, 4),
    "dimensions": {"north": 60, "south": 60, "east": 80, "west": 80},
    "corners": {"NE": 90, "NW": 90, "SE": 90, "SW": 90},
    "road_width_feet": 30,
    "facing": "East",
    "survey_number": "Survey No. 142/B",
    "price_per_sqft": 4500,
    "total_price": 4800 * 4500,
    "roads": [
        {"name": "Main Road (NH-65)", "direction": "East", "width": 30, "distance": 0},
        {"name": "Inner Road", "direction": "North", "width": 20, "distance": 0}
    ],
    "landmarks": [
        {"name": "Shopping Mall", "distance": "0.5 km", "direction": "NE"},
        {"name": "APCRDA Office", "distance": "0.8 km", "direction": "N"},
        {"name": "Apollo Hospital", "distance": "1.2 km", "direction": "W"},
        {"name": "TSRTC Bus Stand", "distance": "2.0 km", "direction": "SE"},
        {"name": "Cyber Towers TS", "distance": "1.5 km", "direction": "S"}
    ],
    "water_resources": {
        "borewell": True,
        "borewell_depth_ft": 120,
        "underground_water": "High Availability",
        "drainage": "Municipal Drainage Connected",
        "pond": False,
        "canal": {"available": True, "name": "Krishna Canal", "distance": "1.8 km"},
        "river": {"available": True, "name": "Godavari River", "distance": "3.2 km"},
        "rainwater_harvesting": True
    },
    "topography": {
        "terrain": "Flat",
        "elevation_ft": 536,
        "slope_percent": 1.5,
        "soil_type": "Red Laterite Soil",
        "soil_bearing_capacity": "18 tons/sqm",
        "vegetation": "Sparse Shrubs",
        "green_area_percent": 20
    },
    "feasibility": {
        "zone": "Residential + Commercial (Mixed Use)",
        "max_floors": 4,
        "fsr": 2.5,
        "max_built_up_sqft": 4800 * 2.5,
        "ground_coverage_percent": 60,
        "setbacks": {"front": 6, "rear": 3, "sides": 3},
        "parking_slots": 8,
        "parking_area_sqft": 800,
        "open_space_sqft": 1920,
        "future_potential": "High — AP Capital Region & TS IT Corridor"
    }
}

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/api/land', methods=['GET'])
def get_land():
    return jsonify(DEFAULT_LAND)

@app.route('/api/land', methods=['POST'])
def update_land():
    data = request.json
    land = DEFAULT_LAND.copy()
    if data.get('area_sqft'):
        sqft = float(data['area_sqft'])
        land['area_sqft'] = sqft
        land['area_acres'] = round(sqft / 43560, 4)
        land['total_price'] = sqft * land['price_per_sqft']
        land['feasibility']['max_built_up_sqft'] = sqft * land['feasibility']['fsr']
        land['feasibility']['parking_slots'] = max(2, int(sqft / 600))
        land['feasibility']['parking_area_sqft'] = land['feasibility']['parking_slots'] * 100
        land['feasibility']['open_space_sqft'] = int(sqft * 0.4)
    if data.get('location'):
        land['location'] = data['location']
    if data.get('max_floors'):
        land['feasibility']['max_floors'] = int(data['max_floors'])
    if data.get('water_source'):
        land['water_resources']['underground_water'] = data['water_source']
    if data.get('road_width'):
        land['road_width_feet'] = float(data['road_width'])
        land['roads'][0]['width'] = float(data['road_width'])
    if data.get('price_per_sqft'):
        land['price_per_sqft'] = float(data['price_per_sqft'])
        land['total_price'] = land['area_sqft'] * float(data['price_per_sqft'])
    return jsonify(land)

@app.route('/api/feasibility', methods=['POST'])
def calc_feasibility():
    d = request.json
    sqft = float(d.get('area_sqft', 4800))
    floors = int(d.get('floors', 4))
    fsr = float(d.get('fsr', 2.5))
    coverage = float(d.get('ground_coverage', 60)) / 100
    built_up = sqft * fsr
    ground_floor_area = sqft * coverage
    parking = max(2, int(sqft / 600))
    open_space = sqft * (1 - coverage)
    return jsonify({
        "total_built_up_sqft": round(built_up),
        "ground_floor_area_sqft": round(ground_floor_area),
        "per_floor_area_sqft": round(ground_floor_area),
        "total_floors": floors,
        "parking_slots": parking,
        "parking_area_sqft": parking * 100,
        "open_space_sqft": round(open_space),
        "efficiency_percent": round((built_up / (sqft * floors)) * 100, 1)
    })

if __name__ == '__main__':
    print("🏗️  Land Visualizer Backend running at http://localhost:5000")
    app.run(debug=True, port=5000)
