# 🏦 Customer Churn Prediction using ANN

A Machine Learning web application built with **TensorFlow**, **Scikit-learn**, and **Streamlit** to predict whether a bank customer is likely to churn.

## 🚀 Live Demo

**Streamlit App:**  
https://customer-churn-hudycduxkjccrbdiymthu5.streamlit.app/

## 📌 Project Overview

This project uses an **Artificial Neural Network (ANN)** to predict customer churn based on banking and customer information. The model is deployed as an interactive web application using Streamlit.

## ✨ Features

- Predict customer churn probability
- Interactive Streamlit interface
- Real-time predictions
- Data preprocessing using:
  - Label Encoding
  - One-Hot Encoding
  - Feature Scaling
- ANN model built with TensorFlow/Keras

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle

## 📂 Project Structure

```text
customer-churn/
│── app.py
│── model.h5
│── scaler.pkl
│── label_encoder.pkl
│── one_hotEncoder.pkl
│── requirements.txt
│── README.md
```

## 📊 Input Features

The model uses the following customer information:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

## 📈 Output

The application predicts:

- Customer Churn Probability
- Whether the customer is likely to churn or not

Example:

```text
Churn Probability: 30.68%

The customer is not likely to churn.
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AliIbrahi1242003/customer-churn.git
```

Navigate to the project directory:

```bash
cd customer-churn
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📦 Requirements

- Python 3.11
- TensorFlow 2.20
- Streamlit
- Scikit-learn
- Pandas
- NumPy

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 👨‍💻 Author

**Ali Ibrahim**

GitHub: https://github.com/AliIbrahi1242003

---

⭐ If you found this project useful, consider giving it a star on GitHub!
