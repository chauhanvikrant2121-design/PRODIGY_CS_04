# Prodigy InfoTech Cybersecurity Internship - Task 4

## Internship
- **Organization:** Prodigy InfoTech
- **Role:** Cybersecurity Intern
- **Domain:** Endpoint Security & Monitoring

## Task Objective
The objective of this task is to create a basic keystroke logging program that records and stores user keyboard inputs. This project demonstrates how background event handlers and system hooks function, providing foundational insight into endpoint telemetry, activity logging, and user input monitoring from an educational and defensive programming perspective.

## Dataset
- **Data Source:** Real-time user keyboard event streams (generated locally during execution).
- **Storage Destination:** `key_log.txt` (A locally generated text file containing captured alphanumeric inputs).

## Technologies Used
- **Programming Language:** Python 3.x
- **Core Library:** `pynput` (specifically the `keyboard.Listener` framework)
- **Development Environment:** Visual Studio Code (VS Code)
- **Version Control:** Git & GitHub

## Project Structure
```text
PRODIGY_CS_04/
├── keylogger.py   # Main implementation script containing the listener logic
├── key_log.txt    # Local text file destination where keys are recorded
└── README.md      # Comprehensive project documentation