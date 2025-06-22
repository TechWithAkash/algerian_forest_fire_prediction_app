
<h1 align="center">
  🔥 Algerian Forest Fire Prediction App
</h1>

<p align="center">
  <img src="https://img.shields.io/github/license/TechWithAkash/algerian_forest_fire_prediction_app?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/TechWithAkash/algerian_forest_fire_prediction_app?style=for-the-badge"/>
  <img src="https://img.shields.io/github/forks/TechWithAkash/algerian_forest_fire_prediction_app?style=for-the-badge"/>
</p>

<p align="center">
  A machine learning-powered web application to predict the Fire Weather Index (FWI) using Algerian forest climate data. Built with Flask, Ridge Regression, and a stunning frontend interface. Ideal for environmental agencies, researchers, and fire prevention systems.
</p>

---

## 🚀 Demo

https://github.com/TechWithAkash/algerian_forest_fire_prediction_app/assets/0000000/demo.mp4 <!-- Replace with actual demo path or YouTube URL -->

> 🎥 **[Watch Full Demo](https://github.com/TechWithAkash/algerian_forest_fire_prediction_app/assets/0000000/demo.mp4)**

---

## 🧠 Problem Statement

Wildfires in Algeria have caused significant environmental and economic damage. This app predicts the **Fire Weather Index (FWI)**, a critical metric used to assess the potential for wildfire ignition and spread, using meteorological inputs.

---

## ✨ Features

- 🔬 Ridge Regression model trained on real Algerian wildfire data
- 📊 User-friendly form for entering weather parameters
- 🧠 Scaled prediction using pre-trained model and scaler
- 💻 Clean, modern UI built with Tailwind CSS & Poppins font
- 📱 Fully responsive and mobile-friendly design
- 💬 Prediction result displayed in a modern popup modal

---

## 📸 UI Preview

| Landing Page | Prediction Modal |
|--------------|------------------|
| ![Landing](https://github.com/TechWithAkash/algerian_forest_fire_prediction_app/assets/0000000/landing.png) | ![Modal](https://github.com/TechWithAkash/algerian_forest_fire_prediction_app/assets/0000000/modal.png) |

---

## 📂 Project Structure

```bash
├── app.py
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
├── templates/
│   ├── index.html
│   ├── predict.html
│   ├── prediction.html
│   └── footer.html
└── static/ (optional for logos, styling etc.)
````

---

## 📦 Tech Stack

* 💻 **Frontend**: HTML, Tailwind CSS, JavaScript
* 🧠 **Backend**: Python, Flask
* 📈 **ML Model**: Ridge Regression (scikit-learn)
* 📊 **Dataset**: Algerian Forest Fire Dataset
* 🧪 **Tools**: VS Code, Git, GitHub

---

## 🧪 Inputs Used for Prediction

* 🌡️ Temperature
* 💧 Relative Humidity (RH)
* 🌬️ Wind Speed (WS)
* ☔ Rainfall
* 🔥 FFMC, DMC, ISI
* 🗺️ Classes (Fire/No Fire)
* 🌍 Region (Bejaia/Sidi-Bel Abbes)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/TechWithAkash/algerian_forest_fire_prediction_app.git
cd algerian_forest_fire_prediction_app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

---

## 📈 Sample Prediction

```plaintext
Input:
Temperature: 35.5
RH: 45
WS: 18
Rain: 0.0
FFMC: 92.0
DMC: 120.0
ISI: 10.5
Classes: 1
Region: 1

Output:
🔥 The Fire Weather Index is: 32.54
```

---

## 🙌 Author

**Akash Vishwakarma**
[GitHub](https://github.com/TechWithAkash) • [LinkedIn](https://www.linkedin.com/in/akash-vishwakarma-creator/)

---

## 📃 License

This project is licensed under the MIT License.

---

## ⭐ Show Your Support

If you found this project helpful:

🌟 Star the repo
🍴 Fork it
🐛 Raise issues or contribute

> *Your star keeps the fire burning! 🔥*

```

