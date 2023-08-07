import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=co&'
       'sortBy=popularity&'
       # 'q=Medellin&Antioquia&Valle de Aburra&'
       'apiKey=603211156fbc4718adbad10c807ab053')

response = requests.get(url)

print(response.json())
