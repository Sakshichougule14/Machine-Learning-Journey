# 📘 Day 08 — Random Forest Classification

## 📖 Overview

Random Forest is a supervised machine learning algorithm used for both classification and regression tasks.

It is an ensemble learning technique that combines multiple Decision Trees to improve prediction accuracy and reduce overfitting.

---

## 🎯 Objective

Make more accurate and robust predictions by combining the results of multiple Decision Trees.

Example:

Suppose 5 Decision Trees predict:

* Tree 1 → Yes
* Tree 2 → Yes
* Tree 3 → No
* Tree 4 → Yes
* Tree 5 → Yes

Final Prediction:

* Yes (Majority Vote)

---

## ⚙️ How Random Forest Works

1. Create multiple random samples from the dataset
2. Build a Decision Tree for each sample
3. Make predictions using all trees
4. Combine predictions using majority voting (classification)
5. Produce the final output

---

## 🌲 Key Concepts

### Bootstrap Sampling

Random subsets of data are selected with replacement to train each tree.

---

### Ensemble Learning

Combining multiple models to improve performance.

---

### Majority Voting

For classification tasks, the class receiving the highest votes becomes the final prediction.

---

## 📊 Why Random Forest is Better than Decision Trees

* Reduces overfitting
* Improves accuracy
* Handles large datasets efficiently
* More robust to noise

---

## 🌍 Applications

* Fraud Detection
* Medical Diagnosis
* Customer Churn Prediction
* Stock Market Analysis
* Recommendation Systems

---

## ✅ Advantages

* High accuracy
* Reduces overfitting
* Handles missing values well
* Works with large datasets

---

## ❌ Limitations

* More computationally expensive
* Less interpretable than a single Decision Tree
* Requires more memory

---

## 📌 Key Takeaways

* Random Forest combines multiple Decision Trees.
* Uses ensemble learning to improve predictions.
* Reduces overfitting compared to Decision Trees.
* One of the most widely used machine learning algorithms.

---

## 📌 Next Step

➡️ Day 09 — Support Vector Machine (SVM)
