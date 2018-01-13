FROM python:3.6.3
ENV PROJ_DIR /subtitle-crawler
ENV TZ=Asia/Taipei
WORKDIR $PROJ_DIR/subcrawler
ADD . $PROJ_DIR
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install -r $PROJ_DIR/requirements.txt
RUN mkdir /data
VOLUME ["/data"]
ENTRYPOINT ["scrapy"]
