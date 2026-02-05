####################################################################################################################
# File Name    : weather.py 
# Description  : Tool file for weather data fetching 
####################################################################################################################

import  os  
import  requests  

def get_weather(city: str) -> dict:  
    """Fetch weather data for a given city using OpenWeatherMap API.
    Args:  
        city (str): Name of the city to fetch weather for.
    Returns:
        dict: Weather data including temperature, humidity, wind speed and description.
    """  
    api_key = os.getenv("OPENWEATHER_API_KEY") 
    
    if not api_key:  
        raise Exception("OPENWEATHER_API_KEY environment variable not set")
     
    base_url = "https://api.openweathermap.org/data/2.5/weather"  
    params = {  
        "q": city,  
        "appid": api_key,  
        "units": "metric"  
    }
    
    r = requests.get(base_url, params=params, timeout=10) 
    
    # Raise exception if the request was not successful
    if r.status_code != 200:
        raise Exception(f"Error fetching weather data: {r.status_code} - {r.text}")

    data = r.json()  
    return  {  
        "temperature": data["main"]["temp"],  
        "humidity": data["main"]["humidity"],  
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"]  
    }

    
    