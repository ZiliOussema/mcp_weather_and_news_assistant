####################################################################################################################
# File Name    : news.py 
# Description  : Tool file for news data fetching 
####################################################################################################################

import os  
import requests  

def get_news(topic: str) -> dict: 
    """Fetch news articles for a given topic using NewsAPI.
    Args:  
        topic (str): Topic to fetch news for.
    Returns:
        dict: News data including headlines and descriptions.
    """  
    api_key = os.getenv("NEWS_API_KEY")  
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "apiKey": api_key,
        "pageSize": 5,
        "sortBy": "publishedAt",
        "language": "en",
    }
    
    r = requests.get(base_url, params=params, timeout=10) 
    
    # Raise exception if the request was not successful
    if r.status_code != 200:
        raise Exception(f"Error fetching news data: {r.status_code} - {r.text}")
    
    data = r.json()
    articles = data.get("articles", [])
    return {
        "topic": topic,
        "results": [
            {
                "title": a.get("title"),
                "source": (a.get("source") or {}).get("name"),
                "publishedAt": a.get("publishedAt"),
                "url": a.get("url"),
            }
            for a in articles
        ],
    }