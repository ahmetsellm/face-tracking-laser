# Face Tracking Laser

Autonomous face tracking system using Python, OpenCV, and STM32 with servo motors.

## How It Works
* The webcam captures the video feed.
* Python and OpenCV detect the face and calculate its center coordinates.
* The coordinates are sent to the STM32 microcontroller via serial port.
* The STM32 processes the data and moves the servo motors to track the target.

## Hardware Used
* STM32 Nucleo-C031C6
* 2x Servo Motors
* Webcam

## Status
Software and simulation are complete. Physical hardware tests will be done after returning to Turkey.
