# ZC's FlightAware Router

This is a simple proof of concept application that interfaces with FlightAware's API to pull airport and route information.

This application uses PySide6 and Pandas

## Installation

1. Create a python virtual environment, install package requirements using

`pip install -e .[dev]`

## Build

2. PyInstaller is included in dev extras_require, you can use the following code to generate an executable:

`pyinstaller --noconfirm --onefile --name zc-flightaware-router main.py`
