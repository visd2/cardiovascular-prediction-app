# ❤️ Cardiovascular Disease Risk Prediction App

This is an AI-powered web application built with Streamlit to predict the risk of cardiovascular disease based on a user's health metrics and lifestyle choices.

## 🚀 Features

-   **User-Friendly Interface:** Simple and intuitive forms to input personal and medical details.
-   **Instant Risk Prediction:** Uses a pre-trained machine learning model (`scikit-learn`) to provide immediate risk assessment.
-   **Visual Feedback:** Displays the risk probability as a percentage with a color-coded result (Red for High Risk, Green for Low Risk) and a progress bar.
-   **Informative Sidebar:** Provides clear instructions on how to use the app.

## 🛠️ How to Run Locally

Follow these steps to get the application running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/visd2/cardiovascular-prediction-app.git
    cd cardiovascular-prediction-app
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the Model File:**
    You need the pre-trained model file `cardio_model.joblib`. Place it in the root directory of the project.
    *(Note: This file is not included in the repository and must be obtained separately).*

5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

The application will now be running and accessible in your web browser!
