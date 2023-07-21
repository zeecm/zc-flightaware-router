# ZC's FlightPlanning Toolkit

This is a simple proof of concept application that interfaces with FlightAware's API as well as FAA NOTAMS to pull airport, route information and Tracks Information.

This application uses Qt for Pythn and Pandas

## Installation

1. Create a python virtual environment, install package requirements using

`pip install -e .[dev]`

## Build

2. PyInstaller is included in dev extras_require, you can use the following code to generate an executable:

`pyinstaller --noconfirm --onefile --name zc-flightaware-router main.py`

## Screenshots:

![Route Information](https://i.ibb.co/Z6GBBZX/image.png)
![Airport Information](https://i.ibb.co/PQJz61z/image.png)
![NAT Tracks](https://i.ibb.co/9ythRzV/image.png)
![Pacific Tracks](https://i.ibb.co/4ZXLx60/image.png)
