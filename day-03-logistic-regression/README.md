# 📘 Day 03 — Logistic Regression

## 📖 Overview

Logistic Regression is a supervised machine learning algorithm used for classification problems. It predicts the probability that an input belongs to a particular category.

Unlike Linear Regression, Logistic Regression outputs values between 0 and 1 using the sigmoid function.

---

## 🧠 Sigmoid Function

\sigma(z)=\frac{1}{1+e^{-z}}

The sigmoid function converts input values into probabilities.

---

## 🎯 Objective

Classify observations into categories such as:

* Spam / Not Spam
* Pass / Fail
* Fraud / Non-Fraud

---

## ⚙️ How Logistic Regression Works

1. Takes weighted sum of inputs
2. Applies sigmoid activation function
3. Produces probability output
4. Assigns class label based on threshold

---

## 📊 Decision Boundary

P(y=1|x)=\frac{1}{1+e^{-(b_0+b_1x)}}

If probability > 0.5 → Class 1
Else → Class 0

---

## 🌍 Applications

* Email spam detection
* Disease prediction
* Fraud detection
* Customer churn prediction

---

## 📌 Key Takeaways

* Used for classification tasks
* Outputs probabilities
* Uses sigmoid activation function
* Simple and interpretable algorithm

---

## 📌 Next Step

➡️ Day 04 — Data Preprocessing
