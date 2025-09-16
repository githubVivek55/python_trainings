import requests
api_key = ""

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=')

response = requests.get(url)
print(response.json())
print(response.status_code)
data = response.json()
articles = data['articles']
for article in articles:
    print(article['title'])
print(f"Total articles: {len(articles)}")
