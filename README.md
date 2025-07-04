# Human-Context-Behavior-Analysis-using-Sensor-Data

> **Description**:  
This project analyzes human context and behavior using sensor data and machine learning algorithms. We use the ExtraSensory dataset and apply Random Forest models to identify activities and predict user mood with high accuracy.  

---

## 📌 Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Features and Labels](#features-and-labels)
- [Results](#results)
- [Future Work](#future-work)
---

## 📖 Introduction

Human behavior is highly complex and variable. Automatically identifying a person's context—such as their location, actions, and social setting—has broad applications in health, personalized recommendations, and behavioral studies.

Recognizing context in the wild is challenging:
- Activities can overlap (e.g., eating while watching TV).
- Sensor data can be noisy or incomplete.
- Users engage in activities across diverse environments.

Our objective is to extract meaningful behavioral context from raw smartphone and wearable sensor data, using machine learning models that generalize well to real-world settings.

---

## 📊 Dataset

We use the **ExtraSensory Dataset**, which includes data from 60 participants over multiple days.  
**Key details:**
- Thousands of examples per user, sampled roughly once per minute.
- Data includes:
  - High-frequency sensors: accelerometer, gyroscope, magnetometer, audio.
  - Low-frequency contextual sensors: location, phone state, environmental sensors.
  - Self-reported activity and mood labels.

**Statistics:**
- 225 sensor features grouped into 11 sensor groups.
- 51 activity labels categorized into 5 domains: Posture, Location, Activity, Phone Usage, Socializing.
- Mood labels to enable mood prediction tasks.

---

## ⚙️ Methodology

Our workflow consists of the following steps:

1. **Data Integration**: Combining CSV data across users into a single dataset.
2. **Exploratory Data Analysis**: Investigating distribution of features and labels.
3. **Feature Importance Calculation**:
   - Used Random Forest Regressor to estimate sensor feature importance for each activity label.
4. **Feature Selection**:
   - For each activity label, identified top 3 sensor feature groups.
5. **Classification**:
   - Built Random Forest Classifier using selected features to predict activity labels.
6. **Mood Prediction**:
   - Linked predicted activity sequences to mood labels using sentiment-based mappings and an "emotional wheel" visualization.

**Proposed System Diagram:**
Sensor Data ➜ Preprocessing ➜ Random Forest Feature Importance ➜ Feature Selection ➜ Classification ➜ Mood Prediction


---

## 📋 Features and Labels

**Sensor Feature Groups (examples):**
- Accelerometer
- Gyroscope
- Magnetometer
- Audio (MFCCs)
- Location
- Watch Accelerometer
- Phone State

**Activity Label Categories:**
- Posture: SITTING, LYING_DOWN, SLEEPING, etc.
- Location: LOC_home, IN_A_CAR, AT_SCHOOL, etc.
- Activity: COOKING, CLEANING, SHOPPING, etc.
- Phone Usage: PHONE_ON_TABLE, PHONE_IN_HAND, etc.
- Socializing: WITH_FRIENDS, AT_A_PARTY, etc.

For each label, top sensor groups were identified (e.g., for LYING_DOWN: ['PS', 'Aud', 'AP']).

---

## ✅ Results

We evaluated model performance on a large combined dataset:

- **Random Forest Classifier Accuracy**:
  - Training accuracy: ~99.9%
  - Test accuracy: ~94.5% (average across activities)

- **Key Insights**:
  - Random Forest consistently outperformed Logistic Regression.
  - Top 3 sensor groups per label enabled robust prediction while reducing dimensionality.
  - Emotional Wheel visualization offered interpretable mood prediction based on activity inputs.

---

## 🚀 Future Work

- Improve generalization to new users with few examples.
- Incorporate temporal models (e.g., RNNs, Transformers) to capture activity transitions.
- Expand mood prediction models to consider richer psychological states.
- Deploy as a real-time mobile application.
