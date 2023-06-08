import requests
class News:
        def __init__(self,city):
                self.city = city
                news_api_url="https://newsapi.org/v2/everything"
                news_api_key="8ecbb891b1684fa5b20d43b0b1aedb99"
                news_params = {
                        "apiKey": news_api_key,
                        "qInTitle": city,
                }
                news_response = requests.get(news_api_url, params=news_params)
                articles = news_response.json()["articles"]
                three_articles = articles[:3]
                #print(three_articles)
                formatted_articles = [f"W mieście {city}: Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
                print(formatted_articles)
Wiadomosci= News("Wrocław")

