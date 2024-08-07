import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam


def create_model():
    model = Sequential([
        Flatten(input_shape=(5,)),
        Dense(24, activation='relu'),
        Dense(24, activation='relu'),
        Dense(3, activation='softmax')
    ])
    model.compile(optimizer= Adam(), loss='mse')
    return model



