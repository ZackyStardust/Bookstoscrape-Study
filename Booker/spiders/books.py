import scrapy
from ..items import bookkeeper

class BooksSpider(scrapy.Spider):
	name = 'books'
	start_urls = [
		'https://books.toscrape.com/catalogue/page-1.html'
	]
	allowed_domains = ['books.toscrape.com']

	def parse(self, response):
		for product_pod in response.css('article.product_pod'):
			item = bookkeeper()
			item['url'] = 'https://books.toscrape.com/catalogue/' + product_pod.css('h3 a::attr(href)').get()
			yield response.follow(url=item['url'], callback=self.page, meta={'item':item})
		next_page = response.css('.next a::attr(href)').get()
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)
	
	def page(self, response):
		item = response.meta['item']
		item['name'] = response.css('h1::text').get()
		item['image'] = response.css('img::attr(src)').get()
		item['price'] = response.css('.price_color::text').get()
		item['avaliability'] = response.css('tr:nth-child(6) td::text').get()
		item['sinopsis'] = response.css('#product_description+ p::text').get()
		item['tag'] = response.css('li~ li+ li a::text').get()
		yield item
