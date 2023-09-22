from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import Flask-CORS
from custom.feature import FeatureExtraction
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

# Load the machine learning model when the server starts
model = joblib.load('finalmodel.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Assuming the extension sends JSON data
        url = data['url']

        # Perform feature extraction and prepare data for prediction
        pt = FeatureExtraction(url)
        temp = pt.getFeaturesList()
        test_df = pt.createDF(temp)

        # Use the loaded model to make predictions
        pred = model.predict(test_df)

        # Customize the response format
        response = {
            'url': url,
            'prediction': 'Safe' if pred[0] == 1 else 'Phishing'
        }

        return jsonify(response)  # Return JSON response
    except Exception as e:
        return jsonify({'error': str(e)})  # Return JSON error response

@app.route('/')
def home():
    return render_template('popup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
