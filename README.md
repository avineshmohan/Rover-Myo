# Rover-Myo
Direct bluetooth connection between Linux and Myo armband using Bluegiga BGAPI/BGLib

Tested in a Raspberry Pi. video: https://www.youtube.com/watch?v=AWxEL4l4Fg8

### Pre-requirements for your Myo device
- Firmware version 1.3.1448 or higher
- It is necessary to calibrate your Myo device using the official software.
- Use the Myo dongle bluetooth

### Requirements
- python >=2.6
- pySerial
- enum34

### Execute Sample
The Myo dongle bluetooth must be connected.

- Open the console "terminal" 
- Go to sample folder in the project
- Execute this command:
  ```
  python test_myo.py
-after this Execute this command
  ```
  python print_pose_listener.py
