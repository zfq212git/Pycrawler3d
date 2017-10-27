import requests
import re
from bs4 import BeautifulSoup

import urllib
import webbrowser

url = "http://www.leiphone.com"

page = requests.get(url)

soup = BeautifulSoup(page.text,"lxml")

find_target1 = "3D"
find_target2 = "三维"

find1 = soup.find_all('a', text=re.compile(find_target1))
find2 = soup.find_all('a', text=re.compile(find_target2))

#print(find)

for link in find1:
    webbrowser.open_new_tab(link.get('href'))

for link in find2:
    webbrowser.open_new_tab(link.get('href'))

