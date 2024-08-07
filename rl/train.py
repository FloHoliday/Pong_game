import numpy as np
from model import create_model
from utils import preprocess_data, reset_game, perform_action

def simulate_game(model, num_episodes=1000):
    training_data = []
    for _ in range(num_episodes):
        state = reset_game()
        game_memory = []
        score = 0
        game_over = False

        while not game_over:
            action_probs = model.predict(np.array(state).reshape(-1, 5))
            action = np.argmax(action_probs)
            new_state, reward, game_over = perform_action(action)
            game_memory.append((state, action, reward))
            state = new_state
            score += reward

        if score > 0:
            for data in game_memory:
                training_data.append(data)

    return training_data

if __name__ == "__main__":
    model = create_model()
    training_data = simulate_game(model)
    X, y = preprocess_data(training_data)
    model.fit(X, y, epochs=10)
    model.save('../data/model.h5')
