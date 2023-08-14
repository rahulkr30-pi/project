import json
import requests

NEWS_API_KEY = 'eb7e540bd4ca415fb40961a480fed6f9'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

def get_latest_news():
    # Fetch the latest news using the API
    response = requests.get(NEWS_API_URL, params={"apiKey": NEWS_API_KEY})
    news_data = response.json()

    # Update the news_data.json file
    with open('data/news_data.json', 'w') as news_file:
        json.dump(news_data, news_file)

    return news_data