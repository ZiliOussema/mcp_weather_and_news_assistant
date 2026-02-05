####################################################################################################################
# File Name    : test_tools.py
# Description  : test tools with direct function calls to verify they work correctly and handle errors gracefully 
####################################################################################################################

from dotenv import load_dotenv
from src.tools.weather import get_weather
from src.tools.news import get_news

# Load environment variables from .env file
load_dotenv()

def test_weather():
    city = "Paris"
    try:
        weather_data = get_weather(city)
        print(f"Weather data for {city}: {weather_data}")
    except Exception as e:
        print(f"Error fetching weather data: {e}")

def test_news():
    topic = "technology"
    try:
        news_data = get_news(topic)
        print(f"News data for topic '{topic}': {news_data}")
    except Exception as e:
        print(f"Error fetching news data: {e}")

if __name__ == "__main__":
    print("Testing weather tool...")
    test_weather()
    print("\nTesting news tool...")
    test_news()