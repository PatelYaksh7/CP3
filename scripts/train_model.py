import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Example dataset
data = {
    'ph': [6.5, 7.0, 5.5, 6.0, 7.5],
    'moisture': [30, 45, 20, 35, 40],
    'nutrients': [7, 8, 6, 7, 8],
    'soil_type': ['Loamy', 'Clay', 'Sandy', 'Loamy', 'Clay'],
    'last_crop': ['Tomato', 'Lettuce', 'Wheat', 'Corn', 'Barley'],
    'weather_type': ['Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Rainy'],
    'next_crop': ['Corn', 'Wheat', 'Barley', 'Tomato', 'Lettuce']
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['ph', 'moisture', 'nutrients', 'soil_type', 'last_crop', 'weather_type']]
y = df['next_crop']

# Convert categorical variables to numeric
X = pd.get_dummies(X)

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
model_path = os.path.join(os.path.dirname(__file__), 'soil_quality_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved to {model_path}")
