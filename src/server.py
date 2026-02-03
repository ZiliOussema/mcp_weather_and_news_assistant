####################################################################################################################
# File Name    : server.py 
# Description  : Main server file to run the weather and news assistant
####################################################################################################################

import os  
from  dotenv  import  load_dotenv  

from mcp.server.fastmcp import FastMCP
from tools.weather import get_weather 
from tools.news import get_news 

# Load environment variables from .env file 
load_dotenv()  

# Initialize FastMCP 
mcp = FastMCP("weather-news")

@mcp.tool()  
def weather(city: str) -> dict:  
    """Get current weather data for a given city.
    Args:  
        city (str): Name of the city to fetch weather for.
    Returns:
        dict: Weather data including temperature, humidity, wind speed and description.
    """
    return get_weather(city)


@mcp.tool() 
def news(topic: str) -> dict: 
    """Get latest news articles for a given topic.
    Args:  
        topic (str): Topic to fetch news for.
    Returns:
        dict: News data including headlines and descriptions.
    """  
    return get_news(topic)

if __name__ == "__main__":  
    mcp.run()  
