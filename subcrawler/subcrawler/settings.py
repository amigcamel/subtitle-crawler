"""Scrapy settings."""
# -*- coding: utf-8 -*-
import scrapy.utils.log

from .logconf import _get_handler_custom

scrapy.utils.log._get_handler = _get_handler_custom

BOT_NAME = 'subcrawler'

SPIDER_MODULES = ['subcrawler.spiders']
NEWSPIDER_MODULE = 'subcrawler.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'  # noqa
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 60 * 24 * 30  # one month
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [500]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.LeveldbCacheStorage'

FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
}

ITEM_PIPELINES = {
    'scrapy.pipelines.files.FilesPipeline': 1
}

FILES_STORE = '/data'

# CUSTOM SETTINGS
TCP_PROXY = 'tor:8118'
