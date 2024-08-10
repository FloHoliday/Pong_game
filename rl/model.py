from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input

def create_model():
    model = Sequential([
        Input(shape=(5,)),           # Explicitly define the input shape using the Input layer
        Flatten(),                   # Flatten the input, which is now implicitly handled
        Dense(24, activation='relu'), # First hidden layer
        Dense(24, activation='relu'), # Second hidden layer
        Dense(3, activation='softmax') # Output layer with 3 neurons (for stay, up, down actions)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

