# Weather API Data Fetcher

A Python-based weather data fetcher that retrieves live weather information from the Open-Meteo API, logs API activity, and stores weather data into a CSV file.

---

## Features

- Fetches real-time weather data using the Open-Meteo API
- Saves weather data into a CSV file
- Logs API activity and errors
- Retry mechanism for failed requests
- Rotating log files
- Input validation for coordinates

---

## Technologies Used

- Python
- Requests
- Logging
- CSV
- Open-Meteo API

---

## Project Structure

```text
weather-api-fetcher/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── weather_data.csv
│
└── logs/
    └── weather_fetcher.log
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/utsabkhadka0710/weather-api-fetcher.git
```

Move into the project directory:

```bash
cd weather-api-fetcher
```

Create virtual environment:
```bash
python -m venv .venv
```

Activate virtual environment 

- **Linux/MacOS:**
```bash
source .venv/bin/activate
```
- **Windows:**
```cmd
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program:

```bash
python main.py
```

Enter latitude and longitude when prompted.

Example:

```text
Enter Latitude: 27.7172
Enter Longitude: 85.3240
```

---

## Example Data Saved

The application stores weather information such as:

- Temperature
- Apparent Temperature
- Humidity
- Rain
- Surface Pressure
- Wind Speed

---

## API Used

This project uses the Open-Meteo API:

https://open-meteo.com/

---

## Logging

Logs are stored inside:

```text
logs/weather_fetcher.log
```

The project uses rotating log files to prevent excessively large log files.

---

## Future Improvements

- JSON export support
- PostgreSQL database integration
- CLI arguments using argparse
- Async requests
- Docker support
- Automated scheduled fetching

---

## Author

Built by Utsab Khadka