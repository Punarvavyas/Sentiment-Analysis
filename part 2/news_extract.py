import pprint
import requests
import re

secret = 'ee3b516efc134a1e84719ecf0771892f'
url = 'https://newsapi.org/v2/everything?'
key_words = ["Canada", "University", "Dalhousie University", "Halifax", "Canada Education"]

count = 0
for key_word in key_words:

    parameters = {
        'q': key_word,
        'pageSize': 100,
        'apiKey': secret
    }

    response = requests.get(url, params=parameters)
    response_json = response.json()

    for i in response_json['articles']:
        fname = "news" + str(count) + ".txt"
        with open(fname, 'w+', encoding='utf-8') as fp:
            news = "title : " + str(i['title']) + " Content : " + str(i['content']) + " Description : " + str(i['description'])
            news = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', news)
            fp.write(news)

        count = count + 1
