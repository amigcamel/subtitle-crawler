# -*- coding: utf-8 -*-
"""Crawl subhd.com."""
import logging
import json

from scrapy.utils.project import get_project_settings
from scrapy.http import FormRequest
import scrapy

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TCP_PROXY = get_project_settings()['TCP_PROXY']


class SubhdSpider(scrapy.Spider):
    """A subhd.com crawler."""

    name = 'subhd'
    allowed_domains = ['subhd.com']
    start_urls = ['http://subhd.com/']
    _base_url = 'http://subhd.com'

    def parse(self, response):
        """Parse all links."""
        selectors = response.css('a::attr(href)')
        for selector in selectors:
            if selector.re('/do0/\d+'):
                url = f'{self._base_url}{selector.extract()}'
                yield scrapy.Request(url=url, callback=self.parse_do0)
            elif selector.re('/ar0/\d+'):
                url = f'{self._base_url}{selector.extract()}'
                yield scrapy.Request(url=url, callback=self.parse_ar0)
            else:
                url = f'{self._base_url}{selector.extract()}'
                yield scrapy.Request(url=url, callback=self.parse)

    def parse_do0(self, response):
        """Parse "do0" pages."""
        title_tran = response.css('.container h1 a::text').extract_first()
        title_orig = response.css('.container h2 a::text').extract_first()
        output = {
            'url': response.url,
            'title_orig': title_orig,
            'title_tran': title_tran,
        }
        logger.debug(output)
        # yield output
        selectors = response.css('a[href^="/ar0/"]::attr(href)')
        for selector in selectors:
            url = f'{self._base_url}{selector.extract()}'
            yield scrapy.Request(url=url, callback=self.parse_ar0)

    def parse_ar0(self, response):
        """Parse "ar0" pages."""
        sid = response.css('#down::attr(sid)').extract_first()
        formdata = {'sub_id': sid}
        url = 'http://subhd.com/ajax/down_ajax'
        yield FormRequest(
            url=url,
            callback=self.parse_down_ajax,
            formdata=formdata,
            meta={'proxy': f'http://{TCP_PROXY}', '_formdata': formdata},
        )

    def parse_down_ajax(self, response):
        """Parse "ajax_down" page."""
        data = json.loads(response.text)
        if data['success']:
            logging.info(data['url'])
        else:
            logging.warning('fail to get ajax url, resend request...')
            formdata = response.meta.get('_formdata')
            yield FormRequest(
                url=response.url,
                callback=self.parse_down_ajax,
                formdata=formdata,
                meta={'proxy': f'http://{TCP_PROXY}', '_formdata': formdata},
            )
