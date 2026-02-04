####################################################################################################################
# File Name    : interactive_test.py
# Description  : Interactive test file to manually test the weather and news tools with user input 
####################################################################################################################

from dotenv import load_dotenv
from src.tools.weather import get_weather
from src.tools.news import get_news

# Load environment variables from .env file
load_dotenv()

def main():
    print("Welcome to the Weather and News Assistant!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Get weather for a city")
        print("2. Get news on a topic")
        print("3. Quit")

        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            city = input("Enter the city name: ")
            try:
                weather_data = get_weather(city)
                print(f"\nWeather data for {city}: {weather_data}")
            except Exception as e:
                print(f"Error fetching weather data: {e}")

        elif choice == "2":
            topic = input("Enter the topic for news: ")
            try:
                news_data = get_news(topic)
                print(f"\nNews for topic '{topic}': ")
                for idx, article in enumerate(news_data["results"], start=1):
                    print(f"\n{idx}. {article['title']}")
                    print(f"   Source: {article['source']}")
                    print(f"   Date: {article['publishedAt']}")
                    print(f"   Link: {article['url']}")
            except Exception as e:
                print(f"Error fetching news data: {e}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()