from rl.utils import simulate_game
from rl.model import create_model
import numpy as np

# Create the model
model = create_model()

# Collect training data
training_data = simulate_game(model, num_episodes=1000)

# Save the training data
np.save('../data/training_data.npy', training_data)
