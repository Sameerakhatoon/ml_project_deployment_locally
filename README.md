# Automated Natural Convection CFD Results

Simplifying natural convection analysis by automating the prediction of heat transfer characteristics based on Rayleigh and Prandtl numbers.

![Project Demo](demo.gif)

## Overview
This project aims to revolutionize natural convection analysis by providing a simplified and efficient solution for predicting key heat transfer characteristics. Traditionally, computational fluid dynamics (CFD) simulations for such scenarios require significant computational resources and time. This project simplifies the process by automating the prediction of average Nusselt number, non-dimensional temperature, and stream function contours based on given Rayleigh and Prandtl numbers.

## Features
- Automated calculation of average Nusselt number, non-dimensional temperature, and stream function contours.
- Visualization of stream function contours to visualize fluid flow patterns.
- Simplified analysis of natural convection scenarios using minimal computational resources.

## Motivation
The motivation behind this project is to overcome the limitations of traditional CFD simulations that demand substantial computing power and expertise. By automating the analysis process, we make it accessible to a wider range of users without compromising accuracy.

## Models
The models used for predicting average Nusselt number and non-dimensional temperature have been developed using machine learning techniques. These models offer a more efficient and resource-friendly alternative to traditional CFD simulations. Here's an overview:

### Model Development
The machine learning models were trained using a dataset generated from validated CFD simulations. This dataset covers a wide range of scenarios(Full Laminar Range - Ra ranging from 10^3 to 10^6) with varying Rayleigh and Prandtl numbers, ensuring the models generalize well to different conditions. Random Forest models have undergone hyperparameter tuning using both Grid Search and Random Search Cross-Validation to optimize their performance.

### Usage
The trained Random Forest models are included as serialized `.pkl` files. To use the models for predictions, follow these steps:

1. Firstly, download those models by running download_models.py.
2. Deserialize the model using through WebApp(When model used for the first time, it get deserialized & stored, this may take some time as model gets built back from .pkl file)
3. Provide the required input, which typically includes Rayleigh and Prandtl numbers.
4. Obtain predictions for average Nusselt number and non-dimensional temperature.

## Getting Started
### Prerequisites
- Python 3.11.4
- NumPy 1.25.1
- Scikit-Learn 1.3.0
- Matplotlib 3.7.2
- Flask 2.0.1
- Requests 2.26.0
- gdown

### Installation
1. Clone this repository: git clone https://github.com/Sameerakhatoon/ml_project_deployment_locally.git
cd automated-natural-convection
2. Create and activate a virtual environment:
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```  
- On macOS and Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
3. Install project dependencies:
- pip install -r requirements.txt
- download all models
    - python download_models.py

## Usage
1. Run the Flask app to access the automated prediction tool:
- flask run
Access the app in your browser at `http://localhost:5000`.

2. Enter the Rayleigh and Prandtl numbers in the provided fields and submit the form.

3. View the calculated average Nusselt number, non-dimensional temperature, and stream function contours on the results page.
