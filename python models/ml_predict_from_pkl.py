import joblib
import numpy as np

# Load model only once
model = joblib.load("C:/Users/sarth/OneDrive/Desktop/ML/gradient_boosting_model.pkl")

def predict(input_data):
    input_array = np.array(input_data)
    if input_array.ndim == 1:
        input_array = input_array.reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction.tolist()
