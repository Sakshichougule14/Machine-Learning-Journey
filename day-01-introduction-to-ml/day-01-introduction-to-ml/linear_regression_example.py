# Day 01: Linear Regression Demonstration

import numpy as np
from sklearn.linear_model import LinearRegression

def train_model():
    """
    Trains a simple Linear Regression model on sample data.
    """
    # Feature (Independent Variable)
    X = np.array([[1], [2], [3], [4], [5]])
    
    # Target (Dependent Variable)
    y = np.array([100, 200, 300, 400, 500])
    
    model = LinearRegression()
    model.fit(X, y)
    
    return model

def make_prediction(model, value):
    """
    Predicts output for a given input value.
    """
    prediction = model.predict([[value]])
    return prediction[0]

if __name__ == "__main__":
    model = train_model()
    result = make_prediction(model, 6)
    
    print(f"Predicted value for input 6: {result}")
