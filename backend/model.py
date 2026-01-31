import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("data.csv")

X = data[['queue_length', 'available_beds', 'doctors_available', 'distance_km']]

y = (
    data['queue_length'] * 1.2
    - data['available_beds'] * 2
    - data['doctors_available'] * 3
    + data['distance_km'] * 1.5
)

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
print("Model trained")
