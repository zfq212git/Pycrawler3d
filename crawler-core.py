import requests
import re
from bs4 import BeautifulSoup

url = "http://www.leiphone.com"

page = requests.get(url)

soup = BeautifulSoup(page.text,"lxml")

find_target = "3D"
find = soup.find(text=re.compile(find_target))

print(find)
