from flask import Flask, request, jsonify
import pandas as pd
import pickle
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), 'soil_quality_model.pkl')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("No input data provided")

        ph = data.get('ph')
        moisture = data.get('moisture')
        nutrients = data.get('nutrients')
        soil_type = data.get('soil_type')
        last_crop = data.get('last_crop')
        weather_type = data.get('weather_type')

        if None in [ph, moisture, nutrients, soil_type, last_crop, weather_type]:
            raise ValueError("Missing one or more required fields")

        input_data = pd.DataFrame([{
            'ph': ph,
            'moisture': moisture,
            'nutrients': nutrients,
            'soil_type': soil_type,
            'last_crop': last_crop,
            'weather_type': weather_type
        }])

        input_data = pd.get_dummies(input_data)

        input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

        prediction = model.predict(input_data)[0]

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
