import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_image(img_path):

    model = load_model("models/medical_cnn_model.h5")

    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img)

    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    return "Diseased" if prediction[0][0] > 0.5 else "Normal"
