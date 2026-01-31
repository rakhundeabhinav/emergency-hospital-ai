# 🚑 Emergency Hospital Finder

## 📌 Project Description
Emergency Hospital Finder is a healthcare assistance system that helps users find nearby hospitals and view important details required during medical emergencies. The system displays hospital information such as estimated waiting time, queue length, available doctors, available beds, and distance. A machine learning model is used to predict waiting time based on hospital load parameters.

This project was developed as part of a hackathon.

---

## ▶️ How to Run the Project

### Backend
Make sure Python is installed.

cd backend
python model.py
python app.py


Backend will start at:
http://127.0.0.1:5000/


---

## 📁 Project Structure

EMERGENCY-HOSPITAL-AI/
│
├── backend/
│ ├── app.py
│ ├── model.py
│ ├── model.pkl
│ ├── realtime_api.py
│ ├── google_api.py
│ └── requirements.txt
│
├── frontend/
│ └── index.html


---

## 🛠️ Tech Stack
- Python (Flask)
- Machine Learning
- HTML, CSS, JavaScript


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






