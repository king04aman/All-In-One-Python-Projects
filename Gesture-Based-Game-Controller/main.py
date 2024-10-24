import cv2
import mediapipe as mp
import numpy as np
import time

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Gesture mappings
GESTURES = {
    "forward": "Move Forward",
    "backward": "Move Backward",
    "left": "Move Left",
    "right": "Move Right",
    "up": "Jump"
}

# Define a function to calculate the direction based on landmarks
def detect_direction(landmarks):
    # Get coordinates of wrist and index finger tip
    wrist = landmarks[0]               # Wrist coordinates
    index_finger_tip = landmarks[8]    # Index finger tip

    # Calculate relative positions of index finger to wrist
    x_diff = index_finger_tip.x - wrist.x  # Difference in X-axis
    y_diff = index_finger_tip.y - wrist.y  # Difference in Y-axis

    # Use thresholds to determine the direction
    if abs(x_diff) > abs(y_diff):  # Horizontal movement dominates
        if x_diff > 0.1:  # Index finger is to the right of the wrist
            return "right"
        elif x_diff < -0.1:  # Index finger is to the left of the wrist
            return "left"
    else:  # Vertical movement dominates
        if y_diff > 0.1:  # Fingers are below wrist
            return "backward"
        elif y_diff < -0.1:  # Fingers are above wrist
            return "up"
    
    # If no significant difference in X or Y, assume pointing forward
    return "forward"

# Video capture for hand gesture recognition
cap = cv2.VideoCapture(0)
prev_time = 0  # To implement delay between gesture changes
delay_interval = 1.0  # 1 second delay between actions

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for natural movement
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect hands
    results = hands.process(frame_rgb)
    
    landmark_list = []
    
    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Collect hand landmark data
            for lm in hand_landmarks.landmark:
                landmark_list.append(lm)

        # Detect direction based on the landmarks
        direction = detect_direction(landmark_list)

        # Check for time delay between actions
        current_time = time.time()
        if current_time - prev_time > delay_interval:
            print(GESTURES[direction])  # Output corresponding action
            prev_time = current_time
    
    # Display the frame with landmarks
    cv2.imshow('Hand Gesture Recognition', frame)
    
    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
