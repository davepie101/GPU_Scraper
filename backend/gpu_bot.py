#!/usr/bin/env python3

import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def newEgg():
	URL = "https://www.newegg.com/p/pl?N=101582767%20601357282"

	page = requests.get(URL)
	soup = BeautifulSoup(page.content,features="html.parser")
	items = soup.find("div", {"class": "items-grid-view"})

	for item in items.findAll("div", {"class": "item-cell"}):
		itemTitle = item.find("a", {"class": "item-title"})
		print(itemTitle)

def adorama():
	URL = "https://www.adorama.com/l/?searchinfo=rtx%203070&sel=Item-Condition_New-Items"
	req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage,features="html.parser")

	items = soup.find("div", {"class": "item-list"})

	print(len(items.findAll("div", {"class": "item"})))
	for item in items.findAll("div", {"class": "item-details"}):
		itemTitle = item.find("a")
		print(itemTitle.text)
		
		
	

if __name__ == '__main__':
	adorama()	
