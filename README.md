# 🏥 Emergency Hospital Finder & Waiting Time Predictor

## 📌 Overview
Emergency Hospital Finder is a location-based healthcare assistance system designed to help users quickly identify nearby hospitals during medical emergencies. The platform displays critical hospital details such as estimated waiting time, queue length, available doctors, available beds, and distance, enabling faster and more informed decision-making.

This project was built as part of a hackathon to address delays in emergency hospital admissions caused by lack of real-time hospital availability information.

---

## 🚨 Problem Statement
During medical emergencies, patients and caregivers often waste crucial time searching for hospitals without knowing:
- Current crowd level
- Bed availability
- Doctor availability
- Estimated waiting time

This lack of transparency can result in delayed treatment and increased risk.

---

## 💡 Solution
The system provides:
- A list of nearby hospitals
- AI-based waiting time prediction using hospital load parameters
- Easy-to-use interface for viewing hospital details
- A scalable backend architecture that can integrate real hospital APIs in the future

---

## ⚙️ Features
- Hospital listing based on location
- AI-predicted waiting time
- Queue length display
- Available beds & doctors information
- Distance from user
- Simple and clean frontend UI
- Modular backend–frontend architecture

---

## 🧠 Technology Stack
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn
- **Frontend:** HTML, CSS, JavaScript
- **Version Control:** Git & GitHub

---

## 🗂️ Project Structure
 emergency-hospital-ai/
├── backend/
│ ├── app.py
│ ├── model.py
│ ├── model.pkl
│ └── realtime_api.py
└── frontend/
└── index.html


---

## 🚀 How It Works
1. User opens the application
2. System lists nearby hospitals
3. User clicks on a hospital name
4. The system displays hospital details including:
   - Estimated waiting time
   - Queue length
   - Available beds
   - Available doctors
   - Distance

---

## 🔮 Future Scope
- Integration with real-time hospital APIs
- Live GPS-based user location
- Multi-city hospital coverage
- Ambulance routing and ETA estimation
- Real-time bed availability dashboards

---

## 👨‍💻 Hackathon Note
The dataset used for training the model is simulated but structured to reflect real-world hospital load conditions. The architecture is production-ready and can be connected to live hospital data sources.

---

## 📜 License
This project is developed for educational and hackathon purposes.
