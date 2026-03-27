# FocusGuard.AI

A real-time focus monitoring application that uses computer vision to detect when you're distracted during study or work sessions. Built with OpenCV and Python.

## Features

- **Real-time Face Detection**: Uses Haar cascades to detect faces in webcam feed
- **Eye Tracking**: Monitors eye presence to determine focus state
- **Focus States**:
  - **FOCUSED**: Eyes detected, actively engaged with screen
  - **WRITING/READING**: Face detected but eyes not visible (likely reading or writing)
  - **DISTRACTED**: No face detected (looking away from screen)
- **Smart Alerts**: 
  - Visual indicators on screen
  - Audio alerts when writing threshold is exceeded
- **Configurable Thresholds**: Customize detection sensitivity and alert timing

## Requirements

- Python 3.7+
- OpenCV (`opencv-python`)
- Webcam (built-in or external)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tatha07/vityarthi
cd study-helper
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install opencv-python
```

## Usage

1. Ensure your webcam is connected and accessible
2. Run the application:
```bash
python main.py
```

3. The application will start monitoring your focus state
4. Press 'q' to quit the application

## Configuration

You can adjust the following parameters in `main.py`:

- `MISSING_THRESHOLD`: Time in seconds before considering user distracted (default: 2.0)
- `WRITING_THRESHOLD`: Time in seconds before alerting during writing/reading (default: 30.0)

## How It Works

The application uses OpenCV's Haar cascade classifiers to:
1. Detect faces in the webcam feed
2. Within detected faces, look for eyes
3. Determine focus state based on detection results:
   - Eyes present = Focused
   - Face present, eyes absent = Writing/Reading
   - No face = Distracted

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

