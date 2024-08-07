import numpy as np

def preprocess_data(training_data):
    X = []
    y = []

    for state, action, reward in training_data:
        state = np.array(state).reshape(-1, 5)
        target = np.zeros(3)
        target[action] = reward
        X.append(state)
        y.append(target)

    X = np.array(X).reshape(-1, 5)
    y = np.array(y)

    return X, y

def reset_game():
    # Reset the game to the initial state
    return [0, 0, 0, 1, 1]  # Example state: [ball_x, ball_y, paddle_y, ball_dx, ball_dy]

def perform_action(action):
    # Perform the action in the game and return the new state, reward, and if the game is over
    new_state = [0, 0, 0, 1, 1]  # Update this with the actual new state
    reward = 1  # Example reward
    game_over = False  # Update this according to the game logic
    return new_state, reward, game_over
