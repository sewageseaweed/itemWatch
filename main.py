import PyQt5
import requests
from bs4 import BeautifulSoup

URL = input("https://www.amazon.com/Good-Smile-Kancolle-Murakumo-Nendoroid/dp/B075WYLFFH/ref=sr_1_16?keywords=kancolle+nendoroid&qid=1569479114&sr=8-16")
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

link = requests.get(URL, headers=headers)

soup = BeautifulSoup(link.content, 'lxml')

price = soup.find(id="priceblock_ourprice")
price = float(price.text.replace('$', ''))
print('$' + str(price))
