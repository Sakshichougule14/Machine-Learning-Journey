# 📘 Day 06 — K-Nearest Neighbors (KNN)

## 📖 Overview

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for both classification and regression tasks.

It predicts the class of a new data point by looking at the 'K' nearest data points in the training dataset.

---

## 🎯 Objective

Classify a new observation based on the majority class of its nearest neighbors.

Example:

If K = 3 and among the 3 nearest neighbors:

* 2 belong to Class A
* 1 belongs to Class B

Then the new observation is classified as Class A.

---

## ⚙️ How KNN Works

1. Choose the value of K
2. Calculate the distance between the new point and all training points
3. Select the K nearest neighbors
4. Assign the majority class

---

## 📏 Distance Metrics

### Euclidean Distance

Distance between two points:

d = √[(x₂ - x₁)² + (y₂ - y₁)²]

---

### Manhattan Distance

d = |x₂ - x₁| + |y₂ - y₁|

---

## 📊 Choosing the Value of K

* Small K → Sensitive to noise
* Large K → More stable but may underfit

Common values:

* K = 3
* K = 5
* K = 7

---

## 🌍 Applications

* Recommendation Systems
* Medical Diagnosis
* Pattern Recognition
* Credit Risk Analysis

---

## ✅ Advantages

* Easy to understand
* No training phase
* Effective for small datasets

---

## ❌ Limitations

* Computationally expensive for large datasets
* Sensitive to irrelevant features
* Requires feature scaling

---

## 📌 Key Takeaways

* KNN is a distance-based algorithm.
* It classifies data using nearby observations.
* Choosing an appropriate K value is important.
* Feature scaling improves KNN performance.

---

## 📌 Next Step

➡️ Day 07 — Decision Tree Classification
