import pandas as pd
import pickle
import tensorflow as tf
import streamlit as st

# Load model
model = tf.keras.models.load_model("model.h5")

# Load encoders and scaler
with open("label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)

with open("one_hotEncoder.pkl", "rb") as file:
    one_hotEncoder = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# ---------------- Streamlit UI ----------------

st.title("Customer Churn Prediction")

CreditScore = st.number_input("Credit Score", min_value=300, max_value=900, value=600)

Geography = st.selectbox(
    "Geography",
    one_hotEncoder.categories_[0]
)

Gender = st.selectbox(
    "Gender",
    label_encoder.classes_
)

Age = st.slider("Age", 18, 92, 30)

Tenure = st.slider("Tenure", 0, 10, 5)

Balance = st.number_input("Balance", value=0.0)

NumOfProducts = st.slider("Number Of Products", 1, 4, 1)

HasCrCard = st.selectbox("Has Credit Card", [0, 1])

IsActiveMember = st.selectbox("Is Active Member", [0, 1])

EstimatedSalary = st.number_input("Estimated Salary", value=50000.0)

# ---------------- Prediction ----------------

if st.button("Predict"):

    # Encode Geography
    geo_encoded = one_hotEncoder.transform([[Geography]]).toarray()

    geo_encoded_df = pd.DataFrame(
        geo_encoded,
        columns=one_hotEncoder.get_feature_names_out(["Geography"])
    )

    # Encode Gender
    gender_encoded = label_encoder.transform([Gender])[0]

    # Create input dataframe
    input_data = pd.DataFrame({
        "CreditScore": [CreditScore],
        "Gender": [gender_encoded],
        "Age": [Age],
        "Tenure": [Tenure],
        "Balance": [Balance],
        "NumOfProducts": [NumOfProducts],
        "HasCrCard": [HasCrCard],
        "IsActiveMember": [IsActiveMember],
        "EstimatedSalary": [EstimatedSalary]
    })

    # Merge encoded geography
    input_data = pd.concat(
        [input_data.reset_index(drop=True), geo_encoded_df.reset_index(drop=True)],
        axis=1
    )

    # Scale
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    prediction_probability = prediction[0][0]

    st.write(f"### Churn Probability: {prediction_probability:.2%}")

    if prediction_probability > 0.5:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is not likely to churn.")