from tensorflow.keras.models import load_model

# ------------Loading the Model----------------------
def loading_model(model_path):
    return load_model(model_path)

if __name__ == '__main__':
    model = loading_model('full_model.keras')
