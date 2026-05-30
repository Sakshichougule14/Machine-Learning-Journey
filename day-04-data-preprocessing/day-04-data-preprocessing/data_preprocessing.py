# Day 04: Data Preprocessing

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Sample Dataset
data = {
    'Age': [20, 25, None, 30, 35],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handle Missing Values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Encode Categorical Data
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])

# Feature Scaling
scaler = StandardScaler()
df[['Age']] = scaler.fit_transform(df[['Age']])

print("\nProcessed Data:")
print(df)
