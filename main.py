import os
import pandas as pd
import pickle
from flask import Flask, request, jsonify
from preprocess import preprocess_data_tinggi, preprocess_data_berat

app = Flask(__name__)

# Load models
with open('./models/Final_model.pkl', 'rb') as f:
    model_tb = pickle.load(f)

with open('./models/BeratBadan_model.pkl', 'rb') as f:
    model_bb = pickle.load(f)

# Load reference data
df_tb_lk = pd.read_csv('./referensi/TinggiBadan_lakiLaki - Sheet1.csv')
df_tb_pr = pd.read_csv('./referensi/TinggiBadan_Perempuan - Sheet1.csv')
df_bb_lk = pd.read_csv('./referensi/BeratBadan_lakiLaki - Sheet1.csv')
df_bb_pr = pd.read_csv('./referensi/BeratBadan_Perempuan - Sheet1.csv')

# Mapping hasil prediksi model
tb_encoding = {0: 'tinggi', 1: 'normal', 2: 'stunted', 3: 'severely stunted'}
bb_encoding = {0: 'overweight', 1: 'normal', 2: 'severely underweight', 3: 'underweight'}

# WHO classification functions
def hitung_z_score(nilai, row):
    median = row['Median']
    sd1 = row['1 SD'] - median
    return (nilai - median) / sd1

def klasifikasi_tb_u(z):
    if z < -3:
        return "severely stunted"
    elif -3 <= z < -2:
        return "stunted"
    elif -2 <= z <= 3:
        return "normal"
    else:
        return "tinggi"

def klasifikasi_bb_u(z):
    if z < -3:
        return "severely underweight"
    elif -3 <= z < -2:
        return "underweight"
    elif -2 <= z <= 1:
        return "normal"
    else:
        return "overweight"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Cek apakah semua field penting ada
        required_fields = ['Jenis Kelamin', 'Umur (bulan)', 'Tinggi Badan (cm)', 'Berat Badan (kg)']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f'Field berikut tidak ditemukan: {", ".join(missing_fields)}'}), 400

        # Validasi tipe data dan isi
        try:
            sex = data['Jenis Kelamin'].lower()
            if sex not in ['laki-laki', 'perempuan']:
                return jsonify({'error': 'Jenis Kelamin harus "laki-laki" atau "perempuan"'}), 400

            age = int(data['Umur (bulan)'])
            if age < 0:
                return jsonify({'error': 'Umur (bulan) tidak boleh negatif'}), 400

            tinggi = float(data['Tinggi Badan (cm)'])
            berat = float(data['Berat Badan (kg)'])

        except ValueError:
            return jsonify({'error': 'Jenis Kelamin harus teks, Umur, Tinggi Badan, dan Berat Badan harus numerik'}), 400

        result = {}

        # --- Tinggi Badan ---
        df_tb = df_tb_lk if sex == 'laki-laki' else df_tb_pr
        row_tb = df_tb[df_tb['Umur (bulan)'] == age]
        if not row_tb.empty:
            row_tb = row_tb.iloc[0]
            z_tb = hitung_z_score(tinggi, row_tb)
            who_tb = klasifikasi_tb_u(z_tb)

            model_tb_input = preprocess_data_tinggi(age, sex, tinggi)
            ml_tb = tb_encoding[model_tb.predict(model_tb_input)[0]]
            final_tb = ml_tb if ml_tb == who_tb else who_tb

            result['Tinggi Badan'] = {
                'Z-score': round(z_tb, 2),
                'WHO': who_tb,
                'ML': ml_tb,
                'Final': final_tb
            }
        else:
            result['Tinggi Badan'] = {'error': 'Data referensi WHO tidak tersedia untuk umur ini'}

        # --- Berat Badan ---
        df_bb = df_bb_lk if sex == 'laki-laki' else df_bb_pr
        row_bb = df_bb[df_bb['Umur (bulan)'] == age]
        if not row_bb.empty:
            row_bb = row_bb.iloc[0]
            z_bb = hitung_z_score(berat, row_bb)
            who_bb = klasifikasi_bb_u(z_bb)

            model_bb_input = preprocess_data_berat(age, berat, sex)
            ml_bb = bb_encoding[model_bb.predict(model_bb_input)[0]]
            final_bb = ml_bb if ml_bb == who_bb else who_bb

            result['Berat Badan'] = {
                'Z-score': round(z_bb, 2),
                'WHO': who_bb,
                'ML': ml_bb,
                'Final': final_bb
            }
        else:
            result['Berat Badan'] = {'error': 'Data referensi WHO tidak tersedia untuk umur ini'}

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'Terjadi kesalahan server: {str(e)}'}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
