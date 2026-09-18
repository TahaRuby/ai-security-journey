# Python GUI Projects

A collection of beginner-friendly Python GUI projects built using different Python GUI libraries and frameworks.

## Requirements

- Python 3.12

> **Important:** Python 3.12 is recommended, especially for projects that use Kivy.

## Installation

First, make sure Python 3.12 is installed on your system.

Check your Python version:

```bash
python --version
```

You should see something similar to:

```text
Python 3.12.x
```

### Install Required Packages

Clone or download this repository, then run the `install.py` file.

Using Python:

```bash
python install.py
```

Or on Windows:

```bash
py install.py
```

The `install.py` file will automatically install the required packages.

You can also install the dependencies manually:

```bash
pip install -r requirements.txt
```

## Required Packages

This project uses the following Python packages:

- PySide6
- PyQt6
- Kivy

> **Note:** `tkinter` is normally included with Python and does not need to be installed using `pip`.

## Projects

### 10 - Alarm Clock

**File:** `10_Alarm_clock.py`

A simple alarm clock application with a graphical user interface.

### 11 - BMI Calculator v2

**File:** `11_bmi_calculator_v2.py`

A BMI (Body Mass Index) calculator that calculates BMI based on the user's height and weight.

### 12 - Note App

**File:** `12_Note_App.py`

A simple note-taking application with a graphical user interface.

### 13 - Weather App v2

**File:** `13_weather_App_v2.py`

A weather application that retrieves and displays weather information using the Open-Meteo API.

### 14 - Calculator GUI

**File:** `14_calculator_GUI.py`

A simple calculator application with a graphical user interface.

### 15 - Countdown GUI

**File:** `15_Countdown_GUI.py`

A countdown timer application with a graphical user interface.

### 16 - Gallery GUI

**File:** `16_gallery_GUI.py`

A simple image gallery application built with Kivy.

The application loads images from the `images` folder and allows users to browse through them.

> **Note:** The Gallery GUI requires image files to be placed inside the `images` folder.

## Project Structure

```text
Python-GUI-Projects/
│
├── README.md
├── install.py
├── requirements.txt
│
├── 10_Alarm_clock.py
├── 11_bmi_calculator_v2.py
├── 12_Note_App.py
├── 13_weather_App_v2.py
├── 14_calculator_GUI.py
├── 15_Countdown_GUI.py
├── 16_gallery_GUI.py
│
└── images/
    ├── image1.jpg
    ├── image2.png
    ├── image3.jpeg
    └── image4.jpg
```

## How to Run

After installing the required packages, each project can be run separately.

### Alarm Clock

```bash
python 10_Alarm_clock.py
```

### BMI Calculator

```bash
python 11_bmi_calculator_v2.py
```

### Note App

```bash
python 12_Note_App.py
```

### Weather App

```bash
python 13_weather_App_v2.py
```

### Calculator

```bash
python 14_calculator_GUI.py
```

### Countdown Timer

```bash
python 15_Countdown_GUI.py
```

### Gallery

```bash
python 16_gallery_GUI.py
```

## Gallery Images

The Gallery GUI project uses the `images` folder to load images.

Place your image files inside the folder:

```text
images/
├── image1.jpg
├── image2.png
├── image3.jpeg
└── image4.jpg
```

### Supported Image Formats

- `.jpg`
- `.jpeg`
- `.png`
- `.gif`
- `.bmp`

> **Important:** The gallery requires at least one supported image inside the `images` folder to display content.

## Weather App

The Weather App uses the **Open-Meteo API** to retrieve and display weather information.

An active internet connection is required when using the Weather App.

## Notes

- Each project can be run independently.
- Run `install.py` before running the projects for the first time.
- Python 3.12 is recommended, especially for Kivy-based projects.
- Make sure the required packages are installed before running the applications.
- The Gallery GUI requires an `images` folder containing image files.
- The Weather App requires an active internet connection.

## Learning Goals

These projects are designed to practice:

- Python programming
- GUI development
- Object-Oriented Programming (OOP)
- Working with APIs
- File and folder management
- Timers and events
- User input and validation
- Image handling
- Building small desktop applications
