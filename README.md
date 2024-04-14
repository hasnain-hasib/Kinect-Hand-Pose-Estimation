# Kinect Hand Pose Estimation

This repository contains Python code for performing hand pose estimation using a Kinect sensor and the Mediapipe library. The hand pose estimation is done using infrared (IR) images captured by the Kinect sensor, making it suitable for low-light conditions or pitch-black environments.

## Requirements

To run the code in this repository, you'll need the following dependencies:
- Python 3.x
- OpenCV (cv2)
- NumPy
- Mediapipe
- Freenect

You can install the required Python packages using pip:
```
pip install opencv-python numpy mediapipe freenect
```

## Usage

1. Connect your Kinect sensor to your computer.
2. Run the Python script `kinect_hand_pose_estimation.py`.
3. The script will capture infrared images from the Kinect sensor, detect hand landmarks using the Mediapipe library, and display the hand pose estimation in real-time.

**Note:** The project utilizes infrared (IR) images from the Kinect sensor, making it ideal for scenarios with low-light conditions or complete darkness.

## References

- [Mediapipe Hands](https://google.github.io/mediapipe/solutions/hands.html) - Official documentation for the Mediapipe Hands module.
- [OpenKinect](https://github.com/OpenKinect/libfreenect) - Official GitHub repository for the libfreenect library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
