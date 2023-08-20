import os
import pickle
import gdown
import numpy as np

# Pre-load and store the models in a dictionary
loaded_models = {}

def load_model(model_url, model_name):
    model_file_name = f'{model_name}.pkl'
    model_path = os.path.join(os.getcwd(), model_file_name)

    if not os.path.exists(model_path):
        print(f"Downloading model: {model_name}")
        gdown.download(model_url, output=model_path)

    if model_name not in loaded_models:
        with open(model_path, 'rb') as model_file:
            loaded_models[model_name] = pickle.load(model_file)

    return loaded_models[model_name]

def predict_values(input_data, model_name):
    models = {
        'best_rf_nusselt_grid': 'https://drive.google.com/uc?export=download&id=1xZgaghlCM1Oxn_LZ1dzXLNS-bvbE8AH_',
        'best_rf_nusselt_random': 'https://drive.google.com/uc?export=download&id=17K-hfWv0zJN7mhkdJ5ufBMHzxwg0pKFS',
        'best_rf_temp_grid': 'https://drive.google.com/uc?export=download&id=1UWRa_K6jVb0xMTII2AVTdHGTy6W-Js_l',
        'best_rf_temp_random': 'https://drive.google.com/uc?export=download&id=1qRd46bZ0BmHyLSm4NB7jQo4XGs9PPctS',
        'best_rf_stream_grid': 'https://drive.google.com/uc?export=download&id=1MGWjj4kcoR5r3E-BQ580dY6iPvapwx5s',
        'best_rf_stream_random': 'https://drive.google.com/uc?export=download&id=1UWRa_K6jVb0xMTII2AVTdHGTy6W-Js_l',
    }

    model_url = models.get(model_name)
    if model_url is None:
        raise ValueError('Invalid model_name')

    model = load_model(model_url, model_name)
    prediction = model.predict(input_data)
    return prediction

# standardization!!