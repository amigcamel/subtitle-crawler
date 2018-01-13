subtitle-crawler
===

## Prerequisite
Python 3.6+

## Usage

    scrapy crawl subhd -o output.json

### Docker

Build image:

    docker build -t subcrawler .

Run crawlers:

    docker run -it --rm -v <mount point>:/data subcrawler crawl subhd -o /data/output.json
