# ZC's FlightPlanning Toolkit

This is a simple proof of concept application that interfaces with several APIs like FlightAware, FAA NOTAMs, Runway Data, and Weather APIS to fetch several information.

I created this application as my own tool to aid my flight sim hobby, as it is useful to have all these information in one place as opposed to me having to visit different sources to retrieve them.

This application uses Qt for Python to create the GUI.

## Features:
- Get IFR Routing between 2 airports (To / Fro USA Airports Only)
- Fetch D-ATIS for airports (USA Only)
- Get Runway Data for airports
- Get METAR for airports
- Get Decoded METAR for airports
- Fetch NAT Tracks 
- Fetch PACOT Tracks

## Third Party Usage
- Runway data from https://github.com/davidmegginson/ourairports-data.
- Flight Routing and Airport info from FlightAware
- Digital ATIS from https://datis.clowd.io/
- Weather from CheckWxAPI https://www.checkwxapi.com/

## Installation

1. Create a python virtual environment, install package requirements using

`pip install -e .[dev]`

## Build

2. PyInstaller is included in dev extras_require, you can use the following code to generate an executable:

`pyinstaller --noconfirm --onefile --name zc-flightaware-router main.py`

3. API Keys Required

The following services require you to have your own api keys:
1. FlightAware
2. CheckWxAPI

## Screenshots:

### Preferences
![Preferences](https://i.ibb.co/7p41P6B/image.png)

### Route Information
![Route Information](https://i.ibb.co/51bGDbq/image.png)

### Airport Information
![Airport Information](https://i.ibb.co/KXBkmGh/image.png)

### NAT Tracks
![NAT Tracks](https://i.ibb.co/5LHM9ds/image.png)

### Pacific Tracks
![Pacific Tracks](https://i.ibb.co/8X7jD3M/image.png)
