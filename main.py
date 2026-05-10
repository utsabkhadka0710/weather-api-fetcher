import requests
import logging
from logging.handlers import RotatingFileHandler
import csv,json
import os


#-----------Logger Setup-------------
# logger initialization
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Console(Terminal) and file handlers initialization
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    "logs/weather_fetcher.log",
    maxBytes = 10000000,
    backupCount = 3
    )

# logging format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
    )

# Setting format for handlers    
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Adding initialized handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)
#-------------------------------------------


#------------Data fetcher function-----------
def fetch_data(latitude, longitude, TIMEOUT=5, RETRY=3):
    """
    Fetch weather data from Open-Meteo API.
    """
    #API url and params 
    url = "https://api.open-meteo.com/v1/forecast?"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,is_day,apparent_temperature,relative_humidity_2m,rain,surface_pressure,wind_speed_10m",
        "timezone": "auto",
        "forecast_days": 1
    }
    
    # Valid Latitude and Longitude checking
    if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        logging.error(f"Fetching didn't started | Invalid Coordinates!!!\n")
        return None
     
    # Fetching data loop with retry logic of fetching failed       
    for attempt in range(0,RETRY):
                
        try:
            logger.info(f"Fetching Started... | url={url} | service= weather_api | fetching_attempt={attempt+1}\n")
            response = requests.get(url, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            logger.info(f"Data Fetched Successfully! | status_code={response.status_code} | url={url}\n")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API Failure!!! | url={url} | Error={e}\n")
        
#----------------------------------------------



#----------------Save To CSV function-------------
def save_to_csv(data, filename="data/weather_data.csv"):
    """
    Saves the fetched weather data (as .csv) into data/weather_data.csv
    """
    
    logger.info(f"Attempt to save fetched data at {filename}...\n")
    
    # Checking if valid data is received before saving to .csv
    if not data:
        logger.error(f"Couldn't save data at {filename} | NO DATA TO SAVE!!!\n")
        return
        
    # Saving the valid weather data as .csv 
    try:
        file_exists = os.path.exists(filename)
        keys = data[0].keys()
        with open(filename,"a",newline="") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            if not file_exists:
                logger.info(f"{filename} doesn't exists!!! | {filename} was created successfully!!!\n")
                writer.writeheader()
            writer.writerows(data)
            logger.info(f"Writing data to {filename}...\n")
        logger.info(f"Data successfully written to {filename}!!!\n")
        return
        
    except Exception: 
        logger.error(f"Failed to save data to {filename}\n")
        
#-------------------------------------------

def main():
    try:
        latitude = float(input("Enter Latitude: "))
        longitude = float(input("Enter Longitude: "))
    except ValueError:
        logger.error("Fetching didn't started | Invalid Numeric Input!")
        return
    
    data = fetch_data(latitude, longitude)
    if not data:
        return
    
    data_to_save = [data["current"]]
    save_to_csv(data_to_save)
    
if __name__ == "__main__":
    main()