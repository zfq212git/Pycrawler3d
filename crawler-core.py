import requests
import re
from bs4 import BeautifulSoup

page = requests.get("http://www.leiphone.com")
soup = BeautifulSoup(page.text,"lxml")
find = soup.find(text=re.compile("3D"))
print(find)
