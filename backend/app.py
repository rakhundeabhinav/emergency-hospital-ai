from flask import Flask, jsonify, request, send_from_directory
import os
import pickle
from realtime_api import get_pune_hospitals_with_details

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "../frontend"),
    static_url_path=""
)

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/hospitals")
def hospitals():
    lat = float(request.args.get("lat"))
    lng = float(request.args.get("lng"))

    hospitals = get_pune_hospitals_with_details(lat, lng)

    # Add AI prediction ONCE
    for h in hospitals:
        predicted = model.predict([[
            h["queue"],
            h["beds"],
            h["doctors"],
            h["distance"]
        ]])[0]

        h["predicted_time"] = max(5, round(predicted, 1))

    return jsonify(hospitals)

if __name__ == "__main__":
    app.run(debug=True)
