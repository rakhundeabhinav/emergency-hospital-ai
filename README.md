# 🏥 Emergency Hospital Finder & Waiting Time Predictor

## 📌 Project Description
Emergency Hospital Finder is a healthcare assistance system designed to help users quickly identify nearby hospitals during medical emergencies. The platform displays important hospital details such as estimated waiting time, queue length, available doctors, available beds, and distance, enabling faster and informed decision-making.

The backend uses a machine learning model trained on hospital load parameters to predict waiting time, while the frontend provides a simple and user-friendly interface to view hospital information.

This project was developed as part of a hackathon to address delays in emergency hospital admissions.

---
##  📌 Project Structure: 
emergency-hospital-ai/
│
├── README.md
│
├── backend/
│   │
│   ├── app.py              # Flask backend (API + routes)
│   ├── model.py            # ML model training script
│   ├── model.pkl           # Trained ML model (important)
│   ├── data.csv            # Dataset used for training
│   ├── requirements.txt    # Python dependencies
│   └── realtime_api.py     # (Optional) future real-time data logic
│
├── frontend/
│   │
│   ├── index.html          # Main UI page
│   ├── styles.css          # UI styling
│   └── script.js           # Frontend logic (API calls)
│
└── .gitignore              # Ignore unnecessary files


## ▶️ How to Run the Project

### 1️⃣ Download the Project
Clone or download this repository from GitHub.

### 2️⃣ Run Backend Server
Make sure Python (3.8 or above) is installed.

Open terminal in the project folder and run:
cd backend
python model.py
python app.py


Backend will start at:
http://127.0.0.1:5000/


### 3️⃣ Open Frontend
Open the following file in any web browser:
frontend/index.html


### 4️⃣ Use the Application
- The homepage displays a list of hospitals
- Click on any hospital name to view:
  - Estimated waiting time
  - Queue length
  - Available beds
  - Available doctors
  - Distance

---

## 🛠️ Technologies Used
- Python (Flask)
- Machine Learning (Scikit-learn)
- HTML, CSS, JavaScript
- Git & GitHub

---

## 📜 Note
The dataset used is simulated for demonstration purposes. The system architecture is scalable and can be integrated with real-time hospital data APIs in the future.



