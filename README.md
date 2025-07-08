# Child Nutritional Status & Stunting Detection API

## About The Project

This repository contains the source code for a REST API developed to classify child nutritional status and detect stunting based on anthropometric data. The project utilizes the Support Vector Machine (SVM) algorithm and is designed to be integrated into a client application, such as the "Gerakan Sayang Anak" app by the DP3A (Agency for Women's Empowerment and Child Protection) of West Kalimantan.

The primary goal is to provide a reliable, real-time classification service that can be used by health workers and parents to monitor child growth, enabling early detection and intervention for nutritional issues like stunting.

## Key Features

* **Dual Classification Models**: Implements two separate SVM models:

  * **Stunting Detection**: Classifies stunting status based on Height-for-Age (HAZ).
  * **Nutritional Status Classification**: Classifies nutritional status based on Weight-for-Age (WAZ).

* **WHO Standards Integration**: Includes a Z-score calculator based on World Health Organization (WHO) growth standards, providing a medical reference for each classification.

* **Dual-Output Response**: The API returns both the Machine Learning (ML) model's prediction and the classification based on WHO's Z-score standards, offering a comprehensive result for validation.

* **Ready for Integration**: Developed as a REST API using Flask, making it easy to integrate with various client applications (e.g., mobile apps, web dashboards).

* **Deployed on Cloud**: The service is containerized using Docker and deployed on Google Cloud Run for scalability and high availability.

## Built With

This project was built using the following technologies:

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Docker
* Google Cloud Run
* Google Container Registry

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.9+
* Docker

### Installation

1. Clone the repo

```bash
git clone https://github.com/BintangBudi/Deteksi-Stunting.git
```

2. Navigate to the project directory

```bash
cd your_repository
```

3. Install Python packages

```bash
pip install -r requirements.txt
```

4. (Optional) To run with Docker, build the image:

```bash
docker build -t stunting-api .
```

## Usage

The API provides a single endpoint (`/predict`) that accepts a POST request with a JSON payload containing a child's anthropometric data (age in months, gender, height in cm, and weight in kg).

### How It Works

1. The API validates the incoming data.
2. It calculates the Z-score and determines the WHO classification for both Height-for-Age and Weight-for-Age.
3. It preprocesses the input data and feeds it to the respective trained SVM models to get the ML predictions.
4. It returns a JSON response containing a consolidated result, including the Z-score, WHO classification, ML prediction, and a final classification for both height and weight status.

### API Endpoint

**POST** `/predict`

#### Request Body:

```json
{
    "Umur (bulan)": 24,
    "Jenis Kelamin": "perempuan",
    "Tinggi Badan (cm)": 85.5,
    "Berat Badan (kg)": 12.0
}
```

#### Success Response:

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

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
