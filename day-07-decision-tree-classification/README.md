# 📘 Day 07 — Decision Tree Classification

## 📖 Overview

Decision Tree is a supervised machine learning algorithm used for both classification and regression tasks.

It works by splitting data into smaller subsets based on feature values, creating a tree-like structure of decisions and outcomes.

---

## 🎯 Objective

Classify or predict an outcome by learning a series of decision rules from the data.

Example:

For loan approval:

* Income > ₹50,000 → Approved
* Income ≤ ₹50,000 → Not Approved

The model creates decision rules automatically from the training data.

---

## ⚙️ How Decision Tree Works

1. Select the best feature for splitting the data
2. Divide the dataset into subsets
3. Repeat the process for each subset
4. Stop when a leaf node is reached
5. Predict the outcome based on the leaf node

---

## 🌳 Components of a Decision Tree

### Root Node

The topmost node representing the entire dataset.

### Decision Node

A node where the data is split based on a condition.

### Leaf Node

The final node that provides the prediction or classification.

---

## 📊 Splitting Criteria

### Gini Impurity

Measures the impurity of a node.

* Lower Gini → Better split
* Higher Gini → Poor split

---

### Entropy

Measures the randomness or disorder in the dataset.

* Lower Entropy → More homogeneous data
* Higher Entropy → More mixed data

---

## 🌍 Applications

* Credit Risk Analysis
* Customer Churn Prediction
* Medical Diagnosis
* Fraud Detection

---

## ✅ Advantages

* Easy to understand and interpret
* Handles both numerical and categorical data
* Requires little data preprocessing
* Visual representation of decisions

---

## ❌ Limitations

* Can overfit the training data
* Sensitive to small changes in data
* Complex trees may become difficult to interpret

---

## 📌 Key Takeaways

* Decision Trees use a tree-like structure for decision making.
* They split data based on the most informative features.
* Gini Impurity and Entropy are common splitting criteria.
* Decision Trees are simple, interpretable, and widely used.

---

## 📌 Next Step

➡️ Day 08 — Random Forest Classification
