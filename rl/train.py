from rl.model import create_model
from rl.utils import simulate_game, preprocess_data
import numpy as np

# Create the model
model = create_model()

# Collect training data
training_data = simulate_game(model, num_episodes=1000)

# Preprocess the data
X, y = preprocess_data(training_data)

# Train the model
model.fit(X, y, epochs=10)

# Save the model
model.save('../data/model.h5')
