# Emotion Classifier App

This is a Streamlit-based web application for detecting emotions in text using a pre-trained PySpark model. It allows users to input text, predicts the emotion associated with it, and provides a confidence score for the prediction. The app also provides monitoring capabilities to track page visits and analyze emotion classifier metrics.

## Features

- Emotion detection in text input.
- Real-time prediction of emotions using a pre-trained PySpark model.
- Visualization of prediction results using interactive charts.
- Monitoring capabilities to track page visits and classifier metrics.
- Database integration for storing page visit and prediction details.

## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/Emotion-Classifier-App.git
    cd Emotion-Classifier-App
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up MySQL Database:**

    - Ensure you have MySQL installed and running.
    - Create a database named `DB`.
    - Update `database.py` with your MySQL connection details.

4. **Run the Application:**

    ```bash
    streamlit run app.py
    ```

## Usage

- **Home:** Allows users to input text for emotion detection. Predictions and confidence scores are displayed along with interactive charts showing prediction probabilities.
- **Monitor:** Provides monitoring capabilities to track page visits and analyze emotion classifier metrics. Users can view page visit details, page metrics, and emotion classifier metrics.

## Components

### 1. Backend

- **Spark Model Loading:** Loads the pre-trained PySpark model for emotion detection.
- **Prediction Function:** Defines a function to predict emotions using the loaded model.
- **Database Integration:** Utilizes MySQL for storing page visit and prediction details.
- **Database Functions:** Includes functions to create tables, add details, and view data from the database.

### 2. Frontend

- **Streamlit Application:** Implements the web interface for the emotion classifier app.
- **User Input:** Provides a text area for users to input text for emotion detection.
- **Prediction Display:** Shows predicted emotions and confidence scores.
- **Interactive Charts:** Visualizes prediction results using Altair and Plotly Express charts.
- **Monitoring:** Enables users to monitor page visits and emotion classifier metrics.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.
