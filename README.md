# Child Nutritional Status & Stunting Detection API

Repositori ini berisi kode sumber untuk REST API yang dikembangkan untuk mengklasifikasikan **status gizi anak** dan **mendeteksi stunting** berdasarkan data antropometri. Proyek ini memanfaatkan algoritma **Support Vector Machine (SVM)** dan dirancang untuk diintegrasikan ke dalam aplikasi klien seperti **Gerakan Sayang Anak** oleh **DP3A (Dinas Pemberdayaan Perempuan dan Perlindungan Anak) Kalimantan Barat**.

Tujuan utama proyek ini adalah untuk menyediakan **layanan klasifikasi real-time** yang andal untuk digunakan oleh **tenaga kesehatan** dan **orang tua** dalam memantau pertumbuhan anak, memungkinkan **deteksi dini dan intervensi** untuk masalah gizi seperti stunting.

---

## 📚 Daftar Isi

1. [Tentang Proyek](#tentang-proyek)

   * [Fitur Utama](#fitur-utama)
   * [Dibangun Dengan](#dibangun-dengan)
2. [Memulai](#memulai)

   * [Prasyarat](#prasyarat)
   * [Instalasi](#instalasi)
3. [Penggunaan](#penggunaan)

   * [Cara Kerja](#cara-kerja)
   * [Endpoint API](#endpoint-api)
4. [Berkontribusi](#berkontribusi)
5. [Lisensi](#lisensi)
6. [Kontak](#kontak)
7. [Ucapan Terima Kasih](#ucapan-terima-kasih)

---

## Tentang Proyek

### Fitur Utama

* **Model Klasifikasi Ganda**:
  Mengimplementasikan dua model SVM terpisah:

  1. **Deteksi Stunting** berdasarkan **Tinggi Badan menurut Umur (TB/U)**
  2. **Klasifikasi Status Gizi** berdasarkan **Berat Badan menurut Umur (BB/U)**

* **Integrasi Standar WHO**:
  Menggunakan kalkulator **Z-score** berdasarkan standar pertumbuhan WHO untuk memberikan referensi medis terhadap klasifikasi.

* **Respons Output Ganda**:
  API mengembalikan hasil **prediksi Machine Learning** dan klasifikasi berdasarkan **Z-score WHO**, memungkinkan validasi hasil yang lebih kuat.

* **Siap untuk Integrasi**:
  Dibuat sebagai REST API menggunakan **Flask**, sehingga mudah diintegrasikan dengan berbagai aplikasi klien (mobile/web).

* **Di-deploy di Cloud**:
  Layanan API dikontainerisasi dengan **Docker** dan di-deploy di **Google Cloud Run** untuk skalabilitas dan ketersediaan tinggi.

### Dibangun Dengan

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Docker
* Google Cloud Run

---

## Memulai

Untuk menjalankan salinan lokal proyek ini, ikuti langkah-langkah berikut:

### Prasyarat

* Python 3.9+
* Docker (opsional)

### Instalasi

```bash
# 1. Kloning repositori ini
git clone https://github.com/[Nama-Pengguna-GitHub-Anda]/[Nama-Repositori-Anda].git

# 2. Masuk ke direktori proyek
cd [Nama-Repositori-Anda]

# 3. Instal paket Python yang diperlukan
pip install -r requirements.txt

# 4. Jalankan aplikasi Flask secara lokal
python main.py
```

Aplikasi akan berjalan di `http://127.0.0.1:5000`.

---

## Penggunaan

### Cara Kerja

1. API memvalidasi data input.
2. Menghitung Z-score dan menentukan klasifikasi WHO untuk **TB/U** dan **BB/U**.
3. Melakukan pra-pemrosesan data dan mengirimkan ke masing-masing model **SVM**.
4. Mengembalikan hasil prediksi dan klasifikasi akhir dalam format JSON.

### Endpoint API

**POST** `/predict`
Menerima permintaan JSON seperti berikut:

#### Contoh Request:

```json
{
    "Umur (bulan)": 24,
    "Jenis Kelamin": "perempuan",
    "Tinggi Badan (cm)": 85.5,
    "Berat Badan (kg)": 12.0
}
```

#### Contoh Success Response:

```json
{
    "Berat Badan": {
        "Final": "normal",
        "ML": "normal",
        "WHO": "normal",
        "Z-score": -0.15
    },
    "Tinggi Badan": {
        "Final": "normal",
        "ML": "normal",
        "WHO": "normal",
        "Z-score": -0.5
    }
}
```

---

## Berkontribusi

Kontribusi sangat dihargai! Jika Anda memiliki saran untuk meningkatkan proyek ini:

1. **Fork proyek ini**
2. **Buat branch fitur baru**
   `git checkout -b feature/NamaFitur`
3. **Commit perubahan**
   `git commit -m 'Menambahkan fitur keren'`
4. **Push ke branch Anda**
   `git push origin feature/NamaFitur`
5. **Buka Pull Request**

Atau buka issue dengan label `enhancement` jika ada ide/masukan.

---

## Lisensi

Didistribusikan di bawah Lisensi MIT. Lihat berkas `LICENSE.txt` untuk detail lebih lanjut.

---

## Kontak

**Bintang Budi Pangestu**
📧 Email: \[Email Anda]
🔗 LinkedIn: \[Profil LinkedIn Anda (opsional)]
📁 Tautan Proyek: [https://github.com/Nama-Pengguna-GitHub-Anda/Nama-Repositori-Anda](https://github.com/Nama-Pengguna-GitHub-Anda/Nama-Repositori-Anda)

---

## Ucapan Terima Kasih

* Dinas Pemberdayaan Perempuan dan Perlindungan Anak (DP3A) Provinsi Kalimantan Barat
* Program Studi Teknik Informatika, Universitas Tanjungpura
* Dosen Pembimbing: Dr. Arif Bijaksana Putra N, S.T., M.T.
