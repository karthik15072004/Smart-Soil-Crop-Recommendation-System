# 🌱 Smart Soil & Crop Recommendation System

An AI-powered agriculture application that combines **Deep Learning** and **Machine Learning** to identify soil type from an uploaded image and recommend the most suitable crops based on soil nutrients and environmental conditions.

The system also estimates crop yield, cultivation cost, expected profit, and farming risk to help farmers make informed decisions.

---

# 📖 Project Overview

Agriculture plays a vital role in food production, and selecting the right crop for a particular soil and climate is essential for maximizing yield and profitability.

This project uses:

- 📷 Deep Learning (MobileNetV2) to classify soil images.
- 🌾 Machine Learning (Random Forest) to recommend suitable crops.
- 💰 Profit estimation based on expected yield, cultivation cost, and market price.

The application is built using **Streamlit** for an interactive user interface.

---

# ✨ Features

## 📷 Soil Image Classification

- Upload soil image
- Automatic soil type detection
- Confidence score for prediction
- Supports:
  - Black Soil
  - Red Soil
  - Clay Soil
  - Alluvial Soil

---

## 🌿 Crop Recommendation

Uses soil nutrients and weather conditions:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Rainfall

to recommend the most suitable crops.

---

## 🌾 Top Crop Suggestions

Displays

- Top 5 recommended crops
- Prediction confidence
- Crop ranking

---

## 📈 Yield Prediction

Estimates

- Expected Yield (tons/hectare)

---

## 💰 Profit Analysis

Calculates

- Estimated Cultivation Cost
- Expected Revenue
- Estimated Profit

---

## ⚠️ Risk Assessment

Classifies farming risk into

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

---

## 🎨 Interactive Dashboard

Built using Streamlit with

- Image Upload
- Sliders
- Input Fields
- Interactive Results

---

# 🧠 AI Models Used

## Deep Learning

### MobileNetV2

Used for

- Soil Image Classification

Transfer Learning is used by freezing initial layers and fine-tuning the final layers for better accuracy.

---

## Machine Learning

### Random Forest Classifier

Used for

- Crop Recommendation

Based on

- Soil Nutrients
- Temperature
- Humidity
- Rainfall

---

# 🛠️ Technology Stack

## Programming Language

- Python

## Frontend

- Streamlit

## Deep Learning

- TensorFlow
- Keras
- MobileNetV2

## Machine Learning

- Scikit-learn
- Random Forest

## Data Processing

- Pandas
- NumPy

## Image Processing

- Pillow

---

# 📂 Project Structure

```
crop-recommendation/
│
├── Dataset/
│   ├── Train/
│   ├── Test/
│
├── Crop_recommendation.csv
├── soil_model.h5
├── class_indices.json
│
├── code.py
├── requirements.txt
└── README.md
```

---

# 📊 Input Parameters

## Soil Nutrients

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)

## Weather Parameters

- Temperature
- Humidity
- Rainfall

## Image Input

- Soil Image (.jpg/.png)

---

# 🌾 Recommended Crops

The model recommends crops such as

- Rice
- Wheat
- Cotton
- Maize
- Mango
- Banana
- Coffee
- Chickpea
- Pomegranate
- Lentil
- Kidney Beans
- Grapes
- Apple

---

# 📈 Output

The application provides

- Soil Type
- Prediction Confidence
- Top Crop Recommendations
- Estimated Yield
- Estimated Cost
- Estimated Profit
- Farming Risk Level

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/karthik15072004/crop-recommendation.git
```

---

## Navigate to Project

```bash
cd crop-recommendation
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run code.py
```

---

# 📊 Dataset

The project uses

### Soil Image Dataset

Contains images of

- Black Soil
- Red Soil
- Clay Soil
- Alluvial Soil

---

### Crop Recommendation Dataset

Features

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- Rainfall
- Crop Label

---

# 🧠 Workflow

```
Soil Image
      │
      ▼
MobileNetV2
      │
      ▼
Soil Type Detection
      │
      ▼
User Inputs
(N, P, K, Temperature,
Humidity, Rainfall)
      │
      ▼
Random Forest
      │
      ▼
Top Crop Recommendations
      │
      ▼
Yield Prediction
      │
      ▼
Profit Estimation
      │
      ▼
Risk Analysis
```

---

# 📷 Application Features

- 🖼 Upload Soil Image
- 🌱 Soil Type Prediction
- 🌾 Crop Recommendation
- 📈 Yield Estimation
- 💰 Profit Calculation
- ⚠️ Risk Assessment

---

# 🎯 Future Enhancements

- Real-time Weather API Integration
- Soil Moisture Sensor Support
- Fertilizer Recommendation System
- Disease Detection
- Drone Image Analysis
- GIS Mapping
- Mobile Application
- Cloud Deployment

---

# 👨‍💻 Author

**Karthik Kumar**

M.Tech in Data Science  
Vellore Institute of Technology (VIT), Vellore

GitHub: https://github.com/karthik15072004

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---

# 📜 License

This project is developed for educational and research purposes.
