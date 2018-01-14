subtitle-crawler
===


## Prerequisite

+ docker-compose 1.13.0+

## Usage

Start crawling:

    docker-compose -d --build
    
See the log:

    docker-compose logs --tail 1 -f

Controlling crawlers via telnet ([scrapy telnet console](https://doc.scrapy.org/en/latest/topics/telnetconsole.html)):

    telnet localhost 6023
    
Monitor haproxy status, visit http://localhost:2090

    
