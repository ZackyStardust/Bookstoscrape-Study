<h1 align="center">
	Books.toscrape Study Project
</h1>

<p align="center">
	<b><i>A series of studies using https://books.toscrape.com and Scrapy, exploring some of its functions and interactions. Also served as an initial study for Pandas.</i></b>
</p>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/ZackyStardust/Warhammer-Scraper?color=blueviolet" />
	<img alt="Number of lines of code" src="https://img.shields.io/tokei/lines/github/ZackyStardust/Warhammer-Scraper?color=blueviolet" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/ZackyStardust/Warhammer-Scraper?color=blue" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/ZackyStardust/Warhammer-Scraper?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/ZackyStardust/Warhammer-Scraper?color=brightgreen" />
</p>

## 🗣️ About

> _A mix of tests using Scrapy, trying to scrape as much information as possible from the books.toscrape websiteç_

Expanding my studies and interest into web scraping, I came across Scrapy, a powerful tool that could scrape big amounts of data in little time. Luckily, while reading the documentation I found the website quotes.toscrape. Although a good place to start, it didn't had much information or structure. Eventually I stumbled upon books.toscrape, with a structure more similar to an online book shop. With that in mind, I tried to see how much information I could scrape - and also, how much of it I could organize into a Excel-compatible file. For this end, I started using and studying Pandas, while also doing some extra things - such as using BeautifulSoup to quickly find the convertion rate from Pounds to Euros, converting the prices of books.toscrape and accordingly organizing into the table.

## 📈 Future Plans

- Adding a script to run the scraper and the parser file automatically.

## ▶️ How to run
- Clone this repo,
- Inside the parent folder, run ```scrapy crawl quotes -O books.csv``` followed by ```bookparse```.
Note: You can change the name of the output file (books.csv) when running the spider, but it will have to be changed inside the parser file accordingly.
