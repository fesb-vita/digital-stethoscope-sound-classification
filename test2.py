import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import backend as K

new_model = tf.keras.models.load_model('./models/my_model2.keras')
weights  = new_model.get_weights()


new_model.save_weights('model_weights.h5')