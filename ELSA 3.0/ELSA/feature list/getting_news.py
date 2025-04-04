import requests
import json

def get_news():
    url = ''  #url address
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False
    
def GetNewsUrl():
    return '' #url address

