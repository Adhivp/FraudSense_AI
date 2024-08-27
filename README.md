# FraudSense AI - URL Feature Extraction and Prediction

Welcome to **FraudSense AI**, a Streamlit-based application designed to analyze URLs and predict their safety using advanced machine learning models. The app helps in detecting potentially malicious websites by extracting and evaluating multiple features from the URL.

![FraudSense AI Logo](images/FraudSense_Logo.jpeg)

## Features

This application performs the following tasks:

1. **Extract Address Bar-Based Features**: Analyzes the URL structure to detect common phishing patterns.
2. **Extract Domain-Based Features**: Retrieves domain information and related features to assess the legitimacy of the website.
3. **Extract HTML/JS-Based Features**: Inspects the HTML and JavaScript content of the webpage to identify suspicious behavior.

## Models

FraudSense AI supports two machine learning models for predictions:

- **XGBoost**: A high-performance, scalable tree boosting system.
- **MLP (Multi-Layer Perceptron)**: A type of neural network particularly effective for classification tasks.

## Directory Structure
- **Dataset/**: Contains Datasets in .csv format used for models.
- **images/**: Contains images used in the app, such as the FraudSense AI logo and icons.
- **Notebooks/**: Jupyter notebooks used for exploratory data analysis and model training.
- **pages/**: Python scripts for different pages of the Streamlit app, such as feature explanations and model predictions.
- **Trained_models/**: Pre-trained models used for predictions (`XGBoost.pkl`, `MLP.pkl`).
- **Utils/**: Utility scripts for feature extraction.
- **main.py**: The main entry point for the Streamlit app.
- **requirements.txt**: List of Python dependencies required to run the app.

## Installation
To run this application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Adhivp/FraudSense_AI.git
    ```

2. Navigate to the project directory:
    ```bash
    cd FraudSense_AI
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

## How to Use
1. **Input a URL**: Enter a URL into the text input field.
2. **Choose a Model**: Select either the XGBoost or MLP model for prediction.
3. **Click 'Predict'**: The app will extract features from the URL, use the selected model to predict, and display the probability of the URL being good or bad.

## Pages
- **Features**: Detailed descriptions of the different URL features used for prediction.
- **Datasets**: Information about the datasets used to train the models.
- **Models**: Descriptions and details about the machine learning models implemented in the app.

## License
This project is licensed under the MIT License. See the LICENSE.txt file for more details.

## Acknowledgements
- **Streamlit**: For providing the framework to build this interactive web application.
- **Scikit-learn**: For the machine learning models.
- **Joblib**: For model serialization and deserialization.
