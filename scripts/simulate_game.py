import numpy as np
from rl.model import create_model
from rl.utils import reset_game, perform_action
import csv


def preprocess_data(training_data):
    x = []
    y =[]

    for state, action, reward in training_data:
        state = np.array(state).reshape(.1, 5)
        target = np.zeros(3)
        target[action] = reward
        x.append(state)
        y.append(target)

    x = np.array(x).reshape(.1, 3)
    y = np.array(y)

    return x, y


def simulate_game(model, num_episodes=100):
    training_data = []
    for episode in range(num_episodes):
        state = reset_game()
        game_memory = []
        score = 0
        game_over = False
        step_count = 0
        max_steps = 100  # Define a maximum number of steps per episode to prevent infinite loops

        print(f"\nStarting episode {episode + 1}/{num_episodes}")
        print(f"Initial State: {state}")
        print("starte the game!!!!")
        while not game_over and step_count <max_steps:
            # Predict action probabilities based on the current state
            action_probs = model.predict(np.array(state).reshape(-1, 5))
            action = np.argmax(action_probs)

            # Perform the selected action in the game environment
            new_state, reward, game_over = perform_action(action)

            # Debugging prints
            print(f"State: {state}")
            print(f"Action Probabilities: {action_probs}")
            print(f"Selected Action: {action}")
            print(f"New State: {new_state}, Reward: {reward}, Game Over: {game_over}")
            print(step_count)

            # Store the state, action, and reward in memory
            game_memory.append((state, action, reward))
            state = new_state
            score += reward
            step_count += 1

        if game_over:
            print(f"Episode {episode + 1} ended with game over status.")
        else:
            print(f"Episode {episode + 1} ended with maximum steps reached.")

        # Only keep the memory of games that resulted in a positive score
        if score > 0:
            for data in game_memory:
                training_data.append(data)

    return training_data


def save_training_data_as_csv(training_data, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for state, action, reward in training_data:
            # Flatten the state and append action and reward
            row = list(state) + [action, reward]
            writer.writerow(row)


if __name__ == "__main__":
    model = create_model()
    training_data = simulate_game(model)
    save_training_data_as_csv(training_data, '../data/training_data.csv')
