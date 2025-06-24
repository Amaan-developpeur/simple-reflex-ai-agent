import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def sense(image_path, model_Name):
    #---- Starting the preprocessu=ing of the image--------------
    image = load_img(image_path, target_size=(224,224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    preprocess_image = preprocess_input(image_array)

    # Predicting
    prediction = model_Name.predict(preprocess_image)
    prediction_index = np.argmax(prediction[0])
    class_names = ['Cataract', 'Diabetic_retinopathy', 'Glaucoma', 'Normal']
    predicted_class = class_names[prediction_index]

    confidence = prediction[0][prediction_index]

    return predicted_class, confidence

