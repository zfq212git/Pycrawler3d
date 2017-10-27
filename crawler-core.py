import requests
import re
from bs4 import BeautifulSoup

import urllib
import webbrowser

url_list = []
key_word_list = []
data_file = open("data.txt", "r")

break_line = 0

for line in data_file:
	if(break_line ==0 and line[0] == "*"):
		break_line = 1

	if (break_line == 0 and line[0] != "*"):
		url_list.append(line)
	
	if (break_line == 1 and line[0] != "*"):
		key_word_list.append(line)

	



for url in url_list:
	print(url)
	page = requests.get(re.compile(url))
	soup = BeautifulSoup(page.text,"lxml")
	#print(soup)
	for key_word in key_word_list:
		print(key_word)
		find = soup.find_all('a', text=re.compile(key_word))
		print(find)
		for link in find:
			webbrowser.open_new_tab(link.get('href'))

