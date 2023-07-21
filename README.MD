# ZC's FlightPlanning Toolkit

This is a simple proof of concept application that interfaces with FlightAware's API as well as FAA NOTAMS to pull airport, route information and Tracks Information.

This application uses Qt for Pythn and Pandas

## Installation

1. Create a python virtual environment, install package requirements using

`pip install -e .[dev]`

## Build

2. PyInstaller is included in dev extras_require, you can use the following code to generate an executable:

`pyinstaller --noconfirm --onefile --name zc-flightaware-router main.py`

