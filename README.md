
# 🏡 House Price Prediction API (FastAPI + ML)

## 📌 Overview

This project is a **Machine Learning-powered API** built with **FastAPI**.
It predicts **house prices** based on input features like number of rooms, area, and age of the house.

The API comes with an **interactive Swagger UI** at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), where you can test the endpoints using the **“Try it out”** button.

---

## 🎯 Features

* ✅ FastAPI backend
* ✅ Machine Learning model (scikit-learn)
* ✅ REST API endpoints
* ✅ Interactive documentation with Swagger UI
* ✅ Easy deployment ready

---

## 🛠️ Requirements

* Python **3.9+**
* pip (Python package manager)
* Virtual environment (recommended)

---

## 📂 Project Structure

```
App/
├── main.py              # FastAPI application
├── model.pkl            # Trained ML model (pickle file)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/house-price-api.git
cd house-price-api
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate virtual environment

* **Windows (PowerShell)**

  ```bash
  .venv\Scripts\activate
  ```
* **Linux/Mac**

  ```bash
  source .venv/bin/activate
  ```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the FastAPI server

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

Once the server is running, open in your browser:

* **Swagger UI (Interactive Docs)** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc (Alternative Docs)** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Example Request & Response

### 🔹 POST `/predict`

**Input JSON:**

```json
{
  "rooms": 3,
  "area": 1200,
  "age": 10
}
```

**Output JSON:**

```json
{
  "predicted_price": 250000.0
}
```

---

## 🧪 Testing with cURL / Postman

### Using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d "{\"rooms\":3, \"area\":1200, \"age\":10}"
```

### Using Postman:

1. Open Postman → New Request
2. Select **POST**
3. Enter `http://127.0.0.1:8000/predict`
4. Select **Body → raw → JSON**
5. Paste input JSON → Send

---

## 📦 Dependencies

* fastapi
* uvicorn
* scikit-learn
* numpy
* pydantic

(Already listed in `requirements.txt`)

---

## 📜 License

This project is licensed under the MIT License.

---

⚡ Now when someone opens your repo, they’ll know exactly how to run and test it.

👉 Do you want me to also **generate the `requirements.txt` file** for your project so your README.md instructions will work smoothly?
