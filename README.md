subtitle-crawler
===


## Prerequisite

+ docker-compose 1.13.0+

## Usage

Clone this project:

    git clone https://github.com/amigcamel/subtitle-crawler

Start crawling:

    docker-compose -d --build
    
See the log:

    docker-compose logs --tail 1 -f

Controlling crawlers via telnet ([scrapy telnet console](https://doc.scrapy.org/en/latest/topics/telnetconsole.html)):

    telnet localhost 6023
    
Monitor haproxy status, visit http://localhost:2090

    
## Data

#### Subtitle files  

All donwloaded files will be saved in `<project_dir>/data/full`

#### http cache  

Cache is stored in `<project_dir>/data/.scrapy`
