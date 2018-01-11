"""Scrapy settings."""
# -*- coding: utf-8 -*-
BOT_NAME = 'subcrawler'

SPIDER_MODULES = ['subcrawler.spiders']
NEWSPIDER_MODULE = 'subcrawler.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'  # noqa
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 60
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

FEED_EXPORT_ENCODING = 'utf-8'
