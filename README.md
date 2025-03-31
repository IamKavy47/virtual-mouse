# AI Virtual Mouse

## Overview
AI Virtual Mouse is a computer vision-based system that enables hands-free mouse control using hand gestures. It utilizes OpenCV, MediaPipe, and AutoPy to track hand movements and simulate mouse actions, enhancing accessibility and interaction.

## Features
- Hand tracking using MediaPipe
- Cursor movement with index finger gestures
- Click functionality using finger distance detection
- Smooth and responsive interaction
- Real-time FPS display

## Requirements
- Python 3.8 (Mediapipe requires Python 3.8)
- OpenCV
- MediaPipe
- NumPy
- AutoPy

## Installation
```sh
pip install opencv-python mediapipe numpy autopy
```

## Usage
1. Run the script:
   ```sh
   python AIVirtualMouseProject.py
   ```
2. Ensure your webcam is connected.
3. Use hand gestures to move the cursor and click.
4. Press 'q' to exit.

## How It Works
- The `HandTrackingModul.py` detects hand landmarks.
- The index finger controls cursor movement.
- Clicking is performed when the index and middle fingers come close.

## Demo
(Add a GIF or video link here)

## Future Improvements
- Support for drag-and-drop
- Additional gesture controls
- Multi-hand interaction

## Credits
Developed using Python, OpenCV, and MediaPipe.


