import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="🩺 Cardiovascular Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("cardio_model.joblib")
        return model
    except Exception as e:
        st.error(f"⚠️ Error loading model file: {e}")
        return None

model = load_model()

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>💓 Heart Health App</h2>", unsafe_allow_html=True)
    st.info("This AI-powered app predicts your risk of cardiovascular disease based on lifestyle and health metrics.")
    st.markdown("---")
    st.markdown("**Instructions:**")
    st.markdown("""
    1. Fill in your personal and health details.
    2. Click **Predict My Risk**.
    3. View your cardiovascular risk visually.
    """)
    st.markdown("---")
    st.markdown("**Developer:** Harshvardhan 🧠")

# -------------------------------
# App Title
# -------------------------------
st.markdown(
    "<h1 style='text-align:center; color:#D7263D;'>❤️ Cardiovascular Disease Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown("<p style='text-align:center; font-size:18px;'>Enter your details below to estimate your heart disease risk.</p>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Input Section in Cards
# -------------------------------
with st.expander("👤 Personal Info"):
    col1, col2 = st.columns(2)
    with col1:
        Sex = st.selectbox("Sex", ["Male", "Female"], help="Select your biological sex")
        Age_Category = st.selectbox(
            "Age Category", ["18-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65+"],
            help="Select your age range"
        )
        Height_cm = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
        Weight_kg = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        BMI = st.number_input("BMI", 10.0, 60.0, 24.0)
    with col2:
        Smoking_History = st.selectbox("Smoking History", ["Never", "Former", "Current"])
        Alcohol_Consumption = st.slider("Alcohol Drinks/week", 0.0, 20.0, 2.0)
        Fruit_Consumption = st.slider("Fruit Servings/day", 0.0, 10.0, 2.0)
        Green_Vegetables_Consumption = st.slider("Veg Servings/day", 0.0, 10.0, 3.0)
        FriedPotato_Consumption = st.slider("Fried Potato Servings/week", 0.0, 10.0, 1.0)

with st.expander("💊 Medical History"):
    col1, col2 = st.columns(2)
    with col1:
        General_Health = st.selectbox("General Health", ["Excellent", "Very Good", "Good", "Fair", "Poor"])
        Checkup = st.selectbox("Medical Checkup Frequency", ["Within past year", "1-2 years", "2+ years", "Never"])
        Exercise = st.selectbox("Exercise Regularly", ["Yes", "No"])
        Skin_Cancer = st.selectbox("Skin Cancer", ["Yes", "No"])
    with col2:
        Other_Cancer = st.selectbox("Other Cancer", ["Yes", "No"])
        Depression = st.selectbox("Depression", ["Yes", "No"])
        Diabetes = st.selectbox("Diabetes", ["Yes", "No"])
        Arthritis = st.selectbox("Arthritis", ["Yes", "No"])

st.markdown("---")

# -------------------------------
# Predict Button & Display
# -------------------------------
if st.button("🔍 Predict My Risk"):
    if model is None:
        st.error("Model not loaded. Please check cardio_model.joblib.")
    else:
        input_dict = {
            'General_Health':[General_Health],
            'Checkup':[Checkup],
            'Exercise':[Exercise],
            'Skin_Cancer':[Skin_Cancer],
            'Other_Cancer':[Other_Cancer],
            'Depression':[Depression],
            'Diabetes':[Diabetes],
            'Arthritis':[Arthritis],
            'Sex':[Sex],
            'Age_Category':[Age_Category],
            'Smoking_History':[Smoking_History],
            'Height_(cm)':[Height_cm],
            'Weight_(kg)':[Weight_kg],
            'BMI':[BMI],
            'Alcohol_Consumption':[Alcohol_Consumption],
            'Fruit_Consumption':[Fruit_Consumption],
            'Green_Vegetables_Consumption':[Green_Vegetables_Consumption],
            'FriedPotato_Consumption':[FriedPotato_Consumption]
        }
        input_df = pd.DataFrame(input_dict)

        try:
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1] * 100

            # Visual risk meter
            if prediction == 1:
                st.markdown(f"<h3 style='text-align:center; color:red;'>🚨 High Risk ({probability:.1f}%)</h3>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h3 style='text-align:center; color:green;'>💚 Low Risk ({100-probability:.1f}%)</h3>", unsafe_allow_html=True)

            st.progress(int(probability))  # Red progress bar for risk

        except Exception as e:
            st.error(f"⚠️ Error during prediction: {e}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("<hr><p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit & ML</p>", unsafe_allow_html=True)
