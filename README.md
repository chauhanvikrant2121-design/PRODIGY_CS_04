# Prodigy InfoTech Cybersecurity Internship - Task 4

## Simple Keylogger
A basic, lightweight Python script designed to demonstrate endpoint logging mechanics by recording keyboard inputs and saving them locally to a text file.

## Features
- Background keyboard monitoring using the `pynput` listener framework.
- Local capture of standard alphanumeric inputs.
- Clean formatting for simple space inputs and line breaks.
- Interactive safety execution switch using the `ESC` key to end the tracking thread seamlessly.

## Project Structure
```text
PRODIGY_CS_04/
├── keylogger.py   # Main implementation script
├── key_log.txt    # Local text file destination for keys
└── README.md      # Documentation file