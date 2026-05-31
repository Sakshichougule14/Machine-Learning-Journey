# 📘 Day 05 — Train-Test Split & Model Evaluation

## 📖 Overview

Before evaluating a machine learning model, it is important to test its performance on unseen data. This is achieved by splitting the dataset into training and testing sets.

Model Evaluation helps measure how well a model performs and whether it can generalize to new data.

---

## 🎯 Train-Test Split

A dataset is typically divided into:

* Training Set – Used to train the model
* Testing Set – Used to evaluate the model

Common split ratios:

* 80% Training – 20% Testing
* 70% Training – 30% Testing

Example:

Dataset Size = 1000 Records

* Training Data = 800 Records
* Testing Data = 200 Records

---

## ⚙️ Why Train-Test Split is Important

Without a test set, we cannot determine how well the model performs on new data.

Benefits:

* Prevents overfitting
* Measures model performance
* Improves model reliability

---

## 📊 Model Evaluation Metrics

### 1. Accuracy

Accuracy measures the proportion of correctly classified observations.

Accuracy = (Correct Predictions) / (Total Predictions)

Higher accuracy indicates better performance.

---

### 2. Confusion Matrix

A confusion matrix summarizes classification results.

Components:

* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

It helps understand model strengths and weaknesses.

---

### 3. Precision

Precision measures how many predicted positive cases are actually positive.

Precision = TP / (TP + FP)

---

### 4. Recall

Recall measures how many actual positive cases are correctly identified.

Recall = TP / (TP + FN)

---

### 5. F1-Score

F1-Score is the harmonic mean of Precision and Recall.

It is useful when classes are imbalanced.

---

## ⚠️ Overfitting vs Underfitting

### Overfitting

* Model performs well on training data
* Performs poorly on testing data
* Learns noise instead of patterns

### Underfitting

* Model performs poorly on both training and testing data
* Fails to capture important patterns

---

## 🌍 Applications

* Fraud Detection
* Medical Diagnosis
* Customer Churn Prediction
* Email Spam Detection

---

## 📌 Key Takeaways

* Train-Test Split helps evaluate model performance on unseen data.
* Accuracy, Precision, Recall, and F1-Score are important evaluation metrics.
* Overfitting and Underfitting should be avoided.
* Model evaluation is a critical step in machine learning workflows.

---

## 📌 Next Step

➡️ Day 06 — K-Nearest Neighbors (KNN)
