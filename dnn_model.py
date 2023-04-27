import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

loaded_model = load_model('my_model.h5')


def predict_week(groceries_data):
    #print(groceries_data)
    groceries_data_np = np.array(groceries_data)
    groceries_data_np = groceries_data_np.reshape(1, 60)
    #print(groceries_data_np.shape)
    prediction = loaded_model.predict(np.array(groceries_data_np)).round()
    #print(type(prediction[0]))

    return prediction[0].tolist()
