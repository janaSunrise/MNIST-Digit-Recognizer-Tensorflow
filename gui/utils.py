import numpy as np
import tensorflow as tf

# Load the model for prediction.
model = tf.keras.models.load_model("models/model.h5")


def predict(grid: np.ndarray) -> tuple:
    """Predict the image from the Numpy Array specified."""
    # Normalization
    normalized_digit = grid.reshape((1, 28, 28, 1))
    normalized_digit = normalized_digit.astype('float32') / 255.0

    # Get predictions
    prediction_array = model.predict([normalized_digit])

    return prediction_array.argmax(), prediction_array
