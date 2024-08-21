import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

csv_file_path = os.path.join(os.path.dirname(__file__), 'crops_data.csv')

df = pd.read_csv(csv_file_path)

X = df[['ph', 'moisture', 'nutrients', 'soil_type', 'last_crop', 'weather_type']]
y = df['next_crop']

X = pd.get_dummies(X)

model = DecisionTreeClassifier()
model.fit(X, y)

model_path = os.path.join(os.path.dirname(__file__), 'soil_quality_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved to {model_path}")
