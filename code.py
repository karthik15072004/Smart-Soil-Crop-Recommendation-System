import streamlit as st
import numpy as np
import os
import json
import pandas as pd
from PIL import Image

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping

from sklearn.ensemble import RandomForestClassifier


dataset_path = r"C:\Users\karth\Downloads\archive (4)\Dataset\Train"
crop_dataset_path = "Crop_recommendation.csv"


if not os.path.exists(dataset_path):
    st.error("❌ Image dataset not found!")
    st.stop()

if not os.path.exists(crop_dataset_path):
    st.error("❌ Crop dataset CSV not found!")
    st.stop()


@st.cache_resource
def get_image_model():

    if os.path.exists("soil_model.h5") and os.path.exists("class_indices.json"):
        model = load_model("soil_model.h5")
        with open("class_indices.json", "r") as f:
            class_indices = json.load(f)
        return model, class_indices

    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        rotation_range=30,
        zoom_range=0.2,
        horizontal_flip=True
    )

    train_data = datagen.flow_from_directory(
        dataset_path,
        target_size=(224,224),
        batch_size=32,
        class_mode='categorical',
        subset='training'
    )

    val_data = datagen.flow_from_directory(
        dataset_path,
        target_size=(224,224),
        batch_size=32,
        class_mode='categorical',
        subset='validation'
    )

    with open("class_indices.json", "w") as f:
        json.dump(train_data.class_indices, f)

    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3))

    for layer in base_model.layers[:-50]:
        layer.trainable = False

    x = base_model.output
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    output = layers.Dense(train_data.num_classes, activation='softmax')(x)

    model = models.Model(inputs=base_model.input, outputs=output)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

    model.fit(train_data, epochs=20, validation_data=val_data, callbacks=[early_stop])

    model.save("soil_model.h5")

    return model, train_data.class_indices



@st.cache_resource
def get_crop_model():
    df = pd.read_csv(crop_dataset_path)

    df = df.sample(frac=1, random_state=42)  # shuffle

    X = df[['N','P','K','temperature','humidity','rainfall']]
    y = df['label']

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X, y)

    return model



image_model, class_indices = get_image_model()
crop_model = get_crop_model()

class_names = list(class_indices.keys())


yield_data = {
    "rice": 3, "wheat": 3, "cotton": 2.5, "maize": 3,
    "mango": 8, "banana": 30, "coffee": 2,
    "chickpea": 1.5, "pomegranate": 10, "lentil": 1.2,
    "kidneybeans": 2, "grapes": 12, "apple": 10
}

cost_data = {
    "rice": 35000, "wheat": 25000, "cotton": 30000, "maize": 25000,
    "mango": 40000, "banana": 50000, "coffee": 35000,
    "chickpea": 20000, "pomegranate": 45000, "lentil": 18000,
    "kidneybeans": 22000, "grapes": 60000, "apple": 55000
}

price_data = {
    "rice": 22000, "wheat": 20000, "cotton": 25000, "maize": 20000,
    "mango": 30000, "banana": 10000, "coffee": 40000,
    "chickpea": 50000, "pomegranate": 60000, "lentil": 45000,
    "kidneybeans": 40000, "grapes": 70000, "apple": 65000
}

def calculate_profit(crop):
    crop = crop.lower()

    y = yield_data.get(crop, np.random.uniform(1.5, 5))
    cost = cost_data.get(crop, 25000)
    price = price_data.get(crop, 25000)

    revenue = y * price
    profit = revenue - cost

    if profit > 50000:
        risk = "Low"
    elif profit > 20000:
        risk = "Medium"
    else:
        risk = "High"

    return round(y,2), cost, round(profit,2), risk



st.title("🌱 Smart Soil & Crop Recommendation System")

image = st.file_uploader("📸 Upload Soil Image", type=["jpg","png"])

st.subheader("🌿 Soil Nutrients")
N = st.number_input("Nitrogen (N)", 0, 140, 50)
P = st.number_input("Phosphorus (P)", 0, 140, 50)
K = st.number_input("Potassium (K)", 0, 140, 50)

temperature = st.slider("Temperature (°C)", 10, 45, 25)
humidity = st.slider("Humidity (%)", 10, 100, 60)
rainfall = st.slider("Rainfall (mm)", 0, 300, 100)

manual_soil = st.selectbox(
    "Override Soil Type",
    ["Auto", "Black", "Red", "Clay", "Alluvial"]
)


if image:
    st.image(image)

    img = Image.open(image).convert("RGB").resize((224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)

    pred = image_model.predict(img)

    soil_type = class_names[np.argmax(pred)]
    soil_type_clean = soil_type.lower().replace("soil","").strip().capitalize()

    confidence = np.max(pred)*100

    soil_type_final = manual_soil if manual_soil != "Auto" else soil_type_clean

    st.success(f"🧠 Soil Type: {soil_type_final} ({confidence:.2f}%)")

    
    input_data = [[N, P, K, temperature, humidity, rainfall]]

    probs = crop_model.predict_proba(input_data)[0]
    classes = crop_model.classes_

    top_indices = np.argsort(probs)[-5:][::-1]

    st.subheader("🌾 Top Crop Recommendations")

    for i in top_indices:
        crop_name = classes[i]
        confidence_crop = probs[i] * 100

        if confidence_crop < 10:
            continue

        st.markdown(f"## 🌾 {crop_name.capitalize()} ({confidence_crop:.2f}%)")

        y, cost, profit, risk = calculate_profit(crop_name)

        st.write(f"📈 Yield: {y} tons/hectare")
        st.write(f"💰 Cost: ₹{cost}")
        st.write(f"💵 Profit: ₹{profit}")
        st.write(f"⚠️ Risk: {risk}")
        st.write("---")