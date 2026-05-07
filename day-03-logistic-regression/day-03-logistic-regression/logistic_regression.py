# Day 03: Logistic Regression Example

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Sample Data
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

# Model
model = LogisticRegression()

# Train Model
model.fit(X, y)

# Predictions
predictions = model.predict(X)

# Output
print("Predicted Classes:", predictions)

# Visualization
plt.scatter(X, y)
plt.xlabel("Input Feature")
plt.ylabel("Class")
plt.title("Logistic Regression Classification")
plt.show()
