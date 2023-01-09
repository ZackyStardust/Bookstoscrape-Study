import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# First, find the exchange rate of GBP to EUR.
URL = 'https://www.x-rates.com/calculator/?from=GBP&to=EUR&amount=1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
eur = soup.find("span", {"class": "ccOutputRslt"}).next_element

# Second, remove the pound symbol and multiply by the GBP to EUR rate.
books = pd.read_csv("books.csv", index_col=False)
books['price'] = books['price'].str.replace('£', '')
for index in books.index:
	books.loc[index, 'price'] = float(books.loc[index, 'price']) * float(eur)
	books.loc[index, 'price'] = round(float(books.loc[index, 'price']), 2)

# Third, clean the avaliability column and multiply the EUR price by the avaliability value.
for index in books.index:
	books.loc[index, 'avaliability'] = re.sub('\D', '', books.loc[index, 'avaliability'])
books['total_value'] = ''
for index in books.index:
	books.loc[index, 'total_value'] = float(books.loc[index, 'price']) * int(books.loc[index, 'avaliability'])
	books.loc[index, 'total_value'] = round(float(books.loc[index, 'total_value']), 2)

#final_sum = 0
#for index in books.index:
#	final_sum = final_sum + float(books.loc[index, 'total_value'])
#books.loc[len(books)] = ['', '', 'Total Sum', '', '', '', '', '']
#books.loc[1000, 'total_value'] = final_sum
#books.to_csv('books_altered.csv', index=False)