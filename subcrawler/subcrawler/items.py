"""Scrapy scraped items."""
import scrapy


class SubItem(scrapy.Item):
    """Subtitle item."""

    file_urls = scrapy.Field()
    files = scrapy.Field()
