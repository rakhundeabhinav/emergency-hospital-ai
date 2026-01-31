import math
import random

PUNE_HOSPITALS = [
    {"id": 1, "name": "Ruby Hall Clinic", "lat": 18.5314, "lng": 73.8760},
    {"id": 2, "name": "Jehangir Hospital", "lat": 18.5286, "lng": 73.8746},
    {"id": 3, "name": "Deenanath Mangeshkar Hospital", "lat": 18.5074, "lng": 73.8077},
    {"id": 4, "name": "Sassoon General Hospital", "lat": 18.5288, "lng": 73.8741},
    {"id": 5, "name": "Sahyadri Hospital", "lat": 18.5204, "lng": 73.8567},
    {"id": 6, "name": "Columbia Asia Hospital", "lat": 18.5610, "lng": 73.8086},
    {"id": 7, "name": "Noble Hospital", "lat": 18.5018, "lng": 73.9270},
    {"id": 8, "name": "Aditya Birla Memorial Hospital", "lat": 18.6279, "lng": 73.7767}
]

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return round(2 * R * math.asin(math.sqrt(a)), 2)

def get_pune_hospitals_with_details(user_lat, user_lng):
    hospitals = []

    for h in PUNE_HOSPITALS:
        distance = calculate_distance(user_lat, user_lng, h["lat"], h["lng"])
        eta = max(5, round(distance * random.uniform(2.8, 4.0), 1))

        queue = random.randint(8, 45)
        beds = random.randint(3, 30)
        doctors = random.randint(3, 18)

        hospitals.append({
            "id": h["id"],
            "name": h["name"],
            "distance": distance,
            "eta": eta,
            "queue": queue,
            "beds": beds,
            "doctors": doctors
        })

    hospitals.sort(key=lambda x: x["distance"])
    return hospitals
