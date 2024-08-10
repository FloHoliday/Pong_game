import numpy as np


# Define the boundaries of the game area
max_x = 9  # Maximum horizontal position (assuming a 10x10 grid)
max_y = 9  # Maximum vertical position

def reset_game():
    ball_x = np.random.randint(0, max_x + 1)
    ball_y = np.random.randint(0, max_y + 1)
    paddle_y = np.random.randint(0, max_y + 1)
    ball_dx = np.random.choice([-1, 1])
    ball_dy = np.random.choice([-1, 1])

    return [ball_x, ball_y, paddle_y, ball_dx, ball_dy]


def perform_action(action, state):
    ball_x, ball_y, paddle_y, ball_dx, ball_dy = state

    # Update the paddle's position based on the action
    if action == 0:  # Move paddle up
        paddle_y = max(paddle_y - 1, 0)  # Ensure it doesn't go out of bounds
    elif action == 1:  # Move paddle down
        paddle_y = min(paddle_y + 1, max_y)  # Ensure it doesn't go out of bounds

    # Update the ball's position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for game-over conditions (e.g., if the ball goes out of bounds)
    game_over = (ball_x < 0 or ball_x > max_x or ball_y < 0 or ball_y > max_y)

    # The new state after the action
    new_state = [ball_x, ball_y, paddle_y, ball_dx, ball_dy]

    # Compute the reward based on the new state
    reward = compute_reward(new_state)  # Implement this function

    return new_state, reward, game_over

def compute_reward(new_state):
    ball_x, ball_y, paddle_y, ball_dx, ball_dy = new_state

    if ball_x > 380: # Ball goet past right paddle
        return 1 # Positiv reward for wining a point
    elif ball_x < -380: # Ball goes past left paddle
        return -1 # Negative reward for losing a point
    else:
        return 0 # Neutral reward for just continuing the game


