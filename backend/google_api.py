import requests

GOOGLE_API_KEY = "PASTE_YOUR_KEY"

def get_nearby_hospitals_google(lat, lng):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": 8000,
        "type": "hospital",
        "key": GOOGLE_API_KEY
    }
    res = requests.get(url, params=params).json()
    hospitals = []
    for i, h in enumerate(res.get("results", [])[:10]):
        hospitals.append({
            "id": i+1,
            "name": h["name"],
            "distance": 5  # computed later
        })
    return hospitals
