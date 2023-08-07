import tweepy
from other import keys
import requests


def tweet(titulo, url, creador):

    client = tweepy.Client(keys.bearer_token, keys.api_key,
                           keys.api_key_secret, keys.access_token, keys.access_token_secret)
    auth = tweepy.OAuth1UserHandler(
        keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)

    client.create_tweet(text="Según " + creador + ", " +
                        titulo + "\n pillatelo por aquí: " + url)

    print(r'El tweet con el titulo "' + titulo +
          r'" fue publicado exitosamente.')


def news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=co&'
           'sortBy=popularity&'
           # 'q=Medellin&Antioquia&Valle de Aburra&'
           'apiKey=603211156fbc4718adbad10c807ab053')

    response = requests.get(url)

    return response


if __name__ == "__main__":
    # tweet()
    api_result = news().json()
    for article in api_result['articles'][:5]:
        tweet(article['title'], article['url'], article['author'])
