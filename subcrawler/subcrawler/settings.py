"""Scrapy settings."""
# -*- coding: utf-8 -*-
import scrapy.utils.log

from .logconf import _get_handler_custom

scrapy.utils.log._get_handler = _get_handler_custom

BOT_NAME = 'subcrawler'

SPIDER_MODULES = ['subcrawler.spiders']
NEWSPIDER_MODULE = 'subcrawler.spiders'

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 60 * 24 * 30  # one month
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [500]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.LeveldbCacheStorage'

TELNETCONSOLE_ENABLED = True
TELNETCONSOLE_HOST = '0.0.0.0'

FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
}

ITEM_PIPELINES = {
    'scrapy.pipelines.files.FilesPipeline': 1
}

FILES_STORE = '/data'

# CUSTOM SETTINGS
TCP_PROXY = 'tor:8118'
