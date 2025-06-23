from flask import Flask, request, jsonify
from flasgger import Swagger
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('stock_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    return "📈 Welcome to the Stock Price Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict stock price for a given day index
    ---
    parameters:
      - name: day
        in: body
        type: integer
        required: true
        example: {"day": 2034}
    responses:
      200:
        description: Predicted stock price
        examples:
          {"predicted_price": 213.42}
    """
    data = request.get_json()
    day = int(data['day'])
    day_scaled = scaler.transform([[day]])
    prediction = model.predict(day_scaled)[0]
    return jsonify({'predicted_price': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)
