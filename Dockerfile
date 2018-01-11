FROM python:3.6.3
ENV PROJ_DIR /subtitle-crawler
WORKDIR $PROJ_DIR/subcrawler
ADD . $PROJ_DIR
RUN pip install -r $PROJ_DIR/requirements.txt
RUN mkdir /data
VOLUME ["/data"]
ENTRYPOINT ["scrapy"]
