def reward_function(params):
    '''
    Enhanced reward function to follow the center line and maintain higher speeds
    '''
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']

    # Calculate markers at varying distances from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Initialize reward
    reward = 1e-3

    # Reward for distance from center
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1

    # Penalize if the car is off track
    if not all_wheels_on_track:
        reward = 1e-3
    else:
        # Reward for higher speeds
        SPEED_THRESHOLD_1 = 2.0  # Lower speed threshold
        SPEED_THRESHOLD_2 = 3.0  # Higher speed threshold
        if speed > SPEED_THRESHOLD_2:
            reward += 1.0
        elif speed > SPEED_THRESHOLD_1:
            reward += 0.5

        # Progress-based reward to encourage finishing the lap quickly
        REWARD_SCALE = 2.0
        time_penalty = steps / 300  # Assuming 300 steps as a reasonable threshold for a fast lap
        reward += (progress / 100) * REWARD_SCALE - time_penalty

    return float(reward)
