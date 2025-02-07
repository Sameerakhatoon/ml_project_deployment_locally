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

## Problem Statement
This project focuses on developing AI models to predict the average Nusselt number, stream functions, and temperature contours for two-dimensional flow within a square cavity with solid walls. Gravity acts downward (-y direction), with given Rayleigh and Prandtl numbers for various temperature combinations on the left and right walls, while the top and bottom walls are thermally insulated. The cavity is filled with air, assuming natural convection. Using Ansys Fluent and the Boussinesq approximation for buoyancy-driven flow, results are presented as streamlines and static temperature contours.

As the fluid near the left boundary absorbs heat, it becomes less dense and rises due to thermal expansion, creating a convection current as cooler fluid moves in to replace it. This flow, known as natural or free convection, is simulated to model temperature and velocity fields within the cavity. The heat flux Q” at the boundary is calculated to determine the average Nusselt number, with numerical results compared to computational methods.

For this 2-D problem, we consider a square cavity of length 𝐿 where the left wall is at \( T_H \) temperature and the right wall at \( T_L \), with \( T_H > T_L \). The top and bottom walls are adiabatic and thermally insulated. The flow is steady, laminar, and governed by the Navier-Stokes and energy equations. Gravity acts as \( g_y = -9.81 \, m/s^2 \) and \( g_x = 0 \, m/s^2 \), with no volumetric heat generation. The Boussinesq approximation, assuming a linear change in density with temperature, is used. The governing equations are non-dimensionalized with \( U = \alpha/L \), the Rayleigh number \( Ra \), and the Prandtl number \( Pr \).

## Features
- Automated calculation of average Nusselt number, non-dimensional temperature, and stream function contours.
- Visualization of stream function contours to visualize fluid flow patterns.
- Simplified analysis of natural convection scenarios using minimal computational resources.

## Step-by-Step Process

### Loading Data & Packages

#### Preparing the Input Data:
1. Generated simulation data using Ansys Fluent.
2. Created an Excel sheet using Python, based on data from *Heat and Mass Transfer Data Book* by C. P. Kothandaraman. This sheet contained:
   - Average temperature
   - Thermophysical properties of air at each temperature (density, viscosity, specific heat, thermal conductivity, thermal expansion coefficient, etc.)
   - Rayleigh number, Prandtl number, and thermal diffusivity.
   - **[Link to the code file](https://drive.google.com/file/d/1evKUaE1hMlY-K-3QgQpADdiYFjBsrfOe/view)**

#### Simulations:
1. Conducted a grid independence study and exported mesh files.
2. Automated simulations using the Ansys Fluent Python package:
   - Generated training data from 1800 CFD simulations.
   - Overcame challenges using Fluent Core package settings and TUI APIs.
   - Used journals executed in Jupyter Notebook for streamlined workflow.
   - **[Link to the code file](https://drive.google.com/file/d/1MOVBthdLZJf5FdBItB_qY0dHqrmsBv1e/view)**
3. Processed simulation output using Python to structure data for machine learning.
   - **[Link to the code file](https://drive.google.com/file/d/1KqqJIqxjM-QgeCmpjkhZPTFX_QaO8QnK/view)**

### Exploratory Data Analysis & Data Preparation
1. Standardized the Rayleigh number due to its large variance.
2. Scaled temperature and stream function contours to a range of 0 to 1.
3. Trained separate models for average Nusselt number, temperature, and stream contours for better accuracy.

### Train Models & Model Enhancement
- Used train-test split of collected data.
- Applied grid/random search algorithms for hyperparameter tuning.
- **[Link to the code file](https://drive.google.com/file/d/1KqqJIqxjM-QgeCmpjkhZPTFX_QaO8QnK/view)**

### Evaluate Models & Finalize Model
- Tested the model against standard results for Pr = 0.71, Ra = \(10^6, 10^5, 10^4, 10^3\).
- Developed and deployed a Flask-based web application.
- Implemented model deserialization for real-time predictions.
- **[GitHub link](https://github.com/Sameerakhatoon/ml_project_deployment_locally)**
- **[Link to the code file](https://drive.google.com/file/d/1xERCKykxvAdR7aHBhENoroBn1vSEnWoN/view)**

