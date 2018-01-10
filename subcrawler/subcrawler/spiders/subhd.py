# -*- coding: utf-8 -*-
import logging

import scrapy

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class SubhdSpider(scrapy.Spider):
    name = 'subhd'
    allowed_domains = ['subhd.com']
    start_urls = ['http://subhd.com/']
    _base_url = 'http://subhd.com'

    def parse(self, response):
        selectors = response.css('a::attr(href)')
        for selector in selectors:
            if selectors.re('/do0/\d+'):
                url = f'{self._base_url}{selector.extract()}'
                yield scrapy.Request(url=url, callback=self.parse_do0)
            elif selector.re('/db0/\w+'):
                url = f'{self._base_url}{selector.extract()}'
                yield scrapy.Request(url=url, callback=self.parse)
            elif selector.re('/ar0/\d+'):
                url = f'{self._base_url}{selector.extract()}'
                yield scrapy.Request(url=url, callback=self.parse_ar0)
 
       
    def parse_do0(self, response):
        selectors = response.css('a[href^="/ar0/"]::attr(href)')
        for selector in selectors:
            url = f'{self._base_url}{selector.extract()}'
            yield scrapy.Request(url=url, callback=self.parse_ar0)

    def parse_ar0(self, response):
        sid = response.css('#down::attr(sid)')
        logging.info(f'sid: {sid}')
