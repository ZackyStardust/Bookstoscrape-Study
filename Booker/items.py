# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class bookkeeper(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	avaliability = scrapy.Field()
	image = scrapy.Field()
	sinopsis = scrapy.Field()
	tag = scrapy.Field()
	url = scrapy.Field()