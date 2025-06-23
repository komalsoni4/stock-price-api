# 📈 Stock Price Prediction API

A Flask-based REST API that predicts stock prices using a trained Linear Regression model. Built as part of a Data Science Internship at CodeClause Studio.

---

## 🚀 Tech Stack
- Python
- Flask
- Scikit-learn
- Swagger (via Flasgger)

---

## 🔧 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/stock-price-api.git
cd stock-price-api
2. Install Dependencies


bash
pip install -r requirements.txt

3. Run the App
bash

python app.py
Open in browser:

Home: http://127.0.0.1:5000/

Swagger UI: http://127.0.0.1:5000/apidocs

📦 Project Files
File	Description
app.py	Flask backend with Swagger UI
stock_model.pkl	Trained Linear Regression model
scaler.pkl	StandardScaler used for predictions
README.md	Project overview
requirements.txt	Python dependencies

📮 Sample API Call (Swagger or Postman)


POST /predict
Content-Type: application/json

{
  "day": 2034
}
Response:


{
  "predicted_price": 213.42
}

✨ Author
Komal Kumari
B.Tech Final Year, IIT Roorkee
Stock Market Prediction | Flask + ML + Swagger

yaml

---

## ✅ 2. Steps to Upload to GitHub

1. **Initialize Git in your project folder (CMD inside project):**

```bash
