import os
import gdown

def download_models():
    models = {
        'best_rf_nusselt_grid': 'https://drive.google.com/uc?export=download&id=1xZgaghlCM1Oxn_LZ1dzXLNS-bvbE8AH_',
        'best_rf_nusselt_random': 'https://drive.google.com/uc?export=download&id=17K-hfWv0zJN7mhkdJ5ufBMHzxwg0pKFS',
        'best_rf_temp_grid': 'https://drive.google.com/uc?export=download&id=1UWRa_K6jVb0xMTII2AVTdHGTy6W-Js_l',
        'best_rf_temp_random': 'https://drive.google.com/uc?export=download&id=1qRd46bZ0BmHyLSm4NB7jQo4XGs9PPctS',
        'best_rf_stream_grid': 'https://drive.google.com/uc?export=download&id=1MGWjj4kcoR5r3E-BQ580dY6iPvapwx5s',
        'best_rf_stream_random': 'https://drive.google.com/uc?export=download&id=1UWRa_K6jVb0xMTII2AVTdHGTy6W-Js_l',
    }

    for model_name, model_url in models.items():
        model_file_name = f'{model_name}.pkl'
        model_path = os.path.join(os.getcwd(), model_file_name)

        if not os.path.exists(model_path):
            print(f"Downloading model: {model_name}")
            gdown.download(model_url, output=model_path)
        else:
            print(f"Model {model_name} already downloaded")

if __name__ == '__main__':
    download_models()