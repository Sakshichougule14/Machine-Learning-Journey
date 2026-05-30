# 📘 Day 04 — Data Preprocessing

## 📖 Overview

Data Preprocessing is the process of cleaning and transforming raw data into a format suitable for machine learning models.

Since real-world data is often incomplete, inconsistent, or noisy, preprocessing is a crucial step before model training.

---

## 🎯 Why Data Preprocessing is Important

Machine learning models perform better when trained on clean and well-structured data.

Common issues in datasets include:

* Missing values
* Duplicate records
* Outliers
* Inconsistent formats
* Categorical variables

---

## ⚙️ Common Data Preprocessing Steps

### 1. Handling Missing Values

Missing values can be treated by:

* Removing rows or columns
* Replacing with Mean
* Replacing with Median
* Replacing with Mode

---

### 2. Encoding Categorical Variables

Machine learning algorithms require numerical input.

Example:

* Male → 1
* Female → 0

Popular techniques:

* Label Encoding
* One-Hot Encoding

---

### 3. Feature Scaling

Features may have different ranges.

Example:

* Age: 18–60
* Salary: 20,000–100,000

Scaling methods:

* Standardization
* Normalization

---

### 4. Removing Duplicate Records

Duplicate entries can introduce bias and affect model performance.

---

### 5. Outlier Detection

Outliers are extreme values that differ significantly from the rest of the data.

Example:

10, 12, 15, 18, 250

Here, 250 is an outlier.

---

## 🌍 Applications

* Customer Analytics
* Fraud Detection
* Healthcare Analytics
* Financial Forecasting

---

## 📌 Key Takeaways

* Data preprocessing improves data quality.
* Clean data leads to better model performance.
* Missing values, categorical variables, and scaling must be handled carefully.
* Data preprocessing is an essential step in every machine learning project.

---

## 📌 Next Step

➡️ Day 05 — Train-Test Split & Model Evaluation
