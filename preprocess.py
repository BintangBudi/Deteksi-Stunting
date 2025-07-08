import numpy as np
import joblib

# Load scaler model (bisa satu jika digunakan bersama, atau ubah path jika terpisah)
scaler_tb = joblib.load("./standarization_model.joblib")  # Untuk tinggi badan
scaler_bb = joblib.load("./standarization_model.joblib")  # Untuk berat badan

# Label encoding untuk jenis kelamin
sex_encoding = {'laki-laki': 1, 'perempuan': 0}

# ===================== Preprocessing untuk Tinggi Badan (Stunting) ===================== #
def preprocess_data_tinggi(age, sex, body_length):
    sex_encoded = sex_encoding.get(sex.lower())
    if sex_encoded is None:
        raise ValueError(f"Invalid sex value: {sex}. Must be 'laki-laki' or 'perempuan'.")
    
    data = np.array([[age, sex_encoded, body_length]])
    standarized_data = scaler_tb.transform(data)
    return standarized_data

# ===================== Preprocessing untuk Berat Badan (Gizi) ===================== #
def preprocess_data_berat(age, body_weight, sex):
    sex_encoded = sex_encoding.get(sex.lower())
    if sex_encoded is None:
        raise ValueError(f"Invalid sex value: {sex}. Must be 'laki-laki' or 'perempuan'.")
    
    data = np.array([[age, body_weight, sex_encoded]])
    standarized_data = scaler_bb.transform(data)
    return standarized_data
