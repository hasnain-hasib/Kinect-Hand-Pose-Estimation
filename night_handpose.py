import freenect
import numpy as np
import cv2
import mediapipe as mp

# Function to get infrared data from Kinect
def get_video():
    array, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    return array

# Function to preprocess depth data
def pretty_depth(depth):
    np.clip(depth, 0, 2**10-1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth

if __name__ == "__main__":
    # Initialize Mediapipe Hands module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    while 1:
        # Get a frame from the Kinect
        frame = get_video()

        # Display IR image
        frame = pretty_depth(frame)
        cv2.imshow('IR image', frame)

        # Convert the frame to RGB for Mediapipe Hand Tracking
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

        # Detect hands using Mediapipe Hand Tracking
        results = hands.process(rgb_frame)

        # Draw hand landmarks if hands are detected
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                for point in landmarks.landmark:
                    height, width, _ = rgb_frame.shape
                    cx, cy = int(point.x * width), int(point.y * height)
                    cv2.circle(rgb_frame, (cx, cy), 5, (255, 0, 0), -1)

        # Display the frame with hand landmarks
        cv2.imshow('Hand Pose Estimation', rgb_frame)

        # Quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    # Release resources
    cv2.destroyAllWindows()
