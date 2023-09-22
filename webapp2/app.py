import requests
from flask import Flask, render_template, request, jsonify
from custom.feature import FeatureExtraction
import joblib

app = Flask(__name__)

# Function to expand shortened URLs
def expand_shortened_url(url):
    try:
        response = requests.get(url)
        
        # Check for redirection in the response
        if response.history:
            print("Redirect chain:")
            for redirect in response.history:
                print(f"Status Code: {redirect.status_code}")
                print(f"Redirected to: {redirect.url}")
            return response.url  # Return the final URL after redirection
        else:
            return url  # No redirection detected, return the input URL
    except Exception as e:
        # Handle any exceptions that might occur during the request
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/remark', methods=['POST'])
def remark():
    return render_template('remark.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    # Check if the URL is shortened and expand if necessary
    expanded_url = expand_shortened_url(url)

    pt = FeatureExtraction(expanded_url)  # Use the expanded URL for feature extraction
    temp = pt.getFeaturesList()
    test_df = pt.createDF(temp)
    model = joblib.load(r'finalmodel.joblib')
    pred = model.predict(test_df)
    if pred[0] == 1:
        print("Safe")
        return render_template('safe.html')
    else:
        print("Phishing")
        return render_template('bad.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
